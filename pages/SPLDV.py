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

try:
    # Rumus eliminasi & substitusi
    x = (c*q - r*b) / (a*q - p*b)
    y = (c - a*x) / b

    st.caption("Note: AI KAKURU akan mencari variabel x dengan metode eliminasi lalu mencari variabel y dengan metode substitusi")

    st.header("Nilai X")
    st.subheader(x)

    st.header("Nilai Y")
    st.subheader(y)
