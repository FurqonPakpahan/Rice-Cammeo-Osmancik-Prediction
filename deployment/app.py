import streamlit as st
import eda
import models

st.sidebar.header("Rice")
st.sidebar.write("Cammeo and Osmancik.")

page = st.sidebar.selectbox(label='Select Page:', options=['Home Page', 'Exploratory Data Analysis', 'Model Prediksi'])

if page == 'Home Page':
    st.header('Welcome Page') 
    st.write('')
    # st.write('Milestone')
    st.write('Muhammad Furqon Pakpahan')
    # st.write('Batch     : HCK - 009')
    st.write('Objective : Di Turki ada 2 beras yang bersetifikat yang ditanam yaitu spesies Osmancik dan spesies Cammeo. Kedua beras ini dipilih untuk penelitian.')
    st.write('')
    st.caption('Silahkan pilih menu lain di Select Box pada sebelah kiri layar anda untuk memulai!')
    st.write('')
    st.write('')
    with st.expander("Latar Belakang"):
        st.caption('Beras adalah makanan pokok yang penting di banyak negara, termasuk Turki. Penelitian tentang berbagai spesies beras dapat memberikan wawasan yang berharga tentang karakteristik beras yang berbeda dan dapat digunakan untuk tujuan agronomi, pengembangan varietas, atau pemilihan biji yang tepat untuk keperluan komersial atau industri. Dalam hal ini, penelitian difokuskan pada dua spesies beras, yaitu Osmancik dan Cammeo, yang telah ditanam secara luas di Turki sejak tahun 1997 dan 2014.')

    with st.expander("Problem Statement"):
            st.caption('Memahami dan membedakan karakteristik antara spesies beras Osmancik dan Cammeo. Untuk mencapai tujuan, data yang mencakup 3810 gambar biji beras dari kedua spesies tersebut telah diambil, diproses, dan fitur-fitur morfologi telah diekstraksi. Terdapat 7 fitur morfologi yang diambil untuk setiap butir beras.')

    with st.expander("Kesimpulan"):
        st.caption('Tidak jauh perbedan yang signifikan antara Osmancik dan Cammeo. Dari klasifikasi yang dilakukan lebih dominan terhadap spesies Osmancik daripada Cammeo.')
elif page == 'Exploratory Data Analysis':
    eda.run()
else:
    models .run()

    