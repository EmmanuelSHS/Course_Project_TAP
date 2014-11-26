# -*- coding: cp936 -*-
from Tkinter import *
from tkMessageBox import *

class Intertwo:
    def __init__(self,CPCal,root):
        # 接口
        self.phac = CPCal
        
        # 创建根窗口
        self.root = root
        self.root.title('Customized Phase Calculator')
        self.root.resizable(False,False)

        # 名称标签初始化
        self.comp_p = StringVar() # 自己输入的组分
        self.comp_p.set('Overall Composition(which your want to calculate(%))')
        self.comp_l = StringVar() # 左边相名称
        self.comp_l.set('Equilibrium Left Composition(Left Point)(%)')
        self.comp_r = StringVar()
        self.comp_r.set('Equilibrium Right Composition(Right Point)(%)')
        self.fra_l = StringVar() # 左边相比例
        self.fra_l.set('Left Phase Fraction')
        self.fra_r = StringVar() # 右边相比例
        self.fra_r.set('Right Phase Fraction')

        # 数值标签的初始化
        self.amt_comp_p = StringVar()
        self.amt_comp_p.set('0.00')
        self.amt_comp_l = StringVar() #左边相成分输入
        self.amt_comp_l.set('0.00')
        self.amt_comp_r = StringVar()
        self.amt_comp_r.set('0.00')
        self.amt_fra_l = StringVar()
        self.amt_fra_l.set('0.00')
        self.amt_fra_r = StringVar()
        self.amt_fra_r.set('0.00')

        # 控件布局
        Label(self.root,textvariable=self.comp_p).grid(row=2,column=0,sticky=W)
        Label(self.root,textvariable=self.comp_l).grid(row=0,column=0,sticky=W)
        Label(self.root,textvariable=self.comp_r).grid(row=1,column=0,sticky=W)
        Label(self.root,textvariable=self.fra_l).grid(row=0,column=2,sticky=W)
        Label(self.root,textvariable=self.fra_r).grid(row=1,column=2,sticky=W)
        Entry(self.root,textvariable=self.amt_comp_l).grid(row=0,column=1,sticky=W)
        Entry(self.root,textvariable=self.amt_comp_r).grid(row=1,column=1,sticky=W)
        Entry(self.root,textvariable=self.amt_comp_p).grid(row=2,column=1,sticky=W)
        Entry(self.root,textvariable=self.amt_fra_l).grid(row=0,column=3,sticky=W)
        Entry(self.root,textvariable=self.amt_fra_r).grid(row=1,column=3,sticky=W)

        self.ok = Button(self.root,text='OK',command=self.disCtl) # 点击ok，触发显示控制函数
        self.ok.grid(row=2,column=2,sticky=E)
        self.quit = Button(self.root,text='Quit',command=self.close)
        self.quit.grid(row=2,column=3,sticky=W)
        
        self.root.mainloop()
        
    def disCtl(self): # 非实例变量，全部使用对应实例变量的简写
        acp = eval(self.amt_comp_p.get())
        acl = eval(self.amt_comp_l.get())
        acr = eval(self.amt_comp_r.get())
        if (int(acl) == 0 and int(acr) == 0) == True:
            self.CErrorInfo()
        elif (acp < acl or acp > acr or acl > acr) == True:
            self.AErrorInfo()
        else:
            afl,afr = self.phac.run(acp,acl,acr,2)
            self.showF(afl,afr)

    def showF(self,afl,afr):
        self.amt_fra_l.set(format(afl,'.2%'))
        self.amt_fra_r.set(format(afr,'.2%'))

    def CErrorInfo(self):
        showinfo('Error','Composition can\'t be both zero on the same time!') # 弹出异常窗口

    def AErrorInfo(self):
        showinfo('Error','Please put the composition in right order (left<overall<right)')
        
    def close(self):
        self.root.quit()
        self.root.destroy()        
