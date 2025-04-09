import streamlit as st

st.title ("Percepatan")

st.subheader("(Rumus 1) Percepatan Dasar")
st.markdown("""
- v0 = Kecepatan Awal (m/s)
- v = Kecepatan Akhir (m/s)
- a = Pecepatan (m/s2)
- t = Waktu (s)
""")
st.subheader("Rumus")
st.markdown("""
- a = v - v0 / t
""")
v = st.number_input("Masukan Kecepatan Akhir (m/s)")
v1 = st.number_input("Masukan kecepatan Awal (m/s)")
t = st.number_input("Masukan Waktu (s)")
if t != 0:
    a = (v - v1) / t
else:
    a = 0.0
st.header("Percepatan (m/s2)")
st.subheader(a)

st.subheader("(Rumus 2) Percepatan Tidak Diketahui Waktu(Pakai Jarak)")
st.markdown("""
- v0 = Kecepatan Awal (m/s)
- v = Kecepatan Akhir (m/s)
- a = Pecepatan (m/s2)
- s = Jarak (m)
""")
st.subheader("Rumus")
st.markdown("""
- a = v2 - v0 2 / 2s
""")
v2 = st.number_input("Masukan Kecepatan Akhir (m/s)", key ="v2")
v3 = st.number_input("Masukan kecepatan Awal (m/s)", key ="v3")
s = st.number_input("Masukan Jarak (m)")
if s != 0:
    a1 = (v2 **2 - v3 **2) / (s **2)
    st.header("Percepatan (m/s2)")
    st.subheader(f" {a1}")

st.subheader("(Rumus 3) Percepatan Sentripetal(Gerak Melingkar)")
st.markdown("""
- v = Kecepatan Linear Beda (m/s)
- a = Pecepatan (m/s2)
- r = Jari - jari Lintasan Lingkaran (m)
""")
st.subheader("Rumus")
st.markdown("""
- a = v2 / r
""")
v4 = st.number_input("Masukan Kecepatan Akhir (m/s)", key ="v4")
r = st.number_input("Masukan Jari-jari Lintasan Lingkaran (m)")
if r != 0:
    a2 = v4 **2 / r
    st.header("Percepatan (m/s2)")
    st.subheader(f" {a2}")