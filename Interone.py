# -*- coding: cp936 -*-
from Tkinter import *
from tkMessageBox import *
from time import sleep

class Interone:
    def __init__(self,CPCal,root):
        # �����ڴ�С����������
        self.root = root
        self.phac = CPCal
        self.root.title('Fe-C Phase Diagram Calculator')
        self.root.geometry('539x550')
        self.root.resizable(False,False) #�������

        self.fra_l = StringVar() # ���������
        self.fra_l.set('Left Phase')
        self.fra_r = StringVar() # �ұ�������
        self.fra_r.set('Right Phase')
        self.amt_fra_l = StringVar() # �������Ա���
        self.amt_fra_l.set('0.00')
        self.amt_fra_r = StringVar() # �ұ�����Ա���
        self.amt_fra_r.set('0.00')
        
        # ������ͼ
        self.c = Canvas(self.root,width=539,height=423,bg='white')
        self.pd = PhotoImage(file = 'FeC.gif')
        self.c.create_image(0,0,image=self.pd,anchor=NW)
        self.c.bind('<Button-1>',self.disCtl) # ��������������ʾ���ƺ���
        self.c.place(x=0,y=0,anchor=NW)
        
        # �ؼ�����
        Label(self.root,textvariable=self.fra_l).place(x=10,y=435,anchor=NW)
        Label(self.root,textvariable=self.fra_r).place(x=270,y=435,anchor=NW)
        Entry(self.root,textvariable=self.amt_fra_l).place(x=110,y=435,anchor=NW)
        Entry(self.root,textvariable=self.amt_fra_r).place(x=370,y=435,anchor=NW)
        self.quit = Button(self.root,text='Quit',command=self.close) # �˳�ָ��
        self.quit.place(x=320,y=500,anchor=NW)
        self.ref = Button(self.root,text='Refresh',command=self.refresh) # ˢ����Ļָ��
        self.ref.place(x=220,y=500,anchor=NE)

        self.root.mainloop()

    def disCtl(self,event):
        fl,fr,acl,acr,p = self.phac.judgePoint(event.x,event.y) # ��CPCal��õ�����������ڵ�������Ϣ���������ƣ��������ƣ���������꣬��������ꡢ��������
        # ͼ���ϴ���ѡ�е�
        self.c.create_text(event.x,event.y,text='Selected Point',anchor=S)
        self.c.create_rectangle(event.x-1,event.y-1,event.x+1,event.y+1,fill='black')
        
        self.showName(fl,fr) # ����������ʾ����
        if fl == 'None': # �쳣����
            self.showC(0,0)
            self.PAErrorInfo() #Phase Areaѡȡ����
        else: # һ�����
            afl,afr = self.phac.run(event.x,acl,acr,p) # ʹ��CPCal run�������õ�����ٷְ٣�����ٷְ�
            self.showC(afl,afr) # ��ʾ�ɷ���ֵ
            if fr == 'None':
                self.RTErrorInfo() # Runtime ����
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
        self.amt_fra_l.set(format(afl,'.2%')) # ��ʽ�����Ϊ�ٷֱȣ�������λС��
        self.amt_fra_r.set(format(afr,'.2%'))

    def SwitchButton(self): #Ϊ�˷�ֹ�ڻ�ˮƽ��ʱ�˳����������������ʱ����ð�ť
        if self.ref['state'] == 'normal':
            self.ref['state']='disabled' 
            self.quit['state']='disabled'
        else:
            self.ref['state']='normal'
            self.quit['state']='normal'

    def PAErrorInfo(self): # Phase Area Error: ���λ�ò��������ڱ���
        showinfo('Error','Please click in the phase area!') # �����쳣����

    def RTErrorInfo(self): # ���λ�ò����������ڱ���
        showinfo('Error','Please click in the two-phases zone!')

    def refresh(self):
        self.c.create_image(0,0,image=self.pd,anchor=NW)

    def close(self):
        self.root.quit()
        self.root.destroy()
        
