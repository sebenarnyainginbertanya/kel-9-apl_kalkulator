import streamlit as st

st.header('Aplikasi Penjumlahan Bilangan Numerik', divider='rainbow')

angka_pertama = st.number_input('Masukkan Angka Pertama')
st.write('The First Number Is ', angka_pertama)

angka_kedua = st.number_input('Masukkan Angka Kedua')
st.write('The Second Number Is ', angka_kedua)

operasi_matematika = angka_pertama / angka_kedua
st.write(f"Angka Pertama {angka_pertama} x {angka_kedua} = {operasi_matematika}")
