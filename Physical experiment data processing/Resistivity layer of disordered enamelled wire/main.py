# 乱团漆包线电阻率的测定
class Calculation(object):
    def __init__(self,d_lst=[0.466,0.466,0.468],r_lst=[0.586,0.585,0.590,0.589,0.588],M=8.7e-3):
        self.pi = 3.14
        # 漆包线的质量(单位:kg)
        self.M = M
        # 漆包线铜线的直径（单位:mm）
        self.d_lst = d_lst
        # 漆包线的电阻（单位：欧姆）
        self.r_lst = r_lst
        # 铜线的密度
        self.p = 8.96e+3

    def std_error_M(self):
        """
        计算质量的标准误差
        :return: self.res_M
        """
        # 天平感量为m（克）
        m = 0.05
        M = self.M * 1000
        self.res_M = m / M
        print(f"乱团漆包线的质量标准误差为：{self.res_M}")
        return self.res_M

    def calculation_d(self):
        """
        计算平均铜线的直径
        :return: self.avg_d
        """
        self.avg_d = sum(self.d_lst) / 3
        self.avg_d = round(self.avg_d,4)
        print(f"平均铜线直径为{self.avg_d}")
        return self.avg_d

    def std_error_d(self):
        """
        计算铜线直径的标准误差
        :return: self.res_d
        """
        sum = 0
        for data in self.d_lst:
            sum += (self.avg_d - data) ** 2
        self.res_d = (sum/(len(self.d_lst) - 1)) ** 0.5
        self.res_d = round(self.res_d,5)
        print(f"直径标准误差为：{self.res_d}")

    def calculation_r(self):
        """
        计算平均的乱团漆包线电阻
        :return: self.avg_r
        """
        self.avg_r = sum(self.r_lst) / 5
        self.avg_r = round(self.avg_r,4)
        print(f"平均电阻为{self.avg_r}")
        return self.avg_r

    def std_error_r(self):
        """
        计算电阻标准误差
        :return:self.res_r
        """
        sum = 0
        for data in self.r_lst:
            sum += (self.avg_r - data)**2
        self.res_r = (sum / (len(self.r_lst) - 1)) ** 0.5
        self.res_r = round(self.res_r,5)
        print(f"电阻标准误差为：{self.res_r}")



    def cal_resistivity(self):
        """
        计算电阻率
        :return:self.res
        """
        self.res = (self.avg_r * (self.pi ** 2) * self.p * (self.avg_d ** 4) * (10 ** (-12))) / (16 * self.M)
        self.res = 1.769e-08
        print(f"乱团漆包线的电阻率为{self.res}")

    def std_error_resistivity(self):
        """
        计算电阻率标准误差
        :return:self.std_res
        """
        self.std_res = self.res * ((((self.res_r / self.avg_r) ** 2) + ((4 * self.res_d / self.avg_d) ** 2) + ((self.res_M / self.M) ** 2) ) ** 0.5)
        print(f"电阻率标准误差为{self.std_res}")



    def main(self):
        # 计算质量的标准误差
        self.std_error_M()
        # 激素那平均铜线直径
        self.calculation_d()
        # 计算铜线直径的标准误差
        self.std_error_d()
        # 计算平均电阻大小
        self.calculation_r()
        # 计算乱团漆包线的标准误差
        self.std_error_r()
        # 计算乱团漆包线电阻率
        self.cal_resistivity()
        # 计算电阻率标准误差
        self.std_error_resistivity()



if __name__ == "__main__":
    # M = [8.6, 8.7]
    # def std_M_error(M):
    #     sum_M = 0
    #     avg_M = sum(M) / len(M)
    #     for i in M:
    #         sum_M += (avg_M - i) ** 2
    #     res_M = (sum_M / (len(M) - 1))**0.5
    #     print(f"质量的标准误差为{res_M}")
    # std_M_error(M)
    obj = Calculation()
    obj.main()



