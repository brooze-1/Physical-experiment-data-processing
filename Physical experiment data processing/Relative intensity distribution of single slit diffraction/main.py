import matplotlib.pyplot as plt
from pylab import *
import csv
class Single(object):
    def __init__(self,X_lst,I_lst,Io=6.82,D=0.765,y=6.328e-7,Xo=0.040422):
        # 单缝到光电探头的距离D = 0.765(m)
        self.D = D
        # 入射光波长 y = 632.8(nm)
        self.y = y
        # 中央明纹位置坐标为 Xo = 40.422(mm)
        self.Xo = Xo
        # 位置坐标（list）[-2,-1,1,2]
        self.X_lst = X_lst
        # 光强(list) [-2,-1,1,2]
        self.I_lst = I_lst
        # 中央明纹光强最大值对应的电流值
        self.Io = Io

    # 计算△Xk = Xk - Xo
    def cal_Xk_Xo(self):
        # self.Xk_Xo(list)用于存储△Xk = Xk - Xo
        self.Xk_Xo = []
        for Xk in self.X_lst:
            self.Xk_Xo.append(round(abs(Xk-self.Xo),7))
        print(f"Xk-Xo:{self.Xk_Xo}")

    # 计算a = |k|*y*D/△Xk   单位为：m
    def cal_a(self):
        self.a_lst = []
        a1 = (2*self.y*self.D)/self.Xk_Xo[0]
        a2 = (1*self.y*self.D)/self.Xk_Xo[1]
        a3 = (1*self.y*self.D)/self.Xk_Xo[2]
        a4 = (2*self.y*self.D)/self.Xk_Xo[3]
        self.a_lst.extend([round(a1,7),round(a2,7),round(a3,7),round(a4,7)])
        print(f"a:{self.a_lst}")


    # 计算缝宽a的平均值
    def cal_avg_a(self):
        avg_a = sum(self.a_lst)/len(self.a_lst)
        return round(avg_a,7)

    # 计算标准差
    def cal_std(self):
        avg_a = self.cal_avg_a()
        sum_num = 0
        for a in self.a_lst:
            sum_num += (a-avg_a)**2
        self.std_r = (sum_num/(len(self.a_lst)-1))**0.5
        # self.std_r = round(self.std_r,6)

    # 输出a的缝宽
    def output(self):
        avg_a = self.cal_avg_a()
        self.res = str(avg_a) + '±' + str(self.std_r)
        print(f"缝宽a的平均值为{avg_a}")
        print(f"缝宽a的标准差为{self.std_r}")
        print(f"缝宽的最终值为{self.res}")

    # 计算相对强度I/Io
    def I_Io(self):
        self.rel_I = []
        for I in self.I_lst:
            self.rel_I.append(round(I/self.Io,5))
        print(f"相对光强I/Io:{self.rel_I}")

    def main(self):
        self.cal_Xk_Xo()
        self.cal_a()
        self.cal_std()
        self.I_Io()
        self.output()


class Draw_img(object):
    def __init__(self,filename='data.csv'):
        self.filename = filename
        self.temp_lst = []
        with open(filename,'r') as f:
            reader = csv.reader(f)
            for row in reader:
                self.temp_lst.append(row)
        # print(self.temp_lst)
        # 18组坐标位置存放在self.X_lst中 单位（mm）
        self.X_lst = self.temp_lst[0]
        # 删除列表文本字段
        del self.X_lst[0]
        # 18组光强I存放在self.I_lst中 单位（10e-7A）
        self.I_lst = self.temp_lst[1]
        # 删除列表中的文本字段
        del self.I_lst[0]
        # 18组相对光强存放在self.I_Io中
        self.I_Io = ['相对光强I/Io']
        # 光强最大值 单位（10e-7A）
        self.I_max = 6.82
        self.f = open(filename,'a',encoding='gbk',newline='')
        self.writer = csv.writer(self.f)
        # 中央明纹的位置  单位（mm）
        self.X = 40.422
        # 18组数据到中央明纹的距离存放在self.x_len中 单位（mm）
        self.x_len = ['到中央明纹的距离']

    # 计算18组数据的相对光强
    def cal_I_Io_lst(self):
        for I in self.I_lst:
            self.I_Io.append(round(float(I) / self.I_max,5))
        # 将18组数据的相对光强写入data文件
        # self.writer.writerow(self.I_Io)
        print(self.I_Io)

    # 计算18组数据的相对中央明纹的距离
    def cal_len(self):
        for x in self.X_lst:
            self.x_len.append(round(float(x)-self.X,7))
        print(self.x_len)
        # 将18组数据的相对中央明纹的距离写入data文件
        # self.writer.writerow(self.x_len)

    # 画光强与距离的曲线
    def draw(self):
        # 删除列表文本字段
        del self.x_len[0]
        del self.I_Io[0]
        # xticks(np.linspace(-6,6,50,endpoint=True))
        # yticks(np.linspace(0,1,50,endpoint=True))
        plt.grid(axis='y',linestyle='-.',linewidth=1)
        plt.grid(axis='x',linestyle='-.',linewidth=1)
        plt.plot(self.x_len,self.I_Io,color='red')
        # plt.axes().get_xaxis().set_visible(False)  # 隐藏x坐标轴
        # plt.axes().get_yaxis().set_visible(False)  # 隐藏y坐标轴
        plt.savefig('test.png')
        plt.show()



    def main(self):
        self.cal_I_Io_lst()
        self.cal_len()
        self.f.close()
        self.draw()


if __name__ == "__main__":
    # X_lst = [0.046202,0.043681,0.038192,0.036272] # 单位为（m）
    # I_lst = [0.04,0.07,0.10,0.04] # 单位为（A）
    # obj = Single(X_lst=X_lst,I_lst=I_lst)
    # obj.main()
    obj2 = Draw_img()
    obj2.main()

