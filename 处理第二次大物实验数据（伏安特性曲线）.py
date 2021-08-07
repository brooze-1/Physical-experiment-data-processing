# 开发时间：2021/3/27  20:10
'''
待测电阻为10欧姆，电流表内接（电流表内阻RA=1欧姆）
电流值：27.07 24.83 22.94 21.31
电压值：0.2961 0.2717 0.2509 0.2331
待测电阻为10k欧姆，电流表内接（电流表内阻RA=100欧姆）
电流值：0.2973 0.2703 0.2477 0.2287
电压值：3.004 2.732 2.504 2.311
待测电阻为10欧姆，电流表外接（电压表内阻RV=10000000欧姆）
电流值：27.07 24.83 22.94 21.31
电压值：0.2667 0.2447 0.2260 0.2099
待测电阻为10k欧姆，电流表外接（电压表内阻RV=1000000欧姆）
电流值：0.3002 0.2729 0.2502 0.2310
电压值：2.974 2.704 2.479 2.288
'''

#将数据导入电流电压数据导入csv文件中，利用excel将数据形成表格
f=open('处理第二次大物实验数据（伏安特性曲线）.csv','w')
data_list=[' 待测电阻为10欧姆，电流表内接（电流表内阻RA=1欧姆） ','电流值： 27.07 24.83 22.94 21.31','电压值： 0.2961 0.2717 0.2509 0.2331',
           ' 待测电阻为10k欧姆，电流表内接（电流表内阻RA=100欧姆） ','电流值： 0.2973 0.2703 0.2477 0.2287','电压值： 3.004 2.732 2.504 2.311'
           ,' 待测电阻为10欧姆，电流表外接（电压表内阻RV=10000000欧姆） ','电流值： 27.07 24.83 22.94 21.31','电压值： 0.2667 0.2447 0.2260 0.2099',
           ' 待测电阻为10k欧姆，电流表外接（电压表内阻RV=1000000欧姆） ','电流值： 0.3002 0.2729 0.2502 0.2310','电压值： 2.974 2.704 2.479 2.288']
for line in data_list:
    line.split(' ')
    ','.join(line)
    f.write(line+'\n')
f.close()


I=input("请输入电流表读数（单位为mA）输入数据时请用空格隔开：")
U=input("请输入电压表读数（单位为V）输入数据时请用空格隔开:")
U_max=eval(input("请输入电压表量程（单位为V）："))
I_max=eval(input('请输入电流表量程（单位为mA）：'))
#I_list用来存放电流数据
#U_list用来存放电压数据
I_list=I.split(' ')    #千万要注意split()方法只能用于字符串数据
U_list=U.split(' ')
#R_list用来存放每次没修正的电阻值
R_list=[]
sum=0
for i in range(len(I_list)):
    #(float(U_list[i]))/(float(I_list[i])/1000)用来计算每次电阻值，将其赋值给R
    R=(float(U_list[i]))/(float(I_list[i])/1000)
    R_list.append(format(R,'.3f'))
    sum+=R
#average用来存储电阻平均值
average=sum/len(I_list)
insert=input('请输入电流表接入电路的方式（外接或内接）：')
if insert=='内接':
    RA=int(input('请输入电流表内阻（单位为欧姆）：'))
elif insert=='外接':
    RV=int(input('请输入电压表内阻（单位为欧姆）：'))
#判断insert输入
else:
    print("请重新运行程序，并输入正确的电流表接入方式！！！")
#将修正后的电阻值放进R_
R_=[]
for i in range(len(I_list)):
    print("第{}次计算电阻值为{:<.4f}".format(i+1,float(R_list[i])))
    if insert=='内接':
        #利用公式R修正=U/I-RA，计算内接时R修正=R_list[i])-RA
        print("第{}次计算修正后电阻值为{:<.4f}".format(i+1,float(R_list[i])-RA))
        R_.append(float(R_list[i])-RA)
    if insert=='外接':
        #计算分母bottom
        bottom=(float(I_list[i])/1000)-(float(U_list[i])/RV)
        #利用公式R修正=[U/(I-U/RV)],计算外接时R修正=U_list[i])/bottom
        print("第{}次计算修正后电阻值为{:<.4f}".format(i+1,float(U_list[i])/bottom))
        #将每次计算的修改值存储至R_中
        R_.append(float(U_list[i])/bottom)
#sum_R是修改值的总和
sumR_=0
for i in R_:
    sumR_+=i

#将U_list中的字符串转化成浮点数储存在new_float_U中，方便取出电压最大值
new_float_U=[]
for i in U_list:
    new_float_U.append(format(float(i),'.3f'))

#将I_k=list中的字符串转化为浮点数储存在new_float_I中，方便取出电流最大值
new_float_I=[]
for i in I_list:
    new_float_I.append(format(float(i),'.4f'))

#计算⊿R/R，即⊿R/R=(float(u_max)*k/float(u_min))+(float(i_max)*k/float(i_min))
k=0.015
u_max=max(new_float_U)
u_min=min(new_float_U)
i_max=max(new_float_I)
i_min=min(new_float_I)
data=(U_max*k/float(u_min))+((I_max/1000)*k/float(i_min))
u_error=k*U_max
i_error=k*I_max/1000
#输出结果
print('电压表仪器误差为：{:<.4f}'.format(u_error))
print('电流表仪器误差为：{:<.4f}'.format(i_error))
print('平均电阻为：',format(average,'.4f'))
print('修正后的平均电阻为：',format(sumR_/len(R_),'.4f'))
print('⊿R/R的值为：{:<.1f}%'.format(data*100))
print('平均电阻-(减去)修正后的平均电阻的值为：',format(average-sumR_/len(R_),'.3f'))




