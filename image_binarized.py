import os

from PIL import Image
import numpy

__author__ = "WSX"
import cv2 as cv
import numpy as np


# -----------二值化（黑0和白 255）-------------
# 二值化的方法（全局阈值  局部阈值（自适应阈值））
# OTSU
# cv.THRESH_BINARY 二值化
# cv.THRESH_BINARY_INV(黑白调换)
# cv.THRES_TRUNC 截断

def threshold(img):  # 全局阈值
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)  # 首先变为灰度图
    ret, binary = cv.threshold(gray, 0, 255,
                               cv.THRESH_BINARY | cv.THRESH_OTSU)  # cv.THRESH_BINARY |cv.THRESH_OTSU 根据THRESH_OTSU阈值进行二值化  cv.THRESH_BINARY_INV(黑白调换)
    # 上面的0 为阈值 ，当cv.THRESH_OTSU 不设置则 0 生效
    # ret 阈值 ， binary二值化图像
    # print("阈值：", ret)
    cv.imshow("binary", binary)


def own_threshold(img):  # 自己设置阈值68           全局
    # print(path)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)  # 首先变为灰度图
    ret, binary = cv.threshold(gray, 68.0, 255,
                               cv.THRESH_BINARY)  # cv.THRESH_BINARY |cv.THRESH_OTSU 根据THRESH_OTSU阈值进行二值化
    # 上面的0 为阈值 ，当cv.THRESH_OTSU 不设置则 0 生效
    # ret 阈值 ， binary二值化图像
    print("阈值：", ret)
    cv.imshow("binary", binary)
    # img = Image.fromarray(np.uint8(binary))
    # new_path = 'tools/image_befor/' + image_name
    # img.save(new_path)
    # image = depoint(Image.open(new_path))
    # os.remove(new_path)
    # return numpy.array(image)


def local_threshold(img):  # 局部阈值
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)  # 首先变为灰度图
    binary = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 25, 10, )  # 255 最大值
    # 上面的 有两种方法ADAPTIVE_THRESH_GAUSSIAN_C （带权重的均值）和ADAPTIVE_THRESH_MEAN_C（和均值比较）
    # blockSize 必须为奇数 ，c为常量（每个像素块均值 和均值比较 大的多余c。。。少于c）
    # ret 阈值 ， binary二值化图像
    cv.imshow("binary", binary)


def custom_threshold(img):  # 自己计算均值二值化
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)  # 首先变为灰度图
    h, w = gray.shape[:2]
    m = np.reshape(gray, [1, w + h])
    mean = m.sum() / w * h  # 求出均值
    binary = cv.threshold(gray, mean, 255, cv.THRESH_BINARY)
    cv.imshow("binary", binary)


def depoint(img):
    """传入二值化后的图片进行降噪"""
    pixdata = img.load()
    w, h = img.size
    for y in range(1, h - 1):
        for x in range(1, w - 1):
            count = 0
            if pixdata[x, y - 1] > 245:  # 上
                count = count + 1
            if pixdata[x, y + 1] > 245:  # 下
                count = count + 1
            if pixdata[x - 1, y] > 245:  # 左
                count = count + 1
            if pixdata[x + 1, y] > 245:  # 右
                count = count + 1
            if pixdata[x - 1, y - 1] > 245:  # 左上
                count = count + 1
            if pixdata[x - 1, y + 1] > 245:  # 左下
                count = count + 1
            if pixdata[x + 1, y - 1] > 245:  # 右上
                count = count + 1
            if pixdata[x + 1, y + 1] > 245:  # 右下
                count = count + 1
            if count > 4:
                pixdata[x, y] = 255
    return img

# def main():
#     img = cv.imread("./image_befor/rmanr_1572187329877.png")
#     # 新建一个显示窗口
#     cv.namedWindow("Show", cv.WINDOW_AUTOSIZE)
#     cv.imshow("Show", img)
#     own_threshold(img)
#     # 如果设置waitKey(0),则表示程序会无限制的等待用户的按键事件
#     cv.waitKey(0)
#     # 关闭窗口
#     cv.destroyAllWindows()
#
#
# main()
