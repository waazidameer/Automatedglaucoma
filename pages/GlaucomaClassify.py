import streamlit as st
import pandas as pd
import random
import os
import numpy as np
import streamlit.components.v1 as components
from PIL import Image, ImageOps 
from tensorflow.keras.models import load_model 
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.mobilenet import preprocess_input
#import subprocess
#if not os.path.isfile('Sign-language/models/SignL.h5'):
    #subprocess.run(['curl --output SignL.h5 "https://media.githubusercontent.com/media/JwalithaKumar/Sign-language/main/sep_5.h5"'], shell=True)


st.set_page_config(
    page_title="SignLanguageDetection",
    initial_sidebar_state="expanded",
)


st.markdown(""" <style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style> """, unsafe_allow_html=True)

uploaded_file = None

st.title("Sign Language Detection")

st.write('<style>div.row-widget.stMarkdown { font-size: 24px; }</style>', unsafe_allow_html=True)

uploaded_file = st.file_uploader("Choose a File", type=['jpg','png','jpeg'])


if uploaded_file!=None:
    st.image(uploaded_file)
x = st.button("Predict")
if x:
    with st.spinner("Thinking..."):
        model = load_model('Sign-language/models/SignL.h5', compile = False)
        image = Image.open(uploaded_file)
        size = (224, 224)
        image = ImageOps.fit(image, size)
        image_array = np.asarray(image)
        image_array = np.expand_dims(image_array, axis=0)
        image_array = preprocess_input(image_array)
        predictions = model.predict(image_array)
        predicted_class_index = np.argmax(predictions)
        custom_class_labels = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z","del","nothing","space"]
        predicted_class_label = custom_class_labels[predicted_class_index]
        #Print the predicted class label and its corresponding probability
        st.write(predicted_class_index)
        st.write(predicted_class_label)
