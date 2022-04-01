# 上海海洋大学视频切割
# cv2.imread()，cv2.imshow()，cv2.imwrite()读取、显示和保存图像
import cv2
cap = cv2.VideoCapture(r"C:\Users\86150\Desktop\上海海洋大学决赛圈回顾.flv")
num = 1
while 1:

    # 逐帧读取视频  按顺序保存到本地文件夹
    ret,frame = cap.read()
    if ret:
        cv2.imwrite(".\pictures\img_{"+ str(num) +".jpg",frame)
        num=num+1
    else:
        break
cap.release()   # 释放资源
