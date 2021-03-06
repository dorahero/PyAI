import cv2
import numpy as np

images = []
images.append(cv2.imread("facer/face1.jpg",cv2.IMREAD_GRAYSCALE))
images.append(cv2.imread("facer/face2.jpg",cv2.IMREAD_GRAYSCALE))
images.append(cv2.imread("facer/face3.jpg",cv2.IMREAD_GRAYSCALE))
images.append(cv2.imread("facer/face4.jpg",cv2.IMREAD_GRAYSCALE))
images.append(cv2.imread("facer/face5.jpg",cv2.IMREAD_GRAYSCALE))

labels = [0,0,0,1,1]

# 創建辨識訓練器
recognizer = cv2.face.LBPHFaceRecognizer_create()
# 帶入影像與 label
recognizer.train(images,np.array(labels))
# 傳入測試影像 可轉灰階亦可不轉
predict_image=cv2.imread("facer/test.jpg",cv2.IMREAD_GRAYSCALE)
print(recognizer.predict(predict_image))
label,confidence = recognizer.predict(predict_image)
print('label:',label)
print("confidence:",confidence)