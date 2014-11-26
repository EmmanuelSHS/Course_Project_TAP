# -*- coding: cp936 -*-
from Tkinter import *
from tkMessageBox import *
from time import sleep

class Interone:
    def __init__(self,CPCal,root):
        # 根窗口大小、名称设置
        self.root = root
        self.phac = CPCal
        self.root.title('Fe-C Phase Diagram Calculator')
        self.root.geometry('539x550')
        self.root.resizable(False,False) #禁用最大化

        self.fra_l = StringVar() # 左边相名称
        self.fra_l.set('Left Phase')
        self.fra_r = StringVar() # 右边相名称
        self.fra_r.set('Right Phase')
        self.amt_fra_l = StringVar() # 左边相相对比例
        self.amt_fra_l.set('0.00')
        self.amt_fra_r = StringVar() # 右边相相对比例
        self.amt_fra_r.set('0.00')
        
        # 导入相图
        self.c = Canvas(self.root,width=539,height=423,bg='white')
        self.pd = PhotoImage(file = 'FeC.gif')
        self.c.create_image(0,0,image=self.pd,anchor=NW)
        self.c.bind('<Button-1>',self.disCtl) # 左键点击，触发显示控制函数
        self.c.place(x=0,y=0,anchor=NW)
        
        # 控件布局
        Label(self.root,textvariable=self.fra_l).place(x=10,y=435,anchor=NW)
        Label(self.root,textvariable=self.fra_r).place(x=270,y=435,anchor=NW)
        Entry(self.root,textvariable=self.amt_fra_l).place(x=110,y=435,anchor=NW)
        Entry(self.root,textvariable=self.amt_fra_r).place(x=370,y=435,anchor=NW)
        self.quit = Button(self.root,text='Quit',command=self.close) # 退出指令
        self.quit.place(x=320,y=500,anchor=NW)
        self.ref = Button(self.root,text='Refresh',command=self.refresh) # 刷新屏幕指令
        self.ref.place(x=220,y=500,anchor=NE)

        self.root.mainloop()

    def disCtl(self,event):
        fl,fr,acl,acr,p = self.phac.judgePoint(event.x,event.y) # 从CPCal类得到鼠标点击点所在的相区信息：左相名称，右相名称，左相界坐标，右相界坐标、所处相区
        # 图像上创建选中点
        self.c.create_text(event.x,event.y,text='Selected Point',anchor=S)
        self.c.create_rectangle(event.x-1,event.y-1,event.x+1,event.y+1,fill='black')
        
        self.showName(fl,fr) # 将相名称显示出来
        if fl == 'None': # 异常处理
            self.showC(0,0)
            self.PAErrorInfo() #Phase Area选取报错
        else: # 一般情况
            afl,afr = self.phac.run(event.x,acl,acr,p) # 使用CPCal run函数，得到左相百分百，右相百分百
            self.showC(afl,afr) # 显示成分数值
            if fr == 'None':
                self.RTErrorInfo() # Runtime 报错
            else:
                self.SwitchButton()
                self.showLLine(int(event.x),int(event.y),int(acl))
                self.showRLine(int(event.x),int(event.y),int(acr))
                self.SwitchButton()
                
    def showLLine(self,x0,y0,xfl):
        x = x0
        while x <> xfl:
            HL = self.c.create_line(x0,y0,x,y0,fill='red')
            x += -1
            self.c.update()
            sleep(0.005)

    def showRLine(self,x0,y0,xfr):
        x = x0 
        while x <> xfr:
            HL = self.c.create_line(x0,y0,x,y0,fill='blue')
            x += 1
            self.c.update()
            sleep(0.005)

    def showName(self,fl,fr):
        self.fra_l.set(fl)
        self.fra_r.set(fr)

    def showC(self,afl,afr):
        self.amt_fra_l.set(format(afl,'.2%')) # 格式化输出为百分比，保留两位小数
        self.amt_fra_r.set(format(afr,'.2%'))

    def SwitchButton(self): #为了防止在画水平线时退出而产生报错，在这段时间禁用按钮
        if self.ref['state'] == 'normal':
            self.ref['state']='disabled' 
            self.quit['state']='disabled'
        else:
            self.ref['state']='normal'
            self.quit['state']='normal'

    def PAErrorInfo(self): # Phase Area Error: 点击位置不在相区内报错
        showinfo('Error','Please click in the phase area!') # 弹出异常窗口

    def RTErrorInfo(self): # 点击位置不在两相区内报错
        showinfo('Error','Please click in the two-phases zone!')

    def refresh(self):
        self.c.create_image(0,0,image=self.pd,anchor=NW)

    def close(self):
        self.root.quit()
        self.root.destroy()
        
