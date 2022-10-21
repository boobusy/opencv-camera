# date:2022-10-21
# Author: Boobusy

import cv2
import tkinter
from tkinter import *
from PIL import Image, ImageTk #图像控件

capture = cv2.VideoCapture(0)
# 设置摄像头参数 
# capture.set(cv2.CAP_PROP_FRAME_WIDTH, 450)  # 宽度 
# capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 450) # 高度
# capture.set(cv2.CAP_PROP_FPS, 30) # 帧数
# capture.set(cv2.CAP_PROP_BRIGHTNESS, 80) # 亮度 1
# capture.set(cv2.CAP_PROP_CONTRAST,0) # 对比度 40
# capture.set(cv2.CAP_PROP_SATURATION, 0) # 饱和度 50
# capture.set(cv2.CAP_PROP_HUE, 0) # 色调 50
# capture.set(cv2.CAP_PROP_EXPOSURE, -3) # 曝光 50

# GUI 窗口
# 文档: http://c.biancheng.net/tkinter/canvas-widget.html
window = tkinter.Tk()
window.title("OpenCV Camera Setting")

frame_d = Frame(window)
frame_img = Frame(window)
v = StringVar()

# 创建执行函数
def func_scale_fps(value): 
    capture.set(cv2.CAP_PROP_FPS, float(value))

def func_scale_liangdu(value): 
    capture.set(cv2.CAP_PROP_BRIGHTNESS, float(value)) # 28

def func_scale_duibidu(value): 
    capture.set(cv2.CAP_PROP_CONTRAST, float(value))   # 21

def func_scale_baohedu(value):     
    capture.set(cv2.CAP_PROP_SATURATION, float(value)) # 35

def func_scale_sediao(value): 
    capture.set(cv2.CAP_PROP_HUE, float(value))        # 54


# 创建 Scale控件
scale_fps = tkinter.Scale(frame_d,
             label='FPS',
             from_=10,
             to=100,            
             #orient=tkinter.HORIZONTAL,   # 设置Scale控件水平方向显示, tkinter.VERTICAL
             length=400,           
             variable = v,          # 绑定变量
             tickinterval=5,        # 设置刻度滑动条的间隔
             command=func_scale_fps)  # 调用执行函数，是数值显示在 Label控件中

scale_liangdu = tkinter.Scale(frame_d,
             label='亮度',
             from_=-100,
             to=100,
             length=400,
             tickinterval=5,
             command=func_scale_liangdu) 

scale_duibidu = tkinter.Scale(frame_d,
             label='对比度',
             from_=-100,
             to=100,
             length=400,
             tickinterval=5,
             command=func_scale_duibidu)

scale_baohedu = tkinter.Scale(frame_d,
             label='饱和度',
             from_=-100,
             to=100,
             length=400,
             tickinterval=5,
             command=func_scale_baohedu)

scale_sediao = tkinter.Scale(frame_d,
             label='色调',
             from_=-100,
             to=100,
             length=400,
             tickinterval=5,
             command=func_scale_sediao)


# 创建画布
canvas = tkinter.Canvas(frame_img,
                   bg='#CDC9A5',
                   height=450,
                   width=450)

scale_fps.grid(row=1, column=1)
scale_liangdu.grid(row =1, column =2)
scale_duibidu.grid(row =1, column =3)
scale_baohedu.grid(row =1, column =4)
scale_sediao.grid(row =1, column =5)
scale_fps.set(value=30)
scale_liangdu.set(value=28)
scale_duibidu.set(value=21)
scale_baohedu.set(value=35)
scale_sediao.set(value=53)

canvas.grid(row=1, column=1)

frame_d.pack(side=tkinter.LEFT, padx=1,pady=1)
frame_img.pack(side=tkinter.RIGHT, padx=1,pady=1)

#界面画布更新图像
def tkImage():
    ref,frame = capture.read()
    frame = cv2.flip(frame, 1) #摄像头翻转
    cvimage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    pilImage = Image.fromarray(cvimage)
    pilImage = pilImage.resize((450, 450),Image.ANTIALIAS)
    tkImage =  ImageTk.PhotoImage(image=pilImage)
    return tkImage

while True:
  pic = tkImage()
  canvas.create_image(0,0,anchor = 'nw',image = pic)
  window.update()
  window.after(1)


# 进入消息循环
# window.mainloop()