import tkinter as tk
import tkinter.messagebox as messagebox
from tkinter import StringVar
from jiami import *
from test import Post

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
    try:
        with open('a.ini', 'r', encoding='utf-8') as f:
            self.token = f.readline().rstrip()
            self.name = f.readline().rstrip()
            self.uid = f.readline().rstrip()
    except:
        None
    def login(self):
        acc = entry_usr_name.get()
        pwd = entry_usr_pwd.get()
        try:
            with open('a.ini', 'r', encoding='utf-8') as f:
                self.token = f.readline().rstrip()
                self.name = f.readline().rstrip()
                self.uid = f.readline().rstrip()
        except:
            print('token失效重新获取')
            get_token(acc, pwd)
            with open('a.ini', 'r', encoding='utf-8') as f:
                self.token = f.readline().rstrip()
                self.name = f.readline().rstrip()
                self.uid = f.readline().rstrip()


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
        res = a.get_info(id, self.token, self.uid).json()
        # activityName = res['data']['activityName']   #活动名称
        # address = res['data']['address']   #活动地址
        # joindate = res['data']['joindate']  #报名时间
        # startdate = res['data']['startdate']  #活动时间
        # name = res['data']['specialList'][0]['name']  #积分类型
        # unitcount = res['data']['specialList'][0]['unitcount']  #积分数量

        app1 = tk.Toplevel(app)
        app1.geometry('643x360')
        app1.title(res['data']['activityName'])





def login():
    main = Main()
    main.login()
    main.get_id()



def chiken():
    main = Main()
    main.login()
    main.chiken()

b = tk.Button(app, text='登录', font=('Arial', 12), width=10, height=1, command=login)
b.pack()
b.place(x=380, y=12.5)

b1 = tk.Button(app, text='活动信息查询', font=('Arial', 12), width=10, height=1, command=chiken)
b1.pack()
b1.place(x=720, y=0)

b1 = tk.Button(app, text='报名活动', font=('Arial', 12), width=10, height=1, command=login)
b1.pack()
b1.place(x=720, y=32)


app.mainloop()
