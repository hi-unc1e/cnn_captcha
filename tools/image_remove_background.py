from PIL import Image
import os
import numpy as np


def gen_captcha_text_image(img_path, img_name):
    """
    返回一个验证码的array形式和对应的字符串标签
    :return:tuple (str, numpy.array)
    """
    # 标签
    label = img_name.split("_")[0]
    # 文件
    img_file = os.path.join(img_path, img_name)
    captcha_image = Image.open(img_file)
    # captcha_image = captcha_image.crop((0, 0, 200, 60))
    captcha_array = np.array(captcha_image)  # 向量化
    return label, captcha_array


def convert2gray(img):
    """
    图片转为灰度图，如果是3通道图则计算，单通道图则直接返回
    :param img:
    :return:
    """
    if len(img.shape) > 2:
        r, g, b = img[:, :, 0], img[:, :, 1], img[:, :, 2]
        gray = 0.2989 * r + 0.5870 * g + 0.1140 * b
        return gray
    else:
        return img


def recognize_captcha(img):
    label, image_array = gen_captcha_text_image('./image_befor/', 'ng76m_1572101929872.png')
    img = convert2gray(image_array)
    img = Image.fromarray(np.uint8(img))
    img.save('./image_after/3.png')


def main():
    img = Image.open("./image_befor/2fdad_1572187319573.png")
    recognize_captcha(img)


if __name__ == '__main__':
    main()
