import streamlit as st

st.title("Website Isinya Gabut Milik Shn")
st.write(
    "Hello teman teman yang membuka web ini :)"
)
st.image("req.jfif", width=700)

st.title("Aplikasi Sederhana")
st.header("Aplikasi mengecek nilai Genap/Ganjil")
angka = st.number_input("Tulis sebuah angka", value)

if (angka % 2) == 0:
    st.write("f{angka} adalah bilangan Genap")
else :
    st.write(f"{angka} adalah bilangan Ganjil")
    
