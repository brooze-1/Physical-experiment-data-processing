"""处理霍尔效应测磁场"""
import csv
# 处理单个截流原线圈
def deal_dange():
    dange_lst = []
    reader = csv.reader(open("data/单个截流原线圈磁场测量数据.csv"))
    i = 0
    for row in reader:
        if i<=1:
            i+=1
            continue
        else:
            # print(row)
            dange_lst.append(row)
            i+=1
    # print(dange_lst)
    Uh_lst1 = []
    # 公式(U3-U2+U1-U4)/4
    for i in range(1,11):
        Uh = (float(dange_lst[0][i])-float(dange_lst[1][i])+float(dange_lst[2][i])-float(dange_lst[3][i]))/4
        Uh_lst1.append("{:.3f}".format(Uh))
    print(Uh_lst1)

def zhiluo():
    reader = csv.reader(open("data/直螺线管内的磁场测量数据.csv"))
    zhiluo_lst = []
    i = 0
    for row in reader:
        if i <= 1:
            i += 1
            continue
        else:
            # print(row)
            zhiluo_lst.append(row)
            i += 1
    # print(zhiluo_lst)
    Uh_lst2 = []
    # 公式(U3-U2+U1-U4)/4
    for i in range(1, 11):
        Uh = (float(zhiluo_lst[0][i]) - float(zhiluo_lst[1][i]) + float(zhiluo_lst[2][i]) - float(zhiluo_lst[3][i])) / 4
        Uh_lst2.append("{:.3f}".format(Uh))
    print(Uh_lst2)


# 计算Uh(计算公式：(U3-U2+U1-U4)/4)
def calculation_Uh(filename):
    reader = csv.reader(open("data/{}.csv".format(filename),"r"))
    data_lst = []
    i = 0
    for row in reader:
        if i <= 1:
            i += 1
            continue
        else:
            # print(row)
            data_lst.append(row)
            i += 1
    # print(zhiluo_lst)
    Uh_lst = []
    for i in range(1, 11):
        Uh = (float(data_lst[0][i]) - float(data_lst[1][i]) + float(data_lst[2][i]) - float(data_lst[3][i])) / 4
        Uh_lst.append("{:.3f}".format(Uh))
    print(Uh_lst)
    calulation_B(Uh_lst)
    write_Uh_into_csv(filename,Uh_lst)

# 计算B（计算公式：Uh=KIB其中I=Is=8）
def calulation_B(Uh_lst):
    B_lst = []
    Is = 8
    K = 170
    for i in range(10):
        B = (float(Uh_lst[i]))/(K*Is)
        B_lst.append("{:.5f}".format(B))
    print(B_lst)


def write_Uh_into_csv(filename,Uh_lst):
    f = open("data/{}.csv".format(filename),"a")
    csvwriter = csv.writer(f)
    Uh_lst.insert(0,"Uh")
    csvwriter.writerow(Uh_lst)


def write_B_into_csv(filename,B_lst):
    f = open("data/{}.csv".format(filename),"a")
    csvwriter = csv.writer(f)
    B_lst.insert(0,"B")
    csvwriter.writerow(B_lst)

if __name__=="__main__":
    # deal_dange()
    # zhiluo()
    calculation_Uh("直螺线管内的磁场测量数")

