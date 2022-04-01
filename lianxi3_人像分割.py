# @File : 人像分割.py
"""原文链接："""
import cv2
import base64
import numpy as np
import os
from aip import AipBodyAnalysis
import time
import random

APP_ID = '******'
API_KEY = '**********************'
SECRET_KEY = '*****************'

client = AipBodyAnalysis(APP_ID, API_KEY, SECRET_KEY)
# 保存图像分割后的路径
path = './mask_img/'

# os.listdir  列出保存到图片名称
img_files = os.listdir('./pictures/')
print(img_files)
for num in range(1, len(img_files) + 1):
    # 按顺序构造出图片路径
    img = './pictures/img_{'+str(num)+'.jpg'
    img1 = cv2.imread(img)
    height, width, _ = img1.shape
    # print(height, width)
    # 二进制方式读取图片
    with open(img, 'rb') as fp:
        img_info = fp.read()

    # 设置只返回前景   也就是分割出来的人像
    seg_res = client.bodySeg(img_info)
    labelmap = base64.b64decode(seg_res['labelmap'])
    nparr = np.frombuffer(labelmap, np.uint8)
    labelimg = cv2.imdecode(nparr, 1)
    labelimg = cv2.resize(labelimg, (width, height), interpolation=cv2.INTER_NEAREST)
    new_img = np.where(labelimg == 1, 255, labelimg)
    mask_name = path + 'mask_{}.png'.format(num)
    # 保存分割出来的人像
    cv2.imwrite(mask_name, new_img)
    print(f'======== 第{num}张图像分割完成 ========')


