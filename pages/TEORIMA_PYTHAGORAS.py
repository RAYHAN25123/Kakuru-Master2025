import streamlit as st
import math

st.title("Teorema Pythagoras")
st.markdown("""
### Penjabaran :
- c = Sisi Miring
- a = Alas
- b = Tinggi
### RUMUS :
- c2 = a2 + b2
- a2 = c2 - b2
- b2 = c2 - a2
""")

st.subheader("Mencari C (Sisi Mriring)")
a = st.number_input("Masukkan panjang sisi a:", min_value=0.0)
b = st.number_input("Masukkan panjang sisi b:", min_value=0.0)
c = a **2 + b **2
c1 = c **0.5
st.header("Hasil C (Sisi Miring)")
st.subheader(c1)

st.subheader("Mencari a (Alas)")
c2 = st.number_input("Masukkan panjang sisi miring c:", min_value=0.0)
a1 = st.number_input("Masukkan panjang sisi b:", min_value=0.0, key= "key b")
b1 = c2 **2 + a1 **2
b2 = b1 **0.5
st.header("Hasil C (Sisi Miring)")
st.subheader(b2)

