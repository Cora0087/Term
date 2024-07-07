import cv2
'''
1.找到图像路径
'''
#找到图像路径
path = "D:/Captures/Saved Pictures/fufu.jpg"
#读取图像
tupian = cv2.imread(path)
tupian = cv2.resize(tupian, (1065, 607))
print(tupian.shape)
#显示图像
cv2.imshow('ff', tupian)
key = cv2.waitKey(0)
if key == ord('a'):
    cv2.destroyAllWindows()