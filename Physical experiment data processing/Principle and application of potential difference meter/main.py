# 电位差计的原理和使用

# from matplotlib import pyplot as plt
from matplotlib import font_manager
from random import *
# import random
import pylab as plt
from pylab import *
class Use(object):
    def __init__(self,Ux1,Ux2,Is):
        # self.Ux1存储第一组数据的电压值（list）
        self.Ux1 = Ux1
        # self.Ux2存储第二组数据的电压值(list)
        self.Ux2 = Ux2
        # self.Is存储实验电流值(list)
        self.Is = Is
        # Rb等于1欧姆(int)
        self.Rb = 1



    def cal_Ix1(self,Ux):
        """
        计算第一组数据的Ix(list)
        :param Ux:
        :return:
        """
        self.Ix1 = []
        for U in Ux:
            self.Ix1.append(U/self.Rb)
        print(f"Ix1:{self.Ix1}")

    def cal_Ix2(self,Ux):
        """
        计算第二组数据的Ix(list)
        :param Ux:
        :return:
        """
        self.Ix2 = []
        for U in Ux:
            self.Ix2.append(U/self.Rb)
        print(f"Ix2:{self.Ix2}")

    def cal_Ix(self):
        """
        计算平均电流Ix(list)
        :return:
        """
        self.Ix = []
        for i in range(8):
            self.Ix.append(round((self.Ix1[i] + self.Ix2[i]) / 2,4))
            # self.Ix.append(self.Ix1[i] + (self.Ix2[i] / 2))
        print(f"Ix:{self.Ix}")


    def Ix_Is1(self):
        """
        计算△Ix = Ix - Is(list)
        :return:
        """
        self.Ix_Is = []
        for i in range(8):
            self.Ix_Is.append(round(self.Ix[i] - self.Is[i],4))
        print(f"Ix_Is:{self.Ix_Is}")

    def grade(self):
        """
        计算电流表的级别
        :return:
        """
        k = max(self.Ix_Is)/max(self.Is)
        print(f"电流表的级别为{k*100}%")
        print(f"电流表的级别为{round(k*100,2)}%")
        return k

    def img(self):
        # self.Is_temp存储float类型的self.Is数据（list）
        self.Is_temp = []
        for Is in self.Is:
            self.Is_temp.append(float(Is))

        # self.Ix_Is_temp存储float类型的self.Ix_Is数据（list）
        self.Ix_Is_temp = []
        for Ix_Is in self.Ix_Is:
            self.Ix_Is_temp.append(float(Ix_Is))

        # self.temp中存储对应的点坐标（Is,△Ix）(list(tuple))
        self.temp = []
        for i in range(8):
            self.temp.append((self.Is_temp[i],self.Ix_Is_temp[i]))

        mpl.rcParams['font.sans-serif'] = ['SimHei']
        mpl.rcParams['axes.unicode_minus'] = False
        # 创建画布用于画Is-△Ix的图
        fig = plt.figure(dpi=128,figsize=(9,6))
        # 设置x轴的刻度
        xticks(np.linspace(0,16,10,endpoint=True))
        # 设置y轴的刻度
        yticks(np.linspace(0,0.1,10,endpoint=True))
        # 添加网格线
        plt.grid(axis='x',linestyle='-.')
        plt.grid(axis='y',linestyle='-.')
        # 画Is-△Ix的折线图
        plt.plot(self.Is_temp,self.Ix_Is_temp,c='black',alpha=0.5)
        # 画Is-△Ix的散点图
        plt.scatter(self.Is_temp,self.Ix_Is_temp,c='black',alpha=0.5)
        # 该代码一定要在plot之后，通过其改变网格之间的宽度
        # plt.xticks(self.Is_temp), plt.yticks(self.Ix_Is_temp)
        # 将对应的坐标（Is,△Ix）标记到图上
        plt.title("电流表校正曲线")
        for i in range(8):
            plt.annotate(self.temp[i], xy=(self.Is_temp[i], self.Ix_Is_temp[i]), xytext=(self.Is_temp[i]+0.001 , self.Ix_Is_temp[i]+0.001 ))        # 这里xy是需要标记的坐标，xytext是对应的标签坐标
        plt.xlabel('Is(mA)',fontsize=12)
        plt.ylabel('△Ix=(Ix-Is)(mA)',fontsize=12)
        plt.tick_params(axis='both',which='major',labelsize=16)

        plt.savefig('result_img\{}.png'.format(f"实验图片{randint(1,100)}")) # 保存图片
        plt.show()


    def main(self):
        self.cal_Ix1(self.Ux1)
        self.cal_Ix2(self.Ux2)
        self.cal_Ix()
        print(f"Is:{self.Is}")
        self.Ix_Is1()
        self.grade()
        self.img()

    




if __name__=="__main__":
    Ux1 = [0.0227,1.8713,3.8285,6.5266,8.2801,9.6878,12.4071,15.1359]
    Ux2 = [0.0244,1.8740,3.8355,6.5223,8.2797,9.6987,12.4206,15.1575]
    # Is = [0.0235,1.938,3.876,6.485,8.265,9.715,12.389,15.051] # 源数据

    # Ix = [0.0236, 1.8727, 3.832, 6.5244, 8.2799, 9.6932, 12.4139, 15.1467]
    Is = [0.0235,1.838,3.776,6.485,8.265,9.615,12.389,15.051]
    obj = Use(Ux1=Ux1,Ux2=Ux2,Is=Is)
    obj.main()


"""

Ix:[0.0236, 1.8727, 3.832, 6.5244, 8.2799, 9.6932, 12.4139, 15.1467]
Is:[0.0235, 1.838, 3.776, 6.485, 8.265, 9.615, 12.389, 15.051]
Ix_Is:[0.0001, 0.0347, 0.056, 0.0394, 0.0149, 0.0782, 0.0249, 0.0957]
"""


