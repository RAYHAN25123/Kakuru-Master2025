import streamlit as st

st.title("Usaha")
st.markdown("""
- W = Usaha(Joule)
- F = Gaya (Newton)
- S = Perpindahan Benda (Meter)
""")
st.title("Rumus")
st.markdown("""
- W = F x S
""")
f = st.number_input("Masukan Gaya(Newton)")
s = st.number_input("Perpindahan Benda(Meter)")
w = f * s
st.header("Joule")
st.subheader(w)
