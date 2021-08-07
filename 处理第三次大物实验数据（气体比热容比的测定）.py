# 开发时间：2021/3/29  21:22
#振动50次周期总时间t)(单位：s)：29.308 29.317 29.318 29.333 29.323
#周期T(单位：s):0.58616 0.58634 0.58636 0.58666 0.58646
#小球直径d(单位：mm)：13.955 13.985 13.965 13.995 13.975
#小球的质量(单位：g)：11.1
#储气瓶的体积（单位：ml）：2650
#标准大气压(单位Pa)P=1.013e5
#m=eval(input('请输入小球的质量（单位kg）'))
import math
m=1.11e-2
#V=eval(input('请输入储气瓶的容积（单位为m³）'))
V=2.65e-3
#P=eval(input('请输入本地大气压（单位为Pa）'))
P=1.013e5
t=input('请输入振动50次周期总时间（多个数据输入请用空格分开）(单位为s)：')
#T=input('请输入周期（多个数据输入请用空格分开）（单位为s）：')
d=input('请输入钢球直径测量数据（多个数据输入请用空格分开）(单位为mm)：')
t_list_str=t.split()
#T_list_str=T.split(' ')
d_list_str=d.split(' ')



#利用振动50次周期总时间来计算周期，用T_list来存储计算的周期
T_list=[]
for i in t_list_str:
    T_list.append("{:<.5f}".format(float(i)/50))
print(T_list)



#计算周期的方差
sum_T=0
for i in T_list:
    sum_T+=float(i)
#average_T为周期的平均值
average_T=sum_T/len(T_list)
su=0
for j in T_list:
    su+=pow((float(j)-average_T),2)
#variance_T为周期标准方差
variance_T=pow(su/(len(T_list)-1),0.5)



#计算直径的方差
sum_d=0
for i in d_list_str:
    sum_d+=float(i)
#average_d为直径的平均值
average_d=sum_d/len(d_list_str)
sum=0    #sum的单位为mm
sum2=0   #sum2的单位为m
for j in d_list_str:
    sum+=pow((float(j)-average_d),2)
    sum2+=pow((float(j)-average_d)/1000,2)
#variance_d_mm(单位为mm)为直径标准方差
#variance_d_m(单位为m)为直径标准方差
variance_d_mm=pow(sum/(len(d_list_str)-1),0.5)
variance_d_m=pow(sum2/(len(d_list_str)-1),0.5)



#计算压强
P_change=m*10/(3.14*((average_d/1000/2)**2))
Pl=P+P_change
print("{:<.1f}".format(P_change))
#Pl_为代码运行后对Pl的有效位进行保留
Pl_=102024


#计算气体比热容比
bottom=pow(average_T,2)*pow(average_d/1000,4)*Pl_
#其中P为近似值，约等于标准大气压
#r为气体比热容比的值
r=(64*m*V)/bottom



#计算气体比热容比的标准方差
#r_T_weight为气体比热容比中的关于T的分量
#r_d_weight为气体比热容比中的关于d的分量
#r_P_weight为气体比热容比中的关于P的分量
r_T_weight=pow((2*variance_T/average_T),2)
r_d_weight=pow((4*variance_d_m/average_d),4)
#r_P_weight=pow()
#此处r_P_weight取P标准大气压为
variance_r=pow(r_T_weight+r_d_weight,0.5)


print('瓶内的平均气压为(单位为Pa)：{:<.1f}'.format(Pl))
print('平均周期为(单位为s)：{:<.5f}'.format(average_T))
print('平均直径为(单位为mm)：{:<.3f}'.format(average_d))
print('周期(单位为s)结果表示T={:<.5f}±{:<.5f}'.format(average_T,variance_T))
print('直径(单位为mm)结果表示d={:<.3f}±{:<.5f}'.format(average_d,variance_d_mm))
print('比热容比结果表示r={:<.4f}±{:<.3f}'.format(r,variance_r))