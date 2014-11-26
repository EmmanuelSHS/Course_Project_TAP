# -*- coding: cp936 -*-

class CPCal:
    def judgePoint(self,x0,y0): #根据用户选择的点，判断出水平连接线与相界的交点坐标，并返回数据
        bl = 85 # 左边界坐标
        br = 485 # 右边界坐标
        #预设位置是位于单相区，此时的值应用到初始化中
        fl = 'None'
        fr = 'None'
        acl = x0
        acr = y0
        p = 1
        #根据y坐标判断进行分区判断，之后再根据x进一步细分判断
        if 20<y0<37:
             fl = 'Liquid'
        elif 37<=y0<57:
             x1 = bl
             x2 = 66.5+0.5*y0
             x3 = -239.74578+15.34557*y0-0.21474*y0**2+0.00101*y0**3
             x4 = br
             if x1<=x0<x2:
                 fl = 'delta-Fe'
             elif x2<=x0<x3:
                 fl = 'delta-Fe'
                 fr = 'Liquid'
                 acl = x2
                 acr = x3
                 p = 2
             elif x3<=x0<=x4:
                 fl = 'Liquid'
        elif 57<=y0<90:
             x1 = bl
             x2 = 112.27273-0.30303*y0
             x3 = 139.54545-0.60606*y0
             x4 = 53.31356+0.90678*y0
             x5 = -152.88294+6.66279*y0-0.03574*y0**2+0.0000795184*y0**3
             x6 = br
             if x1<=x0<x2:
                 fl = 'delta-Fe'
             elif x2<=x0<x3:
                 fl = 'delta-Fe'
                 fr = 'gama-Fe'
                 acl = x2
                 acr = x3
                 p = 2
             elif x3<=x0<x4:
                 fl = 'gama-Fe'
             elif x4<=x0<x5:
                 fl = 'gama-Fe'
                 fr = 'Liquid'
                 acl = x4
                 acr = x5
                 p = 2
             elif x5<=x0<=x6:
                 fl = 'Liquid'
        elif 90<=y0<148:
             x1 = bl
             x2 = 53.31356+0.90678*y0
             x3 = -152.88294+6.66279*y0-0.03574*y0**2+0.0000795184*y0**3
             x4 = br
             if x1<=x0<x2:
                 fl = 'gama-Fe'
             elif x2<=x0<x3:
                 fl = 'gama-Fe'
                 fr = 'Liquid'
                 acl = x2
                 acr = x3
                 p = 2
             elif x3<=x0<=x4:
                 fl = 'Liquid'
        elif 148<=y0<175:
             x1 = bl
             x2 = 53.31356+0.90678*y0
             x3 = -152.88294+6.66279*y0-0.03574*y0**2+0.0000795184*y0**3
             x4 = 25166.02457-434.66145*y0+2.559*y0**2-0.00506*y0**3
             x5 = br
             if x1<=x0<x2:
                 fl = 'gama-Fe'
             elif x2<=x0<x3:
                 fl = 'gama-Fe'
                 fr = 'Liquid'
                 acl = x2
                 acr = x3
                 p = 2
             elif x3<=x0<x4:
                 fl = 'Liquid'
             elif x4<=x0<=x5:
                 fl = 'Liquid'
                 fr = 'Fe3C'
                 acl = x4
                 acr = x5
                 p = 2
        elif 175<=y0<265:
             x1 = bl
             x2 = 335.28179-0.63668*y0-0.000827988*y0**2+0.00000259519*y0**3
             x3 = br
             if x1<=x0<x2:
                 fl = 'gama-Fe'
             elif x2<=x0<x3:
                 fl = 'gama-Fe'
                 fr = 'Fe3C'
                 acl = x2
                 acr = x3
                 p = 2
        elif 265<=y0<320:
             x1 = bl
             x2 = -2156.57891+22.19973*y0-0.07354*y0**2+0.0000818667*y0**3
             x3 = -2701.30428+27.39848*y0-0.09125*y0**2+0.000104056*y0**3
             x4 = 335.28179-0.63668*y0-0.000827988*y0**2+0.00000259519*y0**3
             x5 = br
             if x1<=x0<x2:
                 fl = 'alpha-Fe'
             elif x2<=x0<x3:
                 fl = 'alpha-Fe'
                 fr = 'gama-Fe'
                 acl = x2
                 acr = x3
                 p = 2
             elif x3<=x0<x4:
                 fl = 'gama-Fe'
             elif x4<=x0<=x5:
                 fl = 'gama-Fe'
                 fr = 'Fe3C'
                 acl = x4
                 acr = x5
                 p = 2
        elif 320<=y0<366:
             x1 = bl
             x2 = 196.3913-0.30435*y0
             x3 = br
             if x1<=x0<x2:
                 fl = 'alpha-Fe'
             elif x2<=x0<x3:
                 fl = 'alpha-Fe'
                 fr = 'Fe3C'
                 acl = x2
                 acr = x3
                 p = 2
          
        return fl,fr,acl,acr,p

    def run(self,x0,acl,acr,p): #计算相成分比例，并传递结果
        if p == 1:#求相对成分比例，特例：处于单相区
            afl = 1
            afr = 0 
        else:#一般情况的求法
            afl = float(acr - x0)/float(acr - acl)
            afr = float(x0 - acl)/float(acr - acl)
        return afl,afr

        
