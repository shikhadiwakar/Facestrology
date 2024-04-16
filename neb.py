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
print(eyebrow_model.eval())
