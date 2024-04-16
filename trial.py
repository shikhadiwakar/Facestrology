#import eb
import fss
#import ec
import zodiac
import json
import gradio as gr

types = dict()
types["eyebrow"] = ["Arch","Circle","Straight"]
types["colour"] = ["Blue","Green","Gray","Black","Brown"]
types["face shape"] = ["Oblong","Oval","Square","Heart","Round"]
#types["nose"] = ["Long","Small","Wide"]
#types["mouth"] = ["Medium","Small","Thick"]


def conclusion(region_name,region_type):
    with open('C:\\Users\\shkhd\\OneDrive\\Documents\\ST\\ays.json') as json_file:
        data = json.load(json_file)
        #print('done')
        for region in data["face_regions"]:
            if region["name"] == region_name:
                for feature in region["features"]:
                    if feature["name"] == region_type:
                        return (feature["analysis"])

#print("\n")
#eyebrow_shape = types["eyebrow"][torch.argmax(eyebrow).item()]
#print("Eyebrow:  ",eyebrow_shape)
#print_description("eyebrows",eyebrow_shape)
#print("\n")
#path='D:\\bye.jpg'
#eb.crop_img='D:\\bye1.jpg'

#eyebrow = eb.sw(path)
#print("Eyebrow:",eyebrow)
#print_description("eyebrows",eyebrow_shape)
#print("\n")
def pred(name,dob, input, input_2):
    #eye_color = ec.predict(path)
    #f=("Eye Colour:",eye_color,'\n Meaning:')
    #print_description("eye color",eye_color)
    #return final1
    i = [input, input_2]
    if i == input:
        face_shape= fss.predict(input) 
    else:
        face_shape= fss.predict(input_2) 
    x=conclusion("face shape",face_shape)
    #print(face_shape)
    #g=("Face Shape:",face_shape,'\n Meaning:')
    #analysis=print_description("face shape",face_shape)
    #final=print('for eyes',final1, "\n" ,'for face',final2)
    #print (final)

    zodiac_sign= zodiac.predict(dob)
   # "Eye Colour:" + eye_color + '\n' + print_description("eye color",eye_color) + '\n'
    return ("Hey "+ name + " your zodiac sign as per your date of birth is "+ str(zodiac_sign), "Your face shape is " + str(face_shape) + "Meaning: "+str(x) )# + print_description("face shape",face_shape))


#i=gr.Image(source="webcam", streaming=True)
#gr.Interface(fn=pred, inputs=i, outputs='text',capture_session=True,analytics_enabled=True, title='Face Reading').launch(debug='True')
#plt.show()
input = gr.inputs.Image(type='pil', label="upload your image", source="upload", optional=True)
input_2 = gr.inputs.Image(type='pil', label="Live Input", source="webcam", optional=True)  
gr.Interface(fn= pred, inputs=['text', 'text',input, input_2], outputs=['text', 'text'],capture_session=True,analytics_enabled=True, title='Face Reading').launch(debug='True')
#print_description("eyes",eye_shape)
#print("\n")

#nose_shape = types["nose"][torch.argmax(nose).item()]
#print("Nose:     ",nose_shape)
#print_description("nose",nose_shape)
#print("\n")
#i=inputs.Image(type='filepath')
#Interface(fn=predict, inputs=i, outputs='text',capture_session=True).launch(debug='True')