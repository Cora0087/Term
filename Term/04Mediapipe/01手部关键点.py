import mediapipe as mp
import cv2

class Hands:
    def __init__(self):
        self.mp_hands = mp.solutions.hands.Hands()
        pass

    def process(self, frame):
        # 实例化Hands对象
        # mp_hands = mp.solutions.hands.Hands()
        mp_hands = self.mp_hands
        # 将frame的BGR图像转换为RGB图像
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # Processes an RGB image and returns the hand landmarks
        # and handedness of each detected hand.
        result = mp_hands.process(frame_rgb)
        hand_landmarks_list = result.multi_hand_landmarks
        landmarks = hand_landmarks_list[0]
        # 连接点
        conns = mp.solutions.hands_connections.HAND_CONNECTIONS
        # 关键点样式
        hands_style = mp.solutions.drawing_utils.DrawingSpec(color=(0, 0, 255), thickness=2)
        # 连线样式
        conns_style = mp.solutions.drawing_utils.DrawingSpec(color=(0, 0, 0), thickness=2)
        # 进行关键点样式的绘制
        mp.solutions.drawing_utils.draw_landmarks(
            image=frame,
            landmark_list=landmarks,
            connections=conns,
            landmark_drawing_spec=hands_style,
            connection_drawing_spec=conns_style,
        )
        pass


if __name__ == '__main__':
    mp_hands = Hands()
    cap = cv2.VideoCapture(0)
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        # 进行关键点检测
        mp_hands.process(frame)
        cv2.imshow('hands', frame)
        key = cv2.waitKey(60)
        if key == 'q':
            break
    cap.release()
    cv2.destroyAllWindows()