import tkinter as tk
import tkinter.messagebox as messagebox
from tkinter import StringVar
from jiami import *
from test import Post, test_token
import os

app = tk.Tk()
app.title('到梦空间')
app.geometry('1060x800')

tk.Label(app, text='User name:', font=('Arial', 14)).place(x=10, y=0)
tk.Label(app, text='Password:', font=('Arial', 14)).place(x=10, y=35)

entry_usr_name = tk.Entry(app, font=('Arial', 14))
entry_usr_name.place(x=120, y=0)
entry_usr_pwd = tk.Entry(app, font=('Arial', 14), show="*")
entry_usr_pwd.place(x=120, y=35)

tk.Label(app, text='输入查询id', font=('Arial', 14)).place(x=500, y=0)
tk.Label(app, text='输入报名id', font=('Arial', 14)).place(x=500, y=35)
tk.Label(app, text='输入退出id', font=('Arial', 14)).place(x=500, y=70)

id1 = tk.Entry(app, font=('Arial', 14), width=7)
id1.place(x=620, y=0)

id2 = tk.Entry(app, font=('Arial', 14), width=7)
id2.place(x=620, y=35)

id3 = tk.Entry(app, font=('Arial', 14), width=7)
id3.place(x=620, y=70)


class Main(Post):

    def read(self):
        with open('a.ini', 'r', encoding='utf-8') as f:
            self.token = f.readline().rstrip()
            self.name = f.readline().rstrip()
            self.uid = f.readline().rstrip()

    def login(self):
        acc = entry_usr_name.get()
        pwd = entry_usr_pwd.get()

        if os.path.exists('a.ini'):
            if test_token():
                return True
            else:
                messagebox.showwarning(title='出错了', message='登录失效，请重新登录')
                os.remove('a.ini')
                return False
        else:
            if get_token(acc, pwd):
                return True
            else:
                messagebox.showwarning(title='出错了', message='请检查账号密码')
                return False

    def get_id(self):
        self.get_ids(self.token, self.uid)
        messagebox.showinfo('欢迎您', self.name)
        names = []
        for name, id, statusText in zip(self.names, self.ids, self.statusTexts):
            names.append(name + '   {}   {}'.format(id, statusText))
        list1 = StringVar(value=names)
        lb1 = tk.Listbox(app, listvariable=list1, height=len(names), width=67)
        lb1.place(x=6, y=65)

    def can_join(self):
        names = ['可报名活动']
        if self.get_can_join(self.token, self.uid):
            for name, id, statusText in zip(self.names, self.ids, self.statusTexts):
                names.append(name + '   {}   {}'.format(id, statusText))
                list1 = StringVar(value=names)
                lb2 = tk.Listbox(app, listvariable=list1, height=len(names), width=67)
                lb2.place(x=500, y=245)
        else:
            messagebox.showwarning('出错了', '没有活动')

    def chiken(self):
        id = id1.get()
        res = self.get_info(id, self.token, self.uid)
        if res:
            app1 = tk.Toplevel(app)
            app1.geometry('643x360')
            app1.title('详细信息')
            tk.Label(app1, text=res['data']['activityName'], font=('Arial', 14)).place(x=100, y=0)
            tk.Label(app1, text='活动名称', font=('Arial', 14)).place(x=0, y=0)
            tk.Label(app1, text=res['data']['address'], font=('Arial', 14)).place(x=100, y=25)
            tk.Label(app1, text='活动地址', font=('Arial', 14)).place(x=0, y=25)
            tk.Label(app1, text=res['data']['joindate'], font=('Arial', 14)).place(x=100, y=50)
            tk.Label(app1, text='报名时间', font=('Arial', 14)).place(x=0, y=50)
            tk.Label(app1, text=res['data']['startdate'], font=('Arial', 14)).place(x=100, y=75)
            tk.Label(app1, text='活动时间', font=('Arial', 14)).place(x=0, y=75)
            tk.Label(app1, text=res['data']['specialList'][0]['name'], font=('Arial', 14)).place(x=100, y=100)
            tk.Label(app1, text='积分类型', font=('Arial', 14)).place(x=0, y=100)
            tk.Label(app1, text=res['data']['specialList'][0]['unitcount'], font=('Arial', 14)).place(x=100, y=125)
            tk.Label(app1, text='积分数量', font=('Arial', 14)).place(x=0, y=125)
        else:
            messagebox.showwarning(title='出错了', message='查询失败，请检查活动id')

    def enter(self):
        id = id2.get()
        res = self.join(id, self.token, self.uid)
        if res:
            if res['code'] == '100':
                messagebox.showinfo(title='报名详情', message='报名成功')
            else:
                messagebox.showinfo(title='报名详情', message=res['msg'])
        else:
            messagebox.showwarning(title='出错了', message='查询失败，请检查id')

    def get_joined(self):
        res = self.get_activity(self.token, self.uid)
        names = []
        ids = []
        heights = ['已报名活动']
        if res:
            for li in res['data']['list']:
                if li['statusText'] == '报名中':
                    names.append(li['name'])
                    ids.append(li['aid'])
            if names:
                for name, id in zip(names, ids):
                    heights.append(name + '   {}'.format(id))
                    list1 = StringVar(value=heights)
                    self.lb3 = tk.Listbox(app, listvariable=list1, height=len(heights), width=67)
                    self.lb3.place(x=500, y=105)
            else:
                messagebox.showwarning('出错了', '没有已报名活动')

    def concle(self):
        id = id3.get()
        res = self.get_info(id, self.token, self.uid)
        if res:
            signUpId = str(res['data']['signUpId'])
            if self.get_cancle(signUpId, self.token, self.uid)['code'] == '100':
                messagebox.showinfo(title='成功', message='取消报名成功')
        else:
            messagebox.showwarning(title='出错了', message='失败，请检查活动id')
main = Main()

def login():
    if main.login():
        main.read()
        main.get_id()
    else:
        None


def chiken():
    if main.login():
        main.read()
        main.chiken()
    else:
        pass


def join():
    if main.login():
        main.read()
        main.enter()
    else:
        pass


def can_join():
    if main.login():
        main.read()
        main.can_join()
    else:
        pass


def joined():
    if main.login():
        main.read()
        main.get_joined()
    else:
        pass


def concle():
    if main.login():
        main.read()
        main.concle()
        main.lb3.destroy()
    else:
        pass


b = tk.Button(app, text='登录查询', font=('Arial', 12), width=10, height=1, command=login)
b.place(x=380, y=12.5)

b1 = tk.Button(app, text='活动信息查询', font=('Arial', 12), width=10, height=1, command=chiken)
b1.place(x=720, y=0)

b2 = tk.Button(app, text='报名活动', font=('Arial', 12), width=10, height=1, command=join)
b2.place(x=720, y=32)

b2 = tk.Button(app, text='退出活动', font=('Arial', 12), width=10, height=1, command=concle)
b2.place(x=720, y=64)

b3 = tk.Button(app, text='查询已报名活动', font=('Arial', 12), width=12, height=1, command=joined)
b3.place(x=850, y=10)

b4 = tk.Button(app, text='查询可报名活动', font=('Arial', 12), width=12, height=1, command=can_join)
b4.place(x=850, y=52)

app.mainloop()
