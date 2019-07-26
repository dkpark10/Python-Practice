import os
import cv2
import numpy as np
import random
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip
from PyQt5.QtGui import QFont, QIcon
import sys

class DK_Gui(QWidget):

    def __init__(self):                     # self는 자기 객체
        super().__init__()
        self.initUI()                       # self 초기화

    def initUI(self):

        QToolTip.setFont(QFont('SansSerif', 10))
        self.setToolTip('This is a <b>QWidget</b> widget')
        btn = QPushButton('Button', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.move(50, 50)
        btn.resize(btn.sizeHint())

        self.setWindowTitle('DK_Augmentor')  # 타이틀바 제목
        self.setGeometry(400, 400, 500, 500) # 윈도우에서 출력되는 x,y 위치 윈도우창의 너비 높이
        self.setWindowIcon(QIcon('/home/dokyun/DangDang.jpg'))  # Icon Title
        self.show()

def Augmentor(origin_data_path, jpg_list):

    for i in range(len(jpg_list)):

        rand = random.randint(0,1)
        img = cv2.imread(origin_data_path + '/' + jpg_list[i], cv2.IMREAD_COLOR)

        if rand:
            Img_Mirror(img)
            Img_Resize(img)
            Img_Rotate(img)
        else:
            Img_Arrange(img)
            Img_Mirror_Rotate(img)

def Get_Jpg_List(path):

    if not(os.path.isdir(path)):
        return None

    file_list = os.listdir(path)
    img_jpg_list = []

    for jpg in file_list:
        if jpg.endswith(".jpg"):
            img_jpg_list.append(jpg)

    return img_jpg_list

def Create_Folder(base_path):

    create_path = base_path + "dataset"

    try:
        if not (os.path.isdir(create_path)):
            os.makedirs(os.path.join(create_path))
    except OSError as e:
        if e.errno != e.errno.EEXIST:
            raise

    return create_path

def Save_Img(img):

    save_path = Create_Folder(base_path)
    temp = jpg_list
    save_path += '/' + "edited_" + temp[0]
    del(temp[0])

    cv2.imwrite(save_path , img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def Img_Resize(img):

    ran = random.randint(0,1)
    height, width = img.shape[:2]
    if ran:
        shrink = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
        Save_Img(shrink)
        return shrink
    else:
        expand = cv2.resize(img, width * 2, height * 2, interpolation=cv2.INTER_CUBIC)
        Save_Img(expand)
        return expand

def Img_Arrange(img):

    ran = random.randint(0,1)
    height, width = img.shape[:2]
    matrix1 = np.float32([[1, 0, random.randint(5, 20)], [0, 1, random.randint(1, 30)]])
    matrix2 = np.float32([[0, 1, random.randint(5, 30)], [1, 0, random.randint(1, 20)]])

    if ran:
        arrange1 = cv2.warpAffine(img, matrix1, (height, width))
        Save_Img(arrange1)
        return arrange1
    else:
        arrange2 = cv2.warpAffine(img, matrix2, (height, width))
        Save_Img(arrange2)
        return arrange2

def Img_Mirror(img):

    mirrored = cv2.flip(img,1)
    Save_Img(mirrored)
    return mirrored

def Img_Rotate(img):

    height,width = img.shape[:2]
    ran = random.randint(0,1)
    rot_matrix1 = cv2.getRotationMatrix2D((height / 2, width / 2), random.randint(15, 28), 0.7)
    rot_matrix2 = cv2.getRotationMatrix2D((height / 2, width / 2), random.randint(-25, 12), 1.2)

    if ran:
        rota1 = cv2.warpAffine(img,rot_matrix1,(height,width))
        Save_Img(rota1)
        return rota1
    else:
        rota2 = cv2.warpAffine(img,rot_matrix2,(height,width))
        Save_Img(rota2)
        return rota2

def Img_Mirror_Rotate(img):

    mirimg = Img_Mirror(img)
    height, width = mirimg.shape[:2]
    ran = random.randint(0, 1)

    rot_matrix1 = cv2.getRotationMatrix2D((height / 2, width / 2), random.randint(15, 28), 0.7)
    rot_matrix2 = cv2.getRotationMatrix2D((height / 2, width / 2), random.randint(-25, 12), 1.2)

    if ran:
        mirrot1 = cv2.warpAffine(mirimg, rot_matrix1, (height, width))
        Save_Img(mirrot1)
        return mirrot1
    else:
        mirrot2 = cv2.warpAffine(mirimg, rot_matrix2, (height, width))
        Save_Img(mirrot2)
        return mirrot2

if __name__ == "__main__":

    # base_path = "/home/dokyun/Yolo_mark/x64/Release/data/"
    # origin_data_path = base_path + sys.argv[1]
    # print("Run Main")
    #
    # jpg_list = Get_Jpg_List(origin_data_path)
    # #if jpg_list != None :
    # #    Augmentor(origin_data_path, jpg_list)

    # img = cv2.imread("/home/dokyun/DangDang.jpg",cv2.IMREAD_COLOR)
    # # height, width = img.shape[:2]
    #
    # expand = cv2.resize(img, None, fx=2.0, fy=2.0, interpolation=cv2.INTER_CUBIC)
    # shrink = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
    # cv2.imwrite("/home/dokyun/DangDang2.jpg" , shrink)
    # cv2.imwrite("/home/dokyun/DangDang3.jpg" , expand)

    app = QApplication(sys.argv)
    ex = DK_Gui()
    sys.exit(app.exec_())

else:
    print("module")
