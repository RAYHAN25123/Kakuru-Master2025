import streamlit as st

st.title("BANGUN RUANG BALOK")

st.markdown("""
### Penjabaran :
- p = Panjang
- l = Lebar
- t = Tinggi
- K = Keliling
- L = Luas
- V = Volume
### Rumus Mencari Keliling :
- K = 4 x (p + l + t)
### Rumus Mencari Luas :
- L = 2 x (p x l + p x t + l x t)
### Rumus Mencari Volume :
- V = p x l x t

st.subheader("Balok")
p = st.number_input("Masukan Nilai Panjang:")
l = st.number_input("Masukan Nilai Lebar:")
t = st.number_input("Masukan Nilai Tinggi:")
st.header("KELILING")
k = 4 * ( p + l + t )
st.subheader(k)
st.header("LUAS BALOK")
l1 = 2 * (p * l + p * t + l * t)
st.subheader(l1)
st.header("VOLUME BALOK")
v = p * l * t
st.subheader(v)
