import torch
import torchvision
import tqdm
import torch.nn as nn
import torch.nn.functional as F
from torch.autograd import Variable
import torch
import torch.nn as nn
import cv2
import sys
import os
from PIL import Image

path='D:\\st\\t2.jpg'
crop_img='D:\\st\\t2 copy.jpg'
class CNN(nn.Module):
    def __init__(self,k):
        super(CNN, self).__init__()

        # define the layers
        # kernel size = 3 means (3,3) kernel
        # rgb -> 3 -> in channel
        # number of feature maps = 16
        # number of filters = 3 x 16
        self.l1 = nn.Conv2d(kernel_size=3, in_channels=3, out_channels=16)
        self.pool = nn.MaxPool2d(kernel_size=2, stride=2)
        # MaxPool2d, AvgPool2d.
        # The first 2 = 2x2 kernel size,
        # The second 2 means the stride=2

        self.l2 = nn.Conv2d(kernel_size=3, in_channels=16, out_channels=32)

        # FC layer
        self.fc1 = nn.Linear(32 * 48 * 48, k) # NUM OF CLUSTER
    
    def forward(self, x):
        # define the data flow through the deep learning layers
        x = self.pool(F.relu(self.l1(x))) # 16x16 x 14 x 14
        #print(x.shape)
        x = self.pool(F.relu(self.l2(x))) # 16x32x6x6
        #print(x.shape)
        x = x.reshape(-1, 32*48*48) # [16 x 1152]# CRUCIAL:
        #print(x.shape)
        x = self.fc1(x)
        return x

eyebrow_model = CNN(3)
eyebrow_model.load_state_dict(torch.load('D:\\st\\eyebrow_model.pt'))
eyebrow_model.eval()

class FaceCropper(object):
    CASCADE_PATH = cv2.data.haarcascades+ "haarcascade_frontalface_default.xml"

    def __init__(self):
        self.face_cascade = cv2.CascadeClassifier(self.CASCADE_PATH)

    def generate(self, image_path, show_result):
        img = cv2.imread(image_path)
        
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        faces = self.face_cascade.detectMultiScale(gray, 1.2, 4)
        if (show_result):
            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)
            cv2.imshow('img',img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

        facecnt = len(faces)
        print("Detected faces: %d" % facecnt)
        i = 0
        height, width = img.shape[:2]

        for (x, y, w, h) in faces:
            r = max(w, h) / 2
            centerx = x + w / 2
            centery = y + h / 2
            nx = int(centerx - r)
            ny = int(centery - r)
            nr = int(r * 2)

            faceimg = img[ny:ny+nr, nx:nx+nr]
            lastimg = cv2.resize(faceimg, (200, 200))
            i += 1
            cv2.imwrite(crop_img, lastimg)


detecter = FaceCropper()
detecter.generate(path, True)

types = dict()
types["eyebrow"] = ["Arch","Circle","Straight"]

#def sw(path):
detecter = FaceCropper()
detecter.generate(path, True)
preprocess = torchvision.transforms.Compose([
    # torchvision.transforms.RandomAffine(10),
    torchvision.transforms.ToTensor()])
img = Image.open(path)
img_tensor = preprocess(img)
img_tensor.unsqueeze_(0)
eyebrow = eyebrow_model(Variable(img_tensor))
eyebrow_shape = types["eyebrow"][torch.argmax(eyebrow).item()]
    #return eyebrow_shape
#eyebrow_shape = types["eyebrow"][torch.argmax(eyebrow).item()]
print("Eyebrow:  ",eyebrow_shape)