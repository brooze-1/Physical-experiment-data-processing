#开发时间：2021/3/17  21:10
#自由落体法测量加速度
#限制条件输入的数据个数必须是>=8，并且为4的倍数
data=input('输入的数据请用空格分开:')
#data输入格式：距离间隔 时间平均值（例：100 44.9）
i=1
#将数据以列表形式存储到字典当中例：{0:[100,44.9]}}
d={}
data_2=[]
while data:
    data_2=[]
    #将列表中的数字转化成浮点型，存储在data_2中
    data=data.split(' ')
    #将字符串数据转化为列表存储到data列表中（说明split()只能应用于字符串）
    for j in data:
        data_2.append(float(j))
    d[i]=data_2          #字典的键值可以为整型
    i+=1
    data = input('输入的数据请用空格分开:')
G=[]
#G用于存储每次算出的g
for n in range(1,5):
    neutral=((d[n+4][0]/d[n+4][1])-(d[n][0]/d[n][1]))*2
    g1=neutral/(d[n+4][1]-d[n][1])
    g1=1000*g1
    G.append(g1)
s=0
for u in G:
   print('g每次测量值:{:<.4f}'.format(u))
   #输出每次g的测量值
   s+=u
g=s/len(G)
#算平均重力加速度
print("测得重力加速度为：{:<.4f}米每二次方秒".format(g))
gn=9.7920
E=abs((g-gn)/gn)*100
print('相对误差为：{:<.4f}%'.format(E))



