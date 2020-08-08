# --coding:utf-8--

from keras.preprocessing import image
import glob
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import os
from keras.models import load_model


def read_image(img_path):
    try:
        img = image.load_img(img_path, target_size=(299, 299))
    except Exception as e:
        print(img_path, e)

    img = image.img_to_array(img)
    img = np.expand_dims(img, axis=0)
    return img/255

def draw_save(img_path, label, out='tmp/'):
    img = Image.open(img_path)
    # print(img_path.split('\\')[-2])
    # os.makedirs(os.path.join(out, label), exist_ok=True)
    # print(os.path.join(out, img_path.split('\\')[-3]))
    os.makedirs(os.path.join(out, img_path.split('\\')[-3]), exist_ok=True)
    if img is None:
        return None
    img = img.convert("RGB")
    # 在圖片上加入文字
    # draw = ImageDraw.Draw(img)
    # 使用中文字形
    # font = ImageFont.truetype("TW-Kai-98_1.ttf", 160)
    # # fill文字顏色 黃色
    # draw.text((10, 10), label, fill='#FFFF00', font=font)
    if label == '車尾':
        # 多
        # print(os.path.join(out, img_path.split('\\')[-3], "{}.jpg".format(img_path.split('.')[1].split('\\')[-1]).replace(' ', '')))
        img.save(os.path.join(out, img_path.split('\\')[-3], "{}.jpg".format(img_path.split('.')[1].split('\\')[-1]).replace(' ', '')))
    # 1
    # img.save(os.path.join(out, label, "{}.jpg".format(img_path.split('.')[1].split('\\')[1]).replace(' ', '')))


labels = {'車尾': 0, '非車尾': 1}
labels = {str(v): k for k, v in labels.items()}
# print(labels)
model = load_model('mode_iv3car_tail.h5')
# print(files)

# 1
# files = glob.glob("./pred/*")
# print(files[0])
# try:
#     img = read_image(files[0])
#     pred = model.predict(img)[0]
#     # 推論出機率最高的分類, 取得所在位置
#     index = int(round(pred[0]))
#     print(pred)
#     print(files[0], labels[str(index)], index)
#     try:
#         draw_save(files[0], labels[str(index)], out='tmp/')
#     except Exception as e:
#         print(files[0])
#         print(e)
# except Exception as e:
#     print(e)

# 多
files = glob.glob("./pred/*/*/*/*/*.jpg")
for i in range(len(files)):
    if i % (int(len(files)/10)) == 0:
        print(round(i*100/len(files), 1), '%')
    testID = i
    # print(files)
    # print(files[i])
    try:
        img = read_image(files[testID])
        pred = model.predict(img)[0]
        # 推論出機率最高的分類, 取得所在位置
        index = int(round(pred[0]))
        # print(pred)
        # print(files[testID], labels[str(index)], index)
        try:
            draw_save(files[testID], labels[str(index)], out='tmp/')
        except Exception as e:
            print(files[testID])
            print(e)
    except Exception as e:
        print(e)
