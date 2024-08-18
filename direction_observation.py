"""
    原理：方向观测法
    功能：计算前视点平面坐标
    题目：有后视点A、测站点B、前视点C，已知点A、B坐标是(xa, ya)和(xb, yb)、线段BC长度distance、∠ABC大小angle，求点C坐标(xc, yc)。
    思路：
        1.以B为原点、B指向A方向为x轴正方向建立平面直角坐标系（简称自定义坐标系，是左手系），求C在自定义坐标系中的坐标(xc', yc')。
        2.将自定义坐标系旋转，使其与测量坐标系的方向一致，求旋转后C的坐标(xc", yc")。
        3.平移1中坐标系，使其原点与测量坐标系原点重合，求平移后C的坐标。
    答案：
        解：
            第一步：以B为原点、B指向A为x轴正方向，建立自定义坐标系，设C在自定义坐标系中坐标是(xc', yc')。
            xc' = distance * cos(angle)
            yc' = distance * sin(angle)

            第二步，将自定义坐标系旋转alpha，使其方向与测量坐标系一致，设此时C的坐标变为(xc", yc")。
            ①当xa - xb >= 0且ya - yb >= 0时（向量BA落在测量坐标系右上角象限时），
            应逆时针旋转alpha，
            alpha = arcsin((ya - yb)/distance)，
            此时：
            xc" = xc'cos(alpha) + yc'sin(alpha)
            yc" = yc'cos(alpha) - xc'sin(alpha)
            ②当xa - xb >= 0且ya - yb < 0时（向量BA落在测量坐标系左上角象限时），
            应顺时针旋转alpha，
            alpha = arcsin((ya - yb)/distance)，
            此时：
            xc" = xc'cos(alpha) - yc'sin(alpha)
            yc" = yc'cos(alpha) + xc'sin(alpha)
            ③当xa - xb < 0且ya - yb <= 0时（向量BA落在测量坐标系左下角象限时），
            应顺时针旋转alpha，
            alpha = π - arcsin((ya - yb)/distance)，
            此时：
            xc" = xc'cos(alpha) - yc'sin(alpha)
            yc" = yc'cos(alpha) + xc'sin(alpha)
            ④当xa - xb < 0且ya - yb > 0时（向量BA落在测量坐标系右下角象限时），
            应逆时针旋转alpha，
            alpha = π - arcsin((ya - yb)/distance)，
            此时：
            xc" = xc'cos(alpha) + yc'sin(alpha)
            yc" = yc'cos(alpha) - xc'sin(al®pha)

            第三步，将旋转后的坐标系沿x轴向上平移xb，再沿y轴向右平移yb，平移后的坐标系与测量坐标系是同一个坐标系，此时C的坐标变为(xc, yc)。
            xc = xc" + xb
            yc = yc" + yb

            答：至此，点C坐标已求得。
    用法：
        1.输入后视点点号、坐标；
        2.输入测站点点号、坐标；
        3.输入n个前视点点号、角度、水平距离；
        4.输出n个前视点点号、坐标

    补充：
        1.∠ABC是盘左、盘右观测的平均值
        2.本程序未经测试
        3.待完善
"""
import math
import sys

# 后视点坐标
xa = 0
ya = 0
# 测站点坐标
xb = 0
yb = 0
# 测站点与前视点的水平距离
distance = 0
# ∠ABC大小angle，弧度制
angle = 0
# 前视点点号、x坐标、y坐标
front_point = []


def position_in_diy_coordinate_system(horizontal_distance_between_B_and_C, angle_of_ABC):
    """
    以B为原点、B指向A为x轴正方向，建立自定义坐标系，设C在自定义坐标系中坐标是(xc', yc')。本函数计算xc'和yc'。
    :param horizontal_distance_between_B_and_C: 点B与点C的距离，应输入全局变量distance
    :param angle_of_ABC: ∠ABC大小，应输入全局变量angle
    :return: xc'(xc1)和yc'(yc1)
    """
    xc1 = horizontal_distance_between_B_and_C * math.cos(angle_of_ABC)
    yc1 = horizontal_distance_between_B_and_C * math.sin(angle_of_ABC)
    result = [xc1, yc1]
    return result


