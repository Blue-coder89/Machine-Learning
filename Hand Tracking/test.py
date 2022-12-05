import cv2
import mediapipe as mp
cap = cv2.VideoCapture(0)
myHands = mp.solutions.hands
hands = myHands.Hands()
mpDraw = mp.solutions.drawing_utils
while True:
    success,image = cap.read()
    imgRGB = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    # print(results.multi_hand_landmarks)
    if results.multi_hand_landmarks:
        for hand in results.multi_hand_landmarks:
            mpDraw.draw_landmarks(image,hand,myHands.HAND_CONNECTIONS)
    cv2.imshow("Image" ,image)
    cv2.waitKey(1)