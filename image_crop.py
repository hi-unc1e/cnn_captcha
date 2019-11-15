"""
验证图片尺寸和分离测试集（5%）和训练集（95%）
初始化的时候使用，有新的图片后，可以把图片放在new目录里面使用。
"""
import cv2 as cv
import json
import time, datetime
import numpy
from PIL import Image
import random
import os
import shutil
import matplotlib.pyplot as plt
import numpy as np


def verify(origin_dir, new_dir):
    """
    校验图片大小
    :return:
    """
    if not os.path.exists(origin_dir):
        print("【警告】找不到目录{}，即将创建".format(origin_dir))
        os.makedirs(origin_dir)

    print("开始校验原始图片集")
    # 图片真实尺寸
    # 图片名称列表和数量
    img_list = os.listdir(origin_dir)
    total_count = len(img_list)
    print("原始集共有图片: {}张".format(total_count))
    # 无效图片列表
    bad_img = []

    # 遍历所有图片进行验证
    for index, img_name in enumerate(img_list):
        file_path = os.path.join(origin_dir, img_name)
        # 过滤图片标签不标准的情况
        # prefix, posfix = img_name.split("_")
        # if prefix == "" or posfix == "":
        #     bad_img.append((index, img_name, "图片标签异常"))
        #     continue

        # 图片无法正常打开
        try:
            img = Image.open(file_path)
            #
            img = img.crop((0, 0, 200, 60))
            str_file = img_name[0:5]
            time1, time2 = str(time.time() * 10).split(".")
            # print(time1, time2)
            # file_name = str_file + "_" + time1 + ".png"
            img.save(new_dir + img_name)
            os.remove(origin_dir+"/"+img_name)
            # own_threshold(new_dir, img_name, img_name)
        except OSError:
            bad_img.append((index, img_name, "图片无法正常打开"))
            continue


def own_threshold(img):  # 自己设置阈值68           全局
    img.flags.writeable = True  # 将数组改为读写模式
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)  # 首先变为灰度图
    ret, binary = cv.threshold(gray, 69.0, 255,
                               cv.THRESH_BINARY)  # cv.THRESH_BINARY |cv.THRESH_OTSU 根据THRESH_OTSU阈值进行二值化
    # 上面的0 为阈值 ，当cv.THRESH_OTSU 不设置则 0 生效
    # ret 阈值 ， binary二值化图像
    cv.imshow("11", binary)
    cv.waitKey(0)
    img = Image.fromarray(np.uint8(binary))
    b = img = np.array(img)
    img.flags.writeable = False
    img = Image.fromarray(np.uint8(b))
    depoint(img)



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


def main():
    with open("conf/sample_config.json", "r") as f:
        sample_conf = json.load(f)
    # 图片路径
    origin_dir = sample_conf["origin_image_dir"]
    new_dir = sample_conf["new_origin_image_dir"]
    #
    for image_dir in [origin_dir, new_dir]:
        print(">>> 开始校验目录：[{}]".format(image_dir))
    verify('sample/api', "sample/cut_image/")




if __name__ == '__main__':
    main()
