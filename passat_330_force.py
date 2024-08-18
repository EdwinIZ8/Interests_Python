"""
求帕萨特330 0km/h~100km/h加速过程中所受合力的大小。公式为：F = ma, a = (delta v) / (delta t)，数据来自汽车之家。
"""
def Passat_330_Force():
    F = 1580 * 100000 / 8.5 / 60 / 60
    print("Passat 330 = ", F, "N")


# 求一匹马有多大的牵引力。公式为：F = PS, S = pi * r^2，数据来自马德堡半球实验。
def Horse_Force():
    F1 = 95200 * 3.141592653589793 * 0.37 * 0.37 / 4 / 8
    F2 = 95200 * 3.141592653589793 * 0.37 * 0.37 / 4 / 4
    print(F1, "N", " < Horse < ", F2, "N")


if __name__ == "__main__":
    Passat_330_Force()
    Horse_Force()
