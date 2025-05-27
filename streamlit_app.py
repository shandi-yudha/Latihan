import streamlit as st

st.title("Website Isinya Gabut Milik Shn")
st.write(
    "Hello teman teman yang membuka web ini :)"
)
st.image("req.jfif", width=700)

st.title("Stand Power")
st.header("Aplikasi Mengecek Nilai Bilangan Ganjil/Genap")
angka = st.number_input("Tulis sebuah Angka", value=0, step=1)

if (angka % 2) == 0:
    st.write(f"{angka} adalah Bilangan Genap")
else :
    st.write(f"{angka} adalah Bilangan Ganjil")
st.write("King otw belajar coding")
    
