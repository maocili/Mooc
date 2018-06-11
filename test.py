import os
import Login
from time import sleep
from tkinter import *
class DirList(object):
    def __init__(self, initdir=None):
        self.top = Tk()
        self.label = Label(self.top,text='Directory Lister v1.2')
        self.label1 = Label(self.top,text='账号')
        self.textbox1 = Text(self.top, width=80, height=1)
        self.label2 = Label(self.top, text='密码')
        self.textbox2 = Text(self.top, width=80, height=1)
        self.button = Button(self.top,text='开始刷题',command=self.login)
        self.label.pack()
        self.label1.pack()
        self.textbox1.pack()
        self.label2.pack()
        self.textbox2.pack()
        self.button.pack()

    def login(self,ev=None):
        print(self.textbox1.get(0))
        # Login.requests_interface.login()
        # Login.requests_interface.start('xxdgaeiojkdp4a39rqtp1q')


def main():
    d = DirList(os.curdir)
    mainloop()

if __name__ == '__main__':
    main()
