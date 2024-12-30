import streamlit as st

# Set halaman utama
st.set_page_config(page_title="Formula 1 Data Analysis", page_icon="🏎️", layout="wide")

# Judul halaman
st.title("Formula 1 Data Analysis")

# Deskripsi halaman
st.write("""
    Selamat datang di aplikasi analisis data Formula 1. 
    Pilih menu di samping untuk melihat berbagai analisis tentang performa konstruktor, pembalap, tren, dan lainnya.
""")

# Menu Navigasi
menu = ["Dashboard", "Performa Konstruktor", "Performa Pembalap", "Tren Musim", "Statistik Lainnya"]
choice = st.sidebar.selectbox("Pilih Menu", menu)

# Konten untuk setiap menu
if choice == "Dashboard":
    st.subheader("Dashboard")
    st.write("Ini adalah tampilan dashboard utama. Semua analisis data Formula 1 akan ditampilkan di sini.")
    
elif choice == "Performa Konstruktor":
    st.subheader("Analisis Performa Konstruktor")
    st.write("Data tentang performa konstruktor Formula 1 akan ditampilkan di sini.")
    st.write("Tunggu sampai data tersedia!")

elif choice == "Performa Pembalap":
    st.subheader("Analisis Performa Pembalap")
    st.write("Data tentang performa pembalap Formula 1 akan ditampilkan di sini.")
    st.write("Tunggu sampai data tersedia!")

elif choice == "Tren Musim":
    st.subheader("Tren Musim Formula 1")
    st.write("Analisis tren sepanjang musim Formula 1 akan ditampilkan di sini.")
    st.write("Tunggu sampai data tersedia!")

elif choice == "Statistik Lainnya":
    st.subheader("Statistik Lainnya")
    st.write("Berbagai statistik lainnya terkait Formula 1 akan ditampilkan di sini.")
    st.write("Tunggu sampai data tersedia!")
