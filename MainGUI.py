# -*- coding: cp936 -*-
from Tkinter import *
from tkMessageBox import *
from Interone import *
from Intertwo import *

class MainGUI:
    def __init__(self,phac):
        # 接口
        self.cp = phac

        # 初始化窗口
        self.root = Tk()
        self.root.title('Phase Diagram Calculator')
        self.root.resizable(False,False) #禁用最大化
        self.bg = PhotoImage(file = 'BG.gif')
        self.c = Canvas()
        self.c.create_image(0,0,image=self.bg,anchor=NW)
        self.c.pack()

        # 初始化菜单栏
        self.m = Menu(self.root)
        self.root.config(menu=self.m)
        self.filemenu = Menu(self.m)
        self.m.add_cascade(label='File',menu=self.filemenu)
        self.filemenu.add_command(label='Exit',command=self.close)
        self.helpmenu = Menu(self.m)
        self.m.add_cascade(label='Help',menu=self.helpmenu)
        self.helpmenu.add_command(label='Guide',command=self.guide)
        self.helpmenu.add_command(label='About',command=self.about)

        # 初始化两种计算模式按钮
        self.mode_one_button = Button(self.root,text='Fe-C Phase Diagram Calculator',command=self.mode_one)
        self.mode_one_button.pack()
        self.mode_two_button = Button(self.root,text='Customized Calculator(Enter Your Own Composition)',command=self.mode_two)
        self.mode_two_button.pack()

        # 初始化其他内容
        self.quit_button = Button(self.root,text='Quit',command=self.close)
        self.quit_button.pack()
        self.root.mainloop()

    def mode_one(self): # 图像计算模式
        self.top_one = Toplevel()
        m = Interone(self.cp,self.top_one)

    def mode_two(self): # 自定义计算模式
        self.top_two = Toplevel()
        m = Intertwo(self.cp,self.top_two)

    def guide(self):
        self.top_g = Toplevel()
        self.top_g.title('User Guide')
        self.top_g.geometry('860x500')
        self.top_g.resizable(False,False)
        # 布局，将画布和滚动条捆绑
        self.scrollbar = Scrollbar(self.top_g)
        self.scrollbar.pack(side=RIGHT,fill=Y)
        self.ca = Canvas(self.top_g,height=500,width=889,scrollregion=(0,0,889,2485),yscrollcommand=self.scrollbar.set)
        self.ug = PhotoImage(file='UG.gif')
        self.ca.create_image(0,0,image=self.ug,anchor=NW)
        self.ca.pack(expand=True,fill=BOTH)
        self.scrollbar.config(command=self.ca.yview)
           
    def about(self):
        self.top_a = Toplevel()
        Label(self.top_a,text='Phase Diagram Calculator').pack()
        Label(self.top_a,text='version 2.1').pack()
        Label(self.top_a,text='Author: Wang Mengqi').pack()
        Label(self.top_a,text='Date: 2013.12.26').pack()

    def close(self):
        self.root.quit()
        self.root.destroy()
