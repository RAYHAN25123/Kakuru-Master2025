import streamlit as st

# Judul aplikasi
st.title("Aljabar")

# Input persamaan dari pengguna
persamaan_input = st.text_input("Masukkan persamaan aljabar (contoh: 2*x + 3 = 7)", "2*x + 3 = 7")

if persamaan_input:
    try:
        # Definisi variabel
        x = sp.symbols('x')

        # Pisahkan kiri dan kanan persamaan
        kiri, kanan = persamaan_input.split("=")
        persamaan = sp.Eq(sp.sympify(kiri), sp.sympify(kanan))

        # Tampilkan persamaan
        st.write("Persamaan yang dimasukkan:")
        st.latex(sp.latex(persamaan))

        # Selesaikan persamaan
        solusi = sp.solve(persamaan, x)

        st.write("👉 Solusi persamaan:")
        st.latex(f"x = {solusi}")

    except Exception as e:
        st.error(f"Terjadi kesalahan: {e}")
