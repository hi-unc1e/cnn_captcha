# coding=utf-8
from tkinter import *
from PIL import Image, ImageTk
import os, shutil


class WidgetsDemo:
    def __init__(self):
        # 用来保存图片文件名列表
        self.image_list = []

        # 设置文件名索引
        self.index = 0

        # 设置要移动的文件夹
        self.image_new = 'C:/Users/rong/Desktop/test/'
        self.image_old='G:/MyObject/kaptch_java/image'
        # self.image_new='F:\\方向领域综合设计\\tensorflow-examples-master\\captcha\\image_test\\'
        window = Tk()  # 创建一个窗口
        # 设置屏幕居中
        sw = window.winfo_screenwidth()
        sh = window.winfo_screenheight()
        ww = 400
        wh = 200
        x = (sw - ww) / 2
        y = (sh - wh) / 2
        window.geometry("%dx%d+%d+%d" % (ww, wh, x, y))
        window.title("Widgets Demo")  # 设置标题
        frame1 = Frame(window)  # 创建一个框架
        frame1.pack(side=TOP)  # 将框架frame1放置在window中
        self.E1 = Entry(frame1, bd=2, width=40)
        self.E1.pack(side=LEFT)
        self.b1 = Button(frame1, text='开始', command=self.get_image_list)
        self.b1.pack(side=RIGHT)

        frame2 = Frame(window)  # 创建一个框架
        frame2.pack()  # 将框架frame2放置在window中
        """
        self.pilImage = Image.open("checkcode.jpg")
        self.tkImage = ImageTk.PhotoImage(image=self.pilImage)
        self.label1 = Label(frame2, image=self.tkImage)
        """
        self.label1 = Label(frame2)
        self.label1.pack(side=TOP)
        self.E2 = Entry(frame2, bd=2)
        self.E2.pack(side=BOTTOM)
        self.E2.bind('<Key-Return>', self.rename)

        window.mainloop()

    # 将所有文件名放在self.image_list中
    def get_image_list(self):
        self.index = 0
        path = self.get_image_dir()
        for file in os.listdir(path):
            file_path = os.path.join(path, file)
            self.image_list.append(file_path)
        # print(self.image_list)
        self.pilImage = Image.open(self.image_list[self.index])
        self.tkImage = ImageTk.PhotoImage(image=self.pilImage)
        self.label1.configure(image=self.tkImage)

    # 返回文件夹路径
    def get_image_dir(self):
        image_dir = self.image_old
        return image_dir

    # 对回车的处理函数
    def rename(self, event):
        # 获取新的文件名以及清空文本框
        name = self.E2.get()
        self.E2.delete(0, END)
        # 进行文件的移动以及重命名
        new_file_path = self.image_new + name + '.png'
        shutil.move(self.image_list[self.index], new_file_path)
        # 更新预览图片
        self.index = self.index + 1
        self.pilImage = Image.open(self.image_list[self.index])
        self.tkImage = ImageTk.PhotoImage(image=self.pilImage)
        self.label1.configure(image=self.tkImage)


WidgetsDemo()
