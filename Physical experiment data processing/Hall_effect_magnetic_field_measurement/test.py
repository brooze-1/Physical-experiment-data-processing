# 开发时间：2021/10/14  13:28
import csv
from matplotlib import pyplot as plt
# matplotlib绘图无法显示中文问题的解决方法(见下面两行代码)
from pylab import *
mpl.rcParams['font.sans-serif'] = ['SimHei']

class process_data(object):
    def __init__(self,filename,Is=7.96,K=170):
        # 设置Is的默认值为7.86，K的默认值为170
        self.Is = Is
        self.K = K
        self.title_name=filename
        self.filename = "data/{}.csv".format(filename)
        self.Uh_lst = []
        # self.tmp用来临时存储self.B的数据(字符串)
        self.tmp = []
        # self.tmp_tmp用来临时存储self.B的数据
        self.tmp_tmp = []
        # B_lst用于存储使用Uh计算出来的B值
        self.B_lst = []
        # self.X用于存储点之间的距离(字符串)
        self.X = []
        # self.X_tmp用于存储点之间的距离(整型)
        self.X_tmp = []

    # 计算Uh(计算公式：(U3-U2+U1-U4)/4)
    def calculation_Uh(self):
        reader = csv.reader(open("{}".format(self.filename), "r"))
        data_lst = []
        i = 0
        # 处理数据跳过字段，只拿数据不拿字段
        for row in reader:
            if i < 1:
                i += 1
                continue
            elif i==1:
                self.X = row
                i+=1
                del self.X[0]
                for j in self.X:
                    self.X_tmp.append(int(j))
                print(self.X_tmp)
            else:
                # print(row)
                data_lst.append(row)
                i += 1
        # print(data_lst)
        for i in range(1, 11):
            # 利用计算公式：(U3-U2+U1-U4)/4计算Uh
            Uh = (float(data_lst[0][i]) - float(data_lst[1][i]) + float(data_lst[2][i]) - float(data_lst[3][i])) / 4
            self.Uh_lst.append("{:.3f}".format(Uh))
        # print(self.Uh_lst)

    # 计算B（计算公式：Uh=KIB其中I=Is=8）
    def calulation_B(self):
        for i in range(10):
            # 利用（计算公式：Uh=KIB其中I=Is=8）计算B
            B = (float(self.Uh_lst[i])) / (self.K * self.Is)
            self.B_lst.append("{:.7f}".format(B))
            # 将不含字段的B传给B_lst
            self.tmp=self.B_lst
        # 将self.tmp中的字符串数据转换成浮点型数据存储至self.tmp_tmp
        """
        为什么要转成浮点型数据？
            因为在画图时，如果X与Y轴传入的数据是字符串类型的数据的话，不会自动排序X轴与Y轴
        """
        for j in self.tmp:
            self.tmp_tmp.append(float(j))
        print(self.tmp)

    def write_Uh_into_csv(self):
        # 添加参数newline=’’,避免写入数据是产生空行
        f = open("{}".format(self.filename), "a",newline='')
        csvwriter = csv.writer(f)
        self.Uh_lst.insert(0, "Uh")
        csvwriter.writerow(self.Uh_lst)

    def write_B_into_csv(self):
        # 添加参数newline=’’,避免写入数据是产生空行
        f = open("{}".format(self.filename), "a",newline='')
        csvwriter = csv.writer(f)
        self.B_lst.insert(0, "B")
        csvwriter.writerow(self.B_lst)


    def reader(self):
        reader = csv.reader(open(self.filename,"r"))
        for row in reader:
            print(row)

    def Mapping_B_and_x(self):
        # # self.temp中存储对应的点坐标（self.X_tmp[i],self.tmp_tmp[i]）(list(tuple))
        # self.temp = []
        # for i in range(10):
        #     self.temp.append((self.X_tmp,self.tmp_tmp))

        fig = plt.figure(dpi=128,figsize=(10,6))
        plt.plot(self.X_tmp,self.tmp_tmp,c="red",alpha=0.5)
        plt.scatter(self.X_tmp,self.tmp_tmp,c="red",alpha=0.5)
        # # 将对应的坐标（self.X_tmp[i],self.tmp_tmp[i]）标记到图上
        # for i in range(10):
        #     # 这里xy是需要标记的坐标，xytext是对应的标签坐标
        #     plt.annotate(self.temp[i], xy=(self.X_tmp[i], self.tmp_tmp[i]), xytext=(self.X_tmp[i] , self.tmp_tmp[i] ))
        title = "B=f(x)  {}".format(self.title_name)
        plt.title(title,fontsize=20)
        plt.xlabel("X",fontsize=16)
        fig.autofmt_xdate()
        plt.ylabel("B",fontsize=16)
        plt.tick_params(axis="both",which="major",labelsize=16)
        plt.savefig('result_png\{}.png'.format(self.title_name))  # 保存图片
        plt.show()



    def main(self):
        # 计算Uh
        self.calculation_Uh()
        # 计算B
        self.calulation_B()
        # 画出B关于X的图
        self.Mapping_B_and_x()
        # 将计算出来的Uh数据写入csv文件
        self.write_Uh_into_csv()
        # 将计算出来的B数据写入csv文件
        self.write_B_into_csv()
        # 读出写入后csv文件中的数据
        self.reader()





if __name__=="__main__":
    # 亥姆霍兹线圈的测量数据1(Ba)
    # 亥姆霍兹线圈的测量数据2(Bb)
    # 亥姆霍兹线圈的测量数据3(Ba+b)
    # 单个截流原线圈磁场测量数据
    # 直螺线管内的磁场测量数据
    # obj = process_data("直螺线管内的磁场测量数据")
    # obj.main()
    filenames = [
        "亥姆霍兹线圈的测量数据1(Ba)",
        # "亥姆霍兹线圈的测量数据2(Bb)",
        # "亥姆霍兹线圈的测量数据3(Ba+b)",
        # "单个截流原线圈磁场测量数据",
        # "直螺线管内的磁场测量数据"
                 ]
    for filename in filenames:
        obj = process_data(filename)
        obj.main()
