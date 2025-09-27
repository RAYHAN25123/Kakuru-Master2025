import streamlit as st

st.title("SISTEM PERSAMAAN LINEAR DUA VARIABEL")
st.subheader("Masih dalam tahap pengembangan")

st.subheader("Persamaan 1: ax + by = c")
a = st.number_input("Masukan Nilai Variabel a", value=0.0)
b = st.number_input("Masukan Nilai Variabel b", value=0.0)
c = st.number_input("Masukan Nilai Variabel c", value=0.0)

st.subheader("Persamaan 2: px + qy = r")
p = st.number_input("Masukan Nilai Variabel p", value=0.0)
q = st.number_input("Masukan Nilai Variabel q", value=0.0)
r = st.number_input("Masukan Nilai Variabel r", value=0.0)

x = (c*q-r*b)/(a*q-p*b)
y = (1/b)*(c-a*x)
except ZeroDivisionError: #Kecuali x = 0 y = 0
    x1 = 0 #Berarti ngubah semua valuenya jadi 0?
    y1 = 0

    st.header("Nilai X")
    st.subheader(x)

    st.header("Nilai Y")
    st.subheader(y)
