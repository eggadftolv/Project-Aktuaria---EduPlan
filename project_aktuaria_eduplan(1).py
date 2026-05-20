import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ====================================================
# CONFIG
# ====================================================

st.set_page_config(
    page_title="EduPlan+",
    page_icon="🎓",
    layout="wide"
)

# ====================================================
# SIDEBAR
# ====================================================

menu = st.sidebar.selectbox(
    "Menu",
    [
        "Home",
        "Dana Pendidikan",
        "Analisis Inflasi",
        "Konsultasi",
        "Tentang"
    ]
)

# ====================================================
# HOME
# ====================================================

if menu == "Home":

    st.title("🎓 EduPlan+")

    st.subheader(
        "Smart Education Financial Planner"
    )

    st.write("""
    EduPlan membantu masyarakat
    menghitung dana pendidikan masa depan
    menggunakan konsep aktuaria dan inflasi.
    """)

# ====================================================
# DANA PENDIDIKAN
# ====================================================

elif menu == "Dana Pendidikan":

    st.title("🎓 Simulasi Dana Pendidikan")

    biaya = st.number_input(
        "Biaya Pendidikan Saat Ini (Rp)",
        value=20000000
    )

    inflasi = st.number_input(
        "Inflasi Pendidikan (%)",
        value=10.0
    )

    tahun = st.number_input(
        "Jangka Waktu (Tahun)",
        value=10
    )

    investasi = st.selectbox(
        "Instrumen Investasi",
        [
            "Tabungan",
            "Deposito",
            "Reksa Dana"
        ]
    )

    # ================================================
    # RETURN
    # ================================================

    if investasi == "Tabungan":
        r = 0.03

    elif investasi == "Deposito":
        r = 0.05

    else:
        r = 0.10

    # ================================================
    # PERHITUNGAN
    # ================================================

    i = inflasi / 100

    FV = biaya * (1 + i) ** tahun

    i_bulan = r / 12

    n = tahun * 12

    PMT = (
        FV * i_bulan
    ) / ((1 + i_bulan) ** n - 1)

    # ================================================
    # OUTPUT
    # ================================================

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Biaya Masa Depan",
            f"Rp {FV:,.0f}"
        )

    with col2:

        st.metric(
            "Tabungan per Bulan",
            f"Rp {PMT:,.0f}"
        )

    # ================================================
    # GRAFIK
    # ================================================

    tahun_list = []
    biaya_list = []

    for t in range(tahun + 1):

        nilai = biaya * (1 + i) ** t

        tahun_list.append(t)

        biaya_list.append(nilai)

    fig, ax = plt.subplots()

    ax.plot(
        tahun_list,
        biaya_list,
        marker='o'
    )

    ax.set_title(
        "Pertumbuhan Dana Pendidikan"
    )

    ax.set_xlabel("Tahun")

    ax.set_ylabel("Biaya")

    st.pyplot(fig)

# ====================================================
# ANALISIS INFLASI
# ====================================================

elif menu == "Analisis Inflasi":

    st.title("📉 Analisis Risiko Inflasi")

    biaya = st.number_input(
        "Biaya Awal",
        value=20000000
    )

    tahun = st.number_input(
        "Tahun Persiapan",
        value=10
    )

    stabil = biaya * (1 + 0.05) ** tahun
    normal = biaya * (1 + 0.10) ** tahun
    krisis = biaya * (1 + 0.15) ** tahun

    data = pd.DataFrame({

        "Kondisi": [
            "Stabil",
            "Normal",
            "Krisis"
        ],

        "Biaya": [
            stabil,
            normal,
            krisis
        ]
    })

    st.dataframe(data)

# ====================================================
# KONSULTASI
# ====================================================

elif menu == "Konsultasi":

    st.title("💰 Konsultasi")

    target = st.number_input(
        "Target Dana Pendidikan",
        value=500000000
    )

    tahun = st.number_input(
        "Jangka Waktu",
        value=10
    )

    tabungan = target / (tahun * 12)

    st.metric(
        "Estimasi Tabungan/Bulan",
        f"Rp {tabungan:,.0f}"
    )

    if tabungan > 5000000:

        st.warning("""
        Target dana cukup besar.
        Disarankan memperpanjang waktu investasi.
        """)

    else:

        st.success("""
        Target dana masih realistis.
        """)

# ====================================================
# TENTANG
# ====================================================

elif menu == "Tentang":

    st.title("ℹ Tentang EduPlan+")

    st.write("""
    EduPlan merupakan aplikasi simulasi
    dana pendidikan berbasis aktuaria.
    """)
