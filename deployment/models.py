import streamlit as st
import pandas as pd
import pickle
from PIL import Image

def run():
# Load All Files

    with open('model_grid.pkl', 'rb') as file:
        full_process = pickle.load(file)


    Area = st.number_input(label='input Area here',min_value=7551.000000,max_value=18913.000000)
    Perimeter = st.number_input(label='choose your Perimeter',min_value=359.100006,max_value=548.445984)
    Major_Axis_Length =  st.number_input(label='choose your Major_Axis_Length',min_value=145.264465,max_value=239.010498)
    Minor_Axis_Length =  st.number_input(label='choose your Minor_Axis_Length',min_value=59.532406,max_value=107.542450)
    Eccentricity =  st.number_input(label='choose your Eccentricity',min_value=0.872402,max_value=0.948007)
    Convex_Area =  st.number_input(label='choose your Convex_Area',min_value=7723.000000,max_value=19099.000000)
    Extent =  st.number_input(label='choose your Extent',min_value=0.497413,max_value=0.861050)
    
    st.write('In the following is the result of the data you have input : ')
    
    data_inf = pd.DataFrame({
        "Area": Area,
        "Perimeter": Perimeter,
        "Major_Axis_Length": Major_Axis_Length,
        "Minor_Axis_Length": Minor_Axis_Length,
        "Eccentricity": Eccentricity,
        "Convex_Area": Convex_Area,
        "Extent": Extent,
        }, index=[0])

    st.table(data_inf)

    
    if st.button(label='predict'):
    
        # Melakukan prediksi data dummy
        y_pred_inf = full_process.predict(data_inf)

        
        st.metric(label="Here is the prediction model : ", value = y_pred_inf[0])