import streamlit as st

st.title("Teorima Pythagoras")
st.markdown("""
### Penjabaran :
- a = Sisi siku-siku (Alas)
- b = Sisi siku-siku(Tinggi)
- c = Sisi miring

### Rumus :
- c2 = a2 + b2
- a2 = c2 - b2
- b2 = c2 - a2
""")

st.subheader("Mencari C")
a = st.number_input("Masukan a, key="a2")
b = st.number_input("Masukan b, key="b2")
c = a **2 + b **2
c1 = c **0.5
st.header("Hasil")
st.subheader(c1)

st.subheader("Mencari B")
c2 = st.number_input("Masukan c, key="c2")
a1 = st.number_input("Masukan a, key="a1")
b1 = c2 **2 - a1 **2
b2 = b1 **0.5
st.header("Hasil")
st.subheader(b2)
