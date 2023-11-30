import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# from phik.report import plot_correlation_matrix
from PIL import Image

#membuat function untuk nantinya dipanggil di app.py
def run():
    st.title('Welcome to Explaration Data Analysis')
# #Memanggil data csv 
#     df= pd.read_csv(r'P1G5_Set_1_furqon.csv')

# #menampilakn 5 data teratas
#     st.table(df.head(5))


#menampilakn Explaration Data Analysis 1
    # st.title('Explaration Data Analysis')
    image = Image.open('output1.png')
    st.image(image, caption='Penyebaran jenis beras spesies Osmancik dan spesies Cammeo.')

#menampilkan penjelasan 
    # st.write('lebih banyak jumlah data pada bOsmancik daripada bCammeo.')
    with st.expander('Explanation'):
         st.caption(
        f"""
        <div style="font-size: 15px; text-align: justify;">
        <ul> 
            <li>lebih banyak jumlah data pada b'Osmancik' daripada b'Cammeo'.</li>
            <li>perbedaan dari kedua jenis spesies ini tidak jauh beda.</li>
        </ul>
        </div>
        """,
        unsafe_allow_html=True)

#menampilakn Explaration Data Analysis 2
    # st.title('Explaration Data Analysis')
    image = Image.open('output2.png')
    st.image(image, caption='Distribusi spesies beras dengan jumlah piksel di dalam batas-batas butiran beras.')

# #menampilkan penjelasan 
    with st.expander('Explanation'):
         st.caption(
        f"""
        <div style="font-size: 15px; text-align: justify;">
        <ul> 
            <li>terdapat distribusi jumlah piksel baik itu garis tengah, garis bawah, garis atas pada spesies commeo lebih besar daripada osmancik.</li>
        </ul>
        </div>
        """,
        unsafe_allow_html=True)
#menampilakn Explaration Data Analysis 3
    # st.title('Explaration Data Analysis')
    image = Image.open('output3.png')
    st.image(image, caption='Persebaran batas butiran beras dengan jarak kelilingnya.')

# #menampilkan penjelasan 
    with st.expander('Explanation'):
         st.caption(
        f"""
        <div style="font-size: 15px; text-align: justify;">
        <ul> 
            <li>pola yang cenderung diagonal menunjukkan korelasi positif antara kedua variabel tersebut.</li>
            <li>artinya jumlah piksel pada beras semakin besar sesuai dengan jarak keliling nya.</li>
        </ul>
        </div>
        """,
        unsafe_allow_html=True)

#menampilakn Explaration Data Analysis 4
    # st.title('Explaration Data Analysis')
    image = Image.open('output4.png')
    st.image(image, caption='Mengukur seberapa bulat elips yang memiliki momen yang sama dengan butir beras.')

# #menampilkan penjelasan 


#menampilakn Explaration Data Analysis 5
    # st.title('Explaration Data Analysis')
    image = Image.open('output5.png')
    st.image(image, caption='Garis terpanjang yang dapat digambar pada spesies beras.')

# #menampilkan penjelasan 
#     with st.expander('Explanation'):
#         st.caption('---')

#menampilakn Explaration Data Analysis 6
    st.title('Visualisasi matriks korelasi antara berbagai variabel')
    image = Image.open('heatmap.png')
    st.image(image)
    st.write('Warna Terang : ')
    st.caption(
        f"""
        <div style="font-size: 15px; text-align: justify;">
        <ul> 
            <li>Area dan Contex area memiliki warna terang karena semakin besar area semakin besar kemungkinan area cembungnya.</li>
            <li>Pada Major Axis Length dan Minor Axis Length ini menunjukkan bahwa biji yang lebih panjang dalam satu arah cenderung lebih panjang dalam arah yang lain.</li>
            <li>Eccentricity dan Extent. Bijih dengan eksentrisitas yang tinggi cenderung memiliki ekstent yang rendah, dan sebaliknya.</li>
        </ul>
        </div>
        """,
        unsafe_allow_html=True)
    
    st.write('Warna Gelap : ')
    st.caption(
        f"""
        <div style="font-size: 15px; text-align: justify;">
        <ul> 
            <li>Tidak ada korelasi negatif yang kuat antara variabel-variabel yang ditampilkan dalam heatmap. Semua korelasi negatif terlihat lemah atau dekat dengan nol.</li>
        </ul>
        </div>
        """,
        unsafe_allow_html=True)
    
    st.write('Warna Netral : ')
    st.caption(
        f"""
        <div style="font-size: 15px; text-align: justify;">
        <ul> 
            <li>Sebagian besar pasangan variabel tidak menunjukkan korelasi yang kuat (warna netral pada heatmap). Ini berarti bahwa variabel-variabel ini relatif independen satu sama lain.</li>
        </ul>
        </div>
        """,
        unsafe_allow_html=True)
    
# #menampilkan penjelasan 
#     with st.expander('Explanation'):
#         st.caption('Education level tinggi memiliki pengaruh dalam melakukan pembayaran. Sebaliknya, education level terendah tidak daam pembayaran kartu kredit.')
