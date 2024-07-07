import cv2
#VideoCapture参数： 0 采集自己的摄像头 1/2外部摄像头
cap = cv2.VideoCapture(0)


while cap.isOpened():
    #retval 是否成功采集frame图像
    retval, frame = cap.read()
    if not retval:
        print("没有视频输入")
        break
    cv2.imshow('video', frame)
    key = cv2.waitKey(60)
    if key == ord('e'):#退出按那个键取决于输入的字母
        break

cap.release()
cv2.destroyAllWindows()