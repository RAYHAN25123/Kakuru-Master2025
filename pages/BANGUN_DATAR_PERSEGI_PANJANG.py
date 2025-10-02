import streamlit as st

st.title("PERSEGI PANJANG")
st.markdown("""
### RUMUS :
- K = Keliling
- L = Luas
- p = Panjang
- l = Lebar
### RUMUS MENCARI KELILING :
- K = 2 x (p + l)
### RUMUS MENCARI LUAS :
- L = p x l
""")

p = st.number_input("Masukan Nilai Panjang:")
l = st.number_input("Masukan Nilai Lebar:")
st.header("KELILING")
k = 2 * p + 2 * l
st.subheader(k)
st.header("MENCARI PANJANG")

st.header("LUAS")
luas = p * l
st.subheader(luas)


