import gradio as gr
import numpy as np
def apk( name, dob, self):
  out = 'hi '+ name
  zo = 'your sign is '+ dob
  return( out, zo)
i=gr.Image(source="webcam", streaming=True)
fr =gr.Interface(fn= apk, inputs=['text', 'text', i], outputs=['text', 'text'],capture_session=True,analytics_enabled=True, title='Face Reading')
fr.launch(debug='True')