import streamlit as st
import math

st.title("Teorema Pythagoras")

if pilihan == "Sisi Miring (c)":
    a = st.number_input("Masukkan panjang sisi a:", min_value=0.0)
    b = st.number_input("Masukkan panjang sisi b:", min_value=0.0)
    if a > 0 and b > 0:
        c = math.sqrt(a**2 + b**2)
        st.success(f"✅ Panjang sisi miring (c) = {c:.2f}")

elif pilihan == "Sisi Siku (a atau b)":
    c = st.number_input("Masukkan panjang sisi miring (c):", min_value=0.0)
    x = st.number_input("Masukkan panjang sisi siku yang diketahui:", min_value=0.0)
    if c > 0 and x > 0 and c > x:
        sisi_lain = math.sqrt(c**2 - x**2)
        st.success(f"✅ Panjang sisi siku yang belum diketahui = {sisi_lain:.2f}")
    elif c > 0 and x > 0 and c <= x:
