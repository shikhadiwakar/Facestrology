import fss
import zodiac
import json
import gradio as gr
import e
import fc
import z

types = dict()
types["eyebrow"] = ["Arch","Circle","Straight"]
types["colour"] = ["Blue","Green","Gray","Black","Brown"]
types["face shape"] = ["Oblong","Oval","Square","Heart","Round"]


def conclusion(region_name,region_type):
    with open('D:\\st\\ays.json') as json_file:
        data = json.load(json_file)
        #print('done')
        for region in data["face_regions"]:
            if region["name"] == region_name:
                for feature in region["features"]:
                    if feature["name"] == region_type:
                        return (feature["analysis"])


def pred(Full_Name,DOB,eye_color,face_data):
    zodiac_sign= zodiac.predict(DOB)
    hs=z.horoscope(zodiac_sign)

    eyec=conclusion("eye color",eye_color)
    face=fc.faceimage(face_data)
    face_shape= fss.predict(face)
    eyebrow= e.predict(face)
    
    x=conclusion("face shape",face_shape)
    y=conclusion("eyebrows",eyebrow)
   
    return ("Hey "+ Full_Name + " your zodiac sign as per your date of birth is "+ str(zodiac_sign),str(hs),"Your eye colour is "+str(eye_color)+"\n Meaning: "+str(eyec), "Your face shape is " + str(face_shape) + " \n Meaning: "+str(x), "Your eyebrow shape is " + str(eyebrow) + "\nMeaning: "+str(y))


i=gr.Image(source="webcam", streaming=True)

gr.Interface(fn= pred, inputs=['text', 'text','text', i], outputs=['text','text','text','text','text'], title='Face Reading').launch(debug='True')