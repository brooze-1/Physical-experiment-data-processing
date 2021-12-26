import csv
class huabian(object):
    def __init__(self,Rv=750,k=0.005):
        # 获取电流电压数据
        with open('电流电压数据.csv','r',encoding='utf8') as f:
            reader = csv.reader(f)
            self.U_lst = next(reader)
            del self.U_lst[0]
            self.I_lst = next(reader)
            del self.I_lst[0]
            print("I_lst:",self.I_lst)
            print('U_lst:',self.U_lst)
        # self.Rx_lst
        self.Rx_lst = []
        # self.Rxo_lst
        self.Rxo_lst = []
        # 电压表内阻 self.Rv = 750(Ω)
        self.Rv = Rv
        # 电压表级数等于电流表级数等于0.005
        self.k = k
        # 电压表最大量程为(mA)
        self.U_max = 1500
        # 电流表最大量程为（mA）
        self.I_max = 150


    # 计算Rx及Rxo及Rxo的平均值
    def cal_avg(self):
        # 计算Rx
        for index,u in enumerate(self.U_lst):
            # print(index)
            # print(u)
            self.Rx_lst.append(round(float(u)/float(self.I_lst[index]),2))
        print('Rx_lst:',self.Rx_lst)
        # 计算Rx0
        for index,u in enumerate(self.U_lst):
            self.Rxo_lst.append(round(float(u)/(float(self.I_lst[index])-(float(u)/self.Rv)),2))
        print('Rxo_lst:',self.Rxo_lst)
        # 计算Rxo的平均值
        self.avg_Rxo = round(sum(self.Rxo_lst)/len(self.Rxo_lst),2)
        print("avg_Rxo:",self.avg_Rxo)



    # 计算A类不确定度
    def cal_A(self):
        sum = 0
        for Rxo in self.Rxo_lst:
            sum += (Rxo-self.avg_Rxo)**2
        self.SRxo = round((sum/(len(self.Rxo_lst)-1))**0.5,5)
        print(f"A类不确定度为{self.SRxo}")

    # 计算B类不确定度
    def cal_B(self):
        self.u = (1/3)*self.U_max
        print('self.u(mV):',self.u)
        self.I = self.u/self.avg_Rxo
        print('self.I(mA):',self.I)
        # 计算乘以△U的那部分
        self.U = (self.I*(self.Rv**2))/(((self.I*self.Rv)-self.u)**2)
        print('self.U(mV):',self.U)
        # 计算乘以△I的那部分
        self.i = (self.u*(self.Rv**2))/(((self.I*self.Rv)-self.u)**2)
        print('self.i(mA):',self.i)
        # 计算B类不确定度
        self.URxo = round(((self.U*self.U_max*self.k)**2 + (self.i*self.I_max*self.k)**2)**0.5,5)
        print(f"B类不确定度为：{self.URxo}")


    # 计算总不确定度
    def cal_sum(self):
        self.S = round(((self.SRxo)**2 + (self.URxo)**2)**0.5,5)
        print("总不确定度S:",self.S)

    # 计算相对误差
    def relative_mistake(self):
        self.E = round(self.S/self.avg_Rxo,5)
        print(f'相对误差为:{self.E*100}%')

    # 主函数
    def main(self):
        # 计算Rx及Rxo及Rxo的平均值
        self.cal_avg()
        # 计算A类不确定度
        self.cal_A()
        # 计算B类不确定度
        self.cal_B()
        # 计算总不确定度
        self.cal_sum()
        # 计算相对误差
        self.relative_mistake()

if __name__=="__main__":
    obj = huabian()
    obj.main()
