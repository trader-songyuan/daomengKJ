import tkinter as tk
import tkinter.messagebox as messagebox
from tkinter import StringVar
from jiami import *
from test import Post, test_token
import os

app = tk.Tk()
app.title('到梦空间')
app.geometry('1200x880')

tk.Label(app, text='User name:', font=('Arial', 14)).place(x=10, y=0)
tk.Label(app, text='Password:', font=('Arial', 14)).place(x=10, y=35)

entry_usr_name = tk.Entry(app, font=('Arial', 14))
entry_usr_name.pack()
entry_usr_name.place(x=120, y=0)
entry_usr_pwd = tk.Entry(app, font=('Arial', 14), show="*")
entry_usr_pwd.pack()
entry_usr_pwd.place(x=120, y=35)

tk.Label(app, text='选择查询id', font=('Arial', 14)).place(x=500, y=0)
tk.Label(app, text='选择报名id', font=('Arial', 14)).place(x=500, y=35)

id1 = tk.Entry(app, font=('Arial', 14), width=7)
id1.pack()
id1.place(x=620, y=0)

id2 = tk.Entry(app, font=('Arial', 14), width=7)
id2.pack()
id2.place(x=620, y=35)


class Main:

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
        a = Post()
        a.get_ids(self.token, self.uid)
        messagebox.showinfo('欢迎您', self.name)
        names = []
        for name, id, statusText in zip(a.names, a.ids, a.statusTexts):
            names.append(name + '   {}   {}'.format(id, statusText))
        list1 = StringVar(value=names)
        lb = tk.Listbox(app, listvariable=list1, height=len(names), width=67)
        lb.pack()
        lb.place(x=6, y=65)

    def chiken(self):
        id = id1.get()
        a = Post()
        res = a.get_info(id, self.token, self.uid)
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
            messagebox.showwarning(title='出错了', message='查询失败，请检查id')

    def enter(self):
        id = id2.get()
        a = Post()
        res = a.join(id, self.token, self.uid)
        if res:
            messagebox.showinfo(title='报名详情', message=res['msg'])
        else:
            messagebox.showwarning(title='出错了', message='查询失败，请检查id')


def login():
    main = Main()
    if main.login():
        main.read()
        main.get_id()
    else:
        None


def chiken():
    main = Main()
    if main.login():
        main.read()
        main.chiken()
    else:
        pass

def join():
    main = Main()
    if main.login():
        main.read()
        main.enter()
    else:
        pass


b = tk.Button(app, text='登录查询', font=('Arial', 12), width=10, height=1, command=login)
b.pack()
b.place(x=380, y=12.5)

b1 = tk.Button(app, text='活动信息查询', font=('Arial', 12), width=10, height=1, command=chiken)
b1.pack()
b1.place(x=720, y=0)

b1 = tk.Button(app, text='报名活动', font=('Arial', 12), width=10, height=1, command=join)
b1.pack()
b1.place(x=720, y=32)

app.mainloop()
