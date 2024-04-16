from keras.models import load_model
import keras.utils as image
import numpy as np
import cv2
import keras.backend as K

def get_f1(y_true, y_pred): #taken from old keras source code
    true_positives = K.sum(K.round(K.clip(y_true * y_pred, 0, 1)))
    possible_positives = K.sum(K.round(K.clip(y_true, 0, 1)))
    predicted_positives = K.sum(K.round(K.clip(y_pred, 0, 1)))
    precision = true_positives / (predicted_positives + K.epsilon())
    recall = true_positives / (possible_positives + K.epsilon())
    f1_val = 2*(precision*recall)/(precision+recall+K.epsilon())
    return f1_val

classes=["Heart", "Oblong", "Oval", "Round", "Square"]

dependencies={'get_f1':get_f1}
fsm=load_model('fsm.h5',custom_objects=dependencies)

def predict(file):
   img=image.img_to_array(file)
   img=cv2.resize(img,(200,200))
   img=img.reshape(1,200,200,3)
   img=img.astype('float32')
   img/=255
   a=np.argmax(fsm.predict(img),axis=1)[0]
   global fs
   fs=(classes[a])
   return fs