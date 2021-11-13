import cv2
from skimage import transform, img_as_float


def checkered_face(frame):

    frame_gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    face=face_detector.detectMultiScale(frame_gray,1.5)
    for (x,y,w,h) in face:
        # frame[y:y+h,x:x+w]=cv2.GaussianBlur(frame[y:y+h,x:x+w],((w//2)|1,(h//2)|1),cv2.BORDER_DEFAULT)
        for i in range(y, y + h, 10):
            for j in range(x, x + w, 10):
                frame[i:i + 10, j:j + 10] = frame[i, j]
    return frame
face_detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

cap = cv2.VideoCapture(0)
fps = int(cap.get(cv2.CAP_PROP_FPS))
print("This is the fps ", fps)

while True:
    ret, frame = cap.read()

    if ret == False:
        break
    frame = checkered_face(frame)


    cv2.imshow('checkered face', frame)
    cv2.waitKey(10)
