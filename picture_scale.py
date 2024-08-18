"""
环境：Python 3(3.12.1) + opencv-python(4.9.0.80)
作者：张家馨
功能：批量缩放图片。（最多支持89张.jpg图片）
缘由：C++批量缩放图片的python版。python代码可移植性强（Write once，run anywhere.），所以写了这个程序，以备家里使用。

要求：
    numpy==2.0.1
    opencv-python==4.10.0.84
    setuptools==72.1.0
    wheel==0.43.0
"""

import cv2 as cv
import sys
import os


width = 800 # 默认图片宽度


def resize(filename_to_resize: str):
    """
    缩放图片
    """
    img = cv.imread(filename_to_resize)
    height = img.shape[0] * width // img.shape[1]
    dst = cv.resize(img, (width, height))
    if filename_to_resize[:2] == "./":
        filename_to_resize = filename_to_resize[2:]
    if cv.imwrite(filename_to_resize, dst):
        print(filename_to_resize, " has been resized.")


def nextfile(filename_to_change: str):
    """
    换文件名。（比如：001.jpg -> 002.jpg）
    """
    # temp = list(filename_to_change)
    # if temp[-5] == "9":
    #     temp[-6] = str(int(temp[-6]) + 1)
    #     temp[-5] = "0"
    # else:
    #     temp[-5] = str(int(temp[-5]) + 1)
    # return "".join(temp)
    if filename_to_change[-5] == "9":
        filename_to_change[-6] = str(int(filename_to_change[-6]) + 1)
        filename_to_change[-5] = "0"
    else:
        filename_to_change[-5] = str(int(filename_to_change[-5]) + 1)
    return filename_to_change


if __name__ == "__main__":
    print("\n----------启动程序----------")
    print("最多支持89张.jpg格式的图片。")
    if len(sys.argv) < 2:
        print("\n----------错误----------")
        print("用法: python3 picture_scale.py <文件名>")
    else:
        if sys.argv[1][-4:] != ".jpg":
            print("\n----------错误----------")
            print("图片格式不是.jpg。")
        print("\n----------开始处理----------")
        width = int(input("输入要求的图片宽度（像素）: "))
        filename = sys.argv[1]
        while os.path.exists(filename):
            resize(filename)
            filename = nextfile(filename)
        print("\n----------运行完毕----------\n")

