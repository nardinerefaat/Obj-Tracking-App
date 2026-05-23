import streamlit as st 
import cv2 as cv 
import numpy as np 
import tempfile
import time

def convert_color(img):
    img = cv.cvtColor(img , cv.COLOR_BGR2RGB)
    return img
    

# GUI 
st.title("Object tracking App")
st.markdown("""
            open this cv app njfvkndvfkj

""")

st.set_page_config(
    page_title="Object Tracking App",
    layout="wide",
    page_icon=":guardsman:"
)


# Core function

uploaded_file = st.file_uploader("Uploaded videp" , type=["mp4" , "mov" , "avi" , "mkv"])

if uploaded_file is not None:
    # make embedded file has all the inputs and work on it
    tfile = tempfile.NamedTemporaryFile(delete=False)
    tfile.write(uploaded_file.read())
    tfile.close()

    captures = cv.VideoCapture(tfile.name)

    if not captures.isOpened():
        st.error("file is corupted")

    else:
        stFrame = st.empty() # Placeholder for video frames
        back_subtractor = cv.createBackgroundSubtractorMOG2()
        
            

        while captures.isOpened():
            ret , frame = captures.read()
            if not ret:
                break

            fg_mask = back_subtractor.apply(frame)
            
            (contours , _) = cv.findContours(fg_mask.copy() , cv.RETR_EXTERNAL , cv.CHAIN_APPROX_SIMPLE)
            for i in contours:
                if cv.contourArea(i) > 300:
                    # continue
                    (x , y , w , h) = cv.boundingRect(i)
                    cv.rectangle(frame , (x , y) , (x+w , y+h) , (0 , 255 , 0) , 2)

            stFrame.image(convert_color(frame) , channels="RGB", use_column_width=True  )
            # Delay
            time.sleep(0.01)
        


    captures.release()
    # cv.destroyAllWindows()       

            
        


    

