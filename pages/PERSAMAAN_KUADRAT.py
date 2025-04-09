import streamlit as st

st.title("PERSAMAAN FUNGSI KUADRAT")
st.header("DISKRIMINAN")


db = st.number_input("Masukan Nilai b", value=0)
da = st.number_input("Masukan Nilai a", value=0)
dc = st.number_input("Masukan Nilai c", value=0)
st.subheader("Format: (b² -4 a c)")

dd = -db**2 - (4 * (da * dc))  # Correction
st.subheader(dd)

st.header("SUMBU SIMETRI")
xb = st.number_input("Masukan Nilai b:")
xa = st.number_input("Masukan Nilai a:")
st.subheader("Format: -b/2a")

try:
    x = -xb / (2 * xa)
except ZeroDivisionError:
    x = 0
st.subheader(x)

st.header("NILAI OPTIMUM")
nob = st.number_input("Masukan Nilai b ")
noa = st.number_input("Masukan Nilai a ")
noc = st.number_input("Masukan Nilai c ")
st.subheader("Format: -D/4a [-(b² - 4ac/4a)]")

try:
    nod = (-(nob**2 -4 * noa * noc)) / (4 * noa)
except ZeroDivisionError:
    nod = 0
st.subheader(nod)
