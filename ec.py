import cv2
from imutils import face_utils
import dlib
import numpy as np
import webcolors
#from gradio import inputs, outputs, Interface
import color
import matplotlib.pyplot as plt
import keras.utils as image


def find_color(requested_colour):            
 
        min_colours = {}
        for name, key in webcolors.CSS3_HEX_TO_NAMES.items():
            r_c, g_c, b_c = webcolors.hex_to_rgb(name)
            rd = (r_c - requested_colour[0]) ** 2
            gd = (g_c - requested_colour[1]) ** 2
            bd = (b_c - requested_colour[2]) ** 2
            min_colours[(rd + gd + bd)] = key
            closest_name = min_colours[min(min_colours.keys())]
        return closest_name

def predict(path):
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor("D:\\st\\shape_predictor_68_face_landmarks.dat")
    flag=0
    img=image.load_img(path)

    plt.imshow(img)
    plt.show()
    img=image.img_to_array(img)
    #img= path
    img = cv2.resize(img,(240,240))
    img=img.astype('uint8')
    img_rgb= cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    plt.imshow(img_rgb)
    plt.show()   


    (left_Start, left_End) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]            
    #points for left eye and right eye
    (right_Start, right_End) = face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]

    
    dlib_faces = detector(img_rgb, 0)

    for face in dlib_faces:
        eyes = []                         
        print('loop')
        # convert dlib rect to a bounding box
        #(x,y,w,h) = face_utils.rect_to_bb(face)
        #cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),4) 
        #plt.imshow(img)
        #plt.show()      
    
        shape = predictor(img_rgb, face)
        shape = face_utils.shape_to_np(shape)

        
        leftEye = shape[left_Start:left_End]               
        rightEye = shape[right_Start:right_End]
        
        eyes.append(leftEye)  # wrap in a list
        eyes.append(rightEye)

        for index, eye in enumerate(eyes):
    
            print("loop")
            flag+=1
            left_side_eye = eye[0]  # left edge of eye
            right_side_eye = eye[3]  # right edge of eye
            top_side_eye = eye[1]  # top side of eye
            bottom_side_eye = eye[4]  # bottom side of eye

            # calculate height and width of dlib eye keypoints
            eye_width = right_side_eye[0] - left_side_eye[0]
            eye_height = bottom_side_eye[1] - top_side_eye[1]

            # create bounding box with buffer around keypoints
            eye_x1 = int(left_side_eye[0] - 0 * eye_width)  
            eye_x2 = int(right_side_eye[0] + 0 * eye_width)  
            eye_y1 = int(top_side_eye[1] - 1 * eye_height)
            eye_y2 = int(bottom_side_eye[1] + 0.75 * eye_height)

            cv2.rectangle(img,(eye_x1, eye_y1), (eye_x2, eye_y2),(0,255,0),1) 
            plt.imshow(img)
            plt.show()
            roi_eye = img_rgb[eye_y1:eye_y2 ,eye_x1:eye_x2]  
            #print(roi_eye)   #  desired EYE Region(RGB)
            if flag==1:
                break

        x=roi_eye.shape                                                      
        row=x[0] 
        col=x[1]
        print(x,row,col)
        array1=roi_eye[row//2:(row//2)+2,int((col//3)+3):int((col//3))+6]         
        print(array1)
        array1=array1[1][2] 
        print(array1)
        array1=tuple(array1)   #store it in tuple and pass this tuple to "find_color" Funtion                                                       

    global ec,c
    ec=find_color(array1)
    colour=color.switch(ec)
    return colour

print(predict("D:\\st\\f3.jpg"))