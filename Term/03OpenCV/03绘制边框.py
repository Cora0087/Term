import cv2
path = 'D:/Captures/Saved Pictures/fufu.jpg'
img = cv2.imread(path)
#print(img.shape)

paste_path = 'D:/Captures/Saved Pictures/mm.jpg'
img_to_paste = cv2.imread(paste_path)
# print(img_to_paste.shape)

#opencv打开的图像颜色是BGR
#cv2.imshow('img', img)
# img[:20, :, :] = (0, 0, 0)HWC
# img[20:, :, :] = (0, 0, 0)
# img[:, :20, :] = (5, 0, 0)

#完成左右两边的边框
#an_img = cv2.revise(an_img,(50,50))
#img[50:100, 50:100] = (0, 0, 255)

# img_to_paste = cv2.resize(img_to_paste, (500, 300))
if img.shape[:2] != img_to_paste.shape[:2]:
    img_to_paste = cv2.resize(img_to_paste, (500, 300))

# 确定粘贴的位置（左上角的坐标）
top_left_x = 500
top_left_y = 300

# 确定粘贴的区域
bottom_right_x = top_left_x + img_to_paste.shape[1]
print(bottom_right_x)
bottom_right_y = top_left_y + img_to_paste.shape[0]
print(bottom_right_y)

# 将要粘贴的图像复制到目标图像的指定位置
img[top_left_y:bottom_right_y, top_left_x:bottom_right_x] = img_to_paste

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()