def position_after_rotation(xc1, yc1):
    """
    将自定义坐标系旋转alpha，使其方向与测量坐标系一致，设此时C的坐标变为(xc", yc")。本函数计算xc"和yc"。
    :param xc1: 就是xc'
    :param yc1: 就是yc'
    :return: xc"和yc"
    """
    if xa >= xb and ya >= yb:
        alpha = math.asin((ya - yb) / distance)
        xc2 = xc1*math.cos(alpha) + yc1*math.sin(alpha)
        yc2 = yc1*math.cos(alpha) - xc1*math.sin(alpha)
    elif xa >= xb and ya < yb:
        alpha = math.asin((ya - yb) / distance)
        xc2 = xc1*math.cos(alpha) - yc1*math.sin(alpha)
        yc2 = yc1*math.cos(alpha) + xc1*math.sin(alpha)
    elif xa < xb and ya <= yb:
        alpha = math.pi - math.asin((ya - yb) / distance)
        xc2 = xc1*math.cos(alpha) - yc1*math.sin(alpha)
        yc2 = yc1*math.cos(alpha) + xc1*math.sin(alpha)
    elif xa < xb and ya > yb:
        alpha = math.pi - math.asin((ya - yb) / distance)
        xc2 = xc1*math.cos(alpha) + yc1*math.sin(alpha)
        yc2 = yc1*math.cos(alpha) - xc1*math.sin(alpha)
    else:
        print("程序终止，position_after_rotation函数出错，居然还有第五种情况？")
        sys.exit()
    result = [xc2, yc2]
    return result


def position_after_move(xc2, yc2):
    """
    将旋转后的坐标系沿x轴向上平移xb，再沿y轴向右平移yb，平移后的坐标系与测量坐标系是同一个坐标系，此时C的坐标变为(xc, yc)。本函数计算xc和yc。
    :param xc2: 就是xc"
    :param yc2: 就是yc"
    :return: xc和yc
    """
    xc = xc2 + xb
    yc = yc2 + yb
    result = [xc, yc]
    return result


def degrees_to_radians(degrees_minute_second):
    """
    将度分秒转换成弧度
    :param degrees_minute_second:度分秒格式
    :return: 弧度格式
    """
    split_string = degrees_minute_second.split(',')  # 分隔度分秒
    degrees = split_string[0] + split_string[1] / 60 + split_string[2] / 3600  # 度分秒转换成度
    radians = math.radians(degrees)  # 度转换成弧度
    return radians


if __name__ == '__main__':
    stop_program = input("已输入每一个测站数据？（y/n）")
    while stop_program == "n":
        # 输入后视点、测站点信息
        name_a = input("后视点点号：")
        xa = input("后视点x坐标：")
        ya = input("后视点y坐标：")
        name_b = input("测站点点号：")
        xb = input("测站点x坐标：")
        yb = input("测站点y坐标：")

        stop_station = input("已输入所有前视点数据？（y/n）")
        while stop_station == "n":
            name_c = input("前视点点号：")
            distance = input("水平距离：")
            angle_left = input("∠ABC大小（盘左，角度制，度分秒之间用半角逗号分隔）:")
            angle_right = input("∠ABC大小（盘右，角度制，度分秒之间用半角逗号分隔）:")
            angle_left_in_radians = degrees_to_radians(angle_left)
            angle_right_in_radians = degrees_to_radians(angle_right)
            angle = (angle_left_in_radians + angle_right_in_radians) / 2  # 取盘左、盘右平均数
            step1 = position_in_diy_coordinate_system(distance, angle)
            step2 = position_after_rotation(step1[0], step1[1])
            step3 = position_after_move(step2[0], step2[1])
            front_point_c = [name_c, step3[0], step3[1]]
            front_point += front_point_c
            stop_station = input("已输入所有前视点数据？（y/n）")
        stop_program = input("已输入所有测站数据？（y/n）")
    # 输出结果到屏幕
    print("点号 x坐标 y坐标")
    for point in front_point:
        for item in point:
            print(item, end=" ")
        print("")
