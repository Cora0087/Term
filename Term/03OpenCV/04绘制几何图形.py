import cv2
#1.找到路径
import numpy as np

path = 'D:/Captures/Saved Pictures/money.jpg'
#2.读取图片
img = cv2.imread(path)
print(img.shape)
#绘制线条
#所绘制线条位置 起点 终点 颜色 线条粗细
cv2.line(img=img, pt1=(100, 100), pt2=(200, 200), color=(255, 0, 0), thickness=2)
#绘制矩形
cv2.rectangle(img, (100, 100), (200, 200), (0, 0, 255), 2)
#绘制圆
cv2.circle(img, center=(100, 100), radius=100, color=(0, 255, 0), thickness=2)
#绘制多边形
pts = np.array([[100, 200], [150, 180], [200, 300], [230, 320]])
cv2.polylines(img, pts=[pts], isClosed=False, color=(0, 0, 255), thickness=2)
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
