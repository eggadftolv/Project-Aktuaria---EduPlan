# =========================================================
# EDUPLAN+
# FINAL FIXED VERSION
# STABLE FOR STREAMLIT CLOUD
# =========================================================

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="EduPlan+",
    page_icon="🎓",
    layout="wide"
)

# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

.main {
    background-color: #F4F7FE;
}

section[data-testid="stSidebar"] {
    background: linear-gradient(
        180deg,
        #0F172A 0%,
        #1E293B 100%
    );
}

section[data-testid="stSidebar"] * {
    color: white;
}

.big-title {
    font-size: 60px;
    font-weight: 800;
    color: #1E3A8A;
}

.sub-title {
    font-size: 24px;
    color: #475569;
}

.card {
    background: white;
    padding: 30px;
    border-radius: 20px;
    box-shadow: 0px 6px 16px rgba(0,0,0,0.08);
    margin-bottom: 25px;
}

[data-testid="metric-container"] {
    background: white;
    border-radius: 18px;
    padding: 20px;
    box-shadow: 0px 6px 16px rgba(0,0,0,0.08);
}

.footer {
    text-align: center;
    color: gray;
    padding: 20px;
}

h1, h2, h3 {
    color: #1E293B;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.title("🎓 EduPlan+")

menu = st.sidebar.radio(
    "📌 Navigation",
    [
        "🏠 Home",
        "🎓 Dana Pendidikan",
        "📉 Analisis Risiko Inflasi",
        "💰 Konsultasi",
        "📚 Edukasi Finansial",
        "ℹ Tentang Aplikasi"
    ]
)

# =========================================================
# HOME
# =========================================================

if menu == "🏠 Home":

    st.markdown(
        '<p class="big-title">🎓 EduPlan+</p>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<p class="sub-title">'
        'Smart Education Financial Planner'
        '</p>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="card">

    ## 📈 Mengapa EduPlan Dibuat?

    EduPlan membantu masyarakat memahami:
    - inflasi pendidikan
    - investasi pendidikan
    - perencanaan dana masa depan

    Biaya pendidikan terus meningkat setiap tahun,
    sehingga perencanaan dana pendidikan menjadi penting.

    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Inflasi Pendidikan", "10%")

    with col2:
        st.metric("Kenaikan Biaya", "2-3x")

    with col3:
        st.metric("Nilai Rupiah", "Melemah")

# =========================================================
# DANA PENDIDIKAN
# =========================================================

elif menu == "🎓 Dana Pendidikan":

    st.title("🎓 Simulasi Dana Pendidikan")

    col1, col2 = st.columns(2)

    with col1:

        jenis = st.selectbox(
            "Jenis Pendidikan",
            [
                "Dalam Negeri",
                "Luar Negeri"
            ]
        )

        tahun = int(st.number_input(
            "Jangka Waktu Persiapan (Tahun)",
            min_value=1,
            max_value=30,
            value=10
        ))

    with col2:

        # =====================================================
        # DALAM NEGERI
        # =====================================================

        if jenis == "Dalam Negeri":

            biaya = float(st.number_input(
                "Biaya Pendidikan Saat Ini (Rp)",
                min_value=100000,
                value=20000000,
                step=1000000
            ))

            inflasi = float(st.number_input(
                "Inflasi Pendidikan (%)",
                min_value=1.0,
                max_value=25.0,
                value=10.0,
                step=0.5
            ))

        # =====================================================
        # LUAR NEGERI
        # =====================================================

        else:

            mata_uang = st.selectbox(
                "Mata Uang",
                [
                    "USD",
                    "EUR"
                ]
            )

            biaya_ln = float(st.number_input(
                "Biaya Kuliah per Tahun",
                min_value=1000,
                value=20000,
                step=1000
            ))

            if mata_uang == "USD":

                kurs = float(st.number_input(
                    "Kurs Dollar (Rp)",
                    value=17000
                ))

            else:

                kurs = float(st.number_input(
                    "Kurs Euro (Rp)",
                    value=19000
                ))

            biaya = biaya_ln * kurs

            inflasi = float(st.number_input(
                "Inflasi Pendidikan Global (%)",
                min_value=1.0,
                max_value=25.0,
                value=15.0,
                step=0.5
            ))

        instrumen = st.selectbox(
            "Instrumen Investasi",
            [
                "Tabungan",
                "Deposito",
                "Reksa Dana",
                "Asuransi Pendidikan"
            ]
        )

        # =====================================================
        # RETURN INVESTASI
        # =====================================================

        if instrumen == "Tabungan":
            investasi = 0.03

        elif instrumen == "Deposito":
            investasi = 0.05

        elif instrumen == "Reksa Dana":
            investasi = 0.10

        else:
            investasi = 0.07

    # =====================================================
    # PERHITUNGAN
    # =====================================================

    inflasi_decimal = inflasi / 100

    FV = biaya * (1 + inflasi_decimal) ** tahun

    i_bulanan = investasi / 12

    n = tahun * 12

    # =====================================================
    # ANTI DIVISION ERROR
    # =====================================================

    if i_bulanan > 0 and n > 0:

        PMT = (
            FV * i_bulanan
        ) / ((1 + i_bulanan) ** n - 1)

    else:

        PMT = FV / max(n, 1)

    # =====================================================
    # DASHBOARD
    # =====================================================

    st.divider()

    c1, c2, c3 = st.columns(3)

    with c1:

        st.metric(
            "Biaya Masa Depan",
            f"Rp {float(FV):,.0f}"
        )

    with c2:

        st.metric(
            "Tabungan/Bulan",
            f"Rp {float(PMT):,.0f}"
        )

    with c3:

        st.metric(
            "Return Investasi",
            f"{investasi*100:.1f}%"
        )

    # =====================================================
    # INFORMASI
    # =====================================================

    st.divider()

    st.info(f"""
    Inflasi pendidikan diperkirakan sebesar
    {inflasi:.1f}% per tahun.

    Return investasi dari instrumen {instrumen}
    diperkirakan sebesar {investasi*100:.1f}% per tahun.

    Semakin tinggi inflasi pendidikan,
    semakin besar dana yang harus dipersiapkan.
    """)

    # =====================================================
    # TABEL PROYEKSI
    # =====================================================

    st.divider()

    st.header("📅 Tabel Proyeksi Dana")

    tahun_list = []
    biaya_list = []
    investasi_list = []

    saldo = 0

    for t in range(int(tahun) + 1):

        nilai_biaya = biaya * (
            1 + inflasi_decimal
        ) ** t

        saldo = (
            saldo * (1 + investasi)
            + (PMT * 12)
        )

        tahun_list.append(t)
        biaya_list.append(round(nilai_biaya))
        investasi_list.append(round(saldo))

    df = pd.DataFrame({
        "Tahun": tahun_list,
        "Biaya Pendidikan": biaya_list,
        "Nilai Investasi": investasi_list
    })

    st.dataframe(df, use_container_width=True)

    # =====================================================
    # GRAFIK
    # =====================================================

    st.divider()

    st.header("📈 Grafik Pertumbuhan Dana")

    fig, ax = plt.subplots(figsize=(12,6))

    ax.plot(
        tahun_list,
        biaya_list,
        marker='o',
        linewidth=3,
        label='Biaya Pendidikan'
    )

    ax.plot(
        tahun_list,
        investasi_list,
        marker='s',
        linewidth=3,
        label='Nilai Investasi'
    )

    ax.set_title("Simulasi Dana Pendidikan")

    ax.set_xlabel("Tahun")

    ax.set_ylabel("Nilai (Rp)")

    ax.grid(True)

    ax.legend()

    st.pyplot(fig)

# =========================================================
# ANALISIS RISIKO INFLASI
# =========================================================

elif menu == "📉 Analisis Risiko Inflasi":

    st.title("📉 Analisis Risiko Inflasi")

    biaya = float(st.number_input(
        "Biaya Pendidikan Saat Ini (Rp)",
        value=20000000
    ))

    tahun = int(st.number_input(
        "Jangka Waktu Persiapan",
        value=10
    ))

    tahun_list = list(range(int(tahun) + 1))

    stabil = []
    normal = []
    krisis = []

    for t in tahun_list:

        stabil.append(
            biaya * (1 + 0.05) ** t
        )

        normal.append(
            biaya * (1 + 0.10) ** t
        )

        krisis.append(
            biaya * (1 + 0.15) ** t
        )

    data = pd.DataFrame({
        "Tahun": tahun_list,
        "Stabil (5%)": stabil,
        "Normal (10%)": normal,
        "Krisis (15%)": krisis
    })

    st.dataframe(data, use_container_width=True)

    fig, ax = plt.subplots(figsize=(12,6))

    ax.plot(
        tahun_list,
        stabil,
        marker='o',
        linewidth=3,
        label='Stabil'
    )

    ax.plot(
        tahun_list,
        normal,
        marker='o',
        linewidth=3,
        label='Normal'
    )

    ax.plot(
        tahun_list,
        krisis,
        marker='o',
        linewidth=3,
        label='Krisis'
    )

    ax.set_title("Perbandingan Risiko Inflasi")

    ax.set_xlabel("Tahun")

    ax.set_ylabel("Biaya Pendidikan")

    ax.grid(True)

    ax.legend()

    st.pyplot(fig)

# =========================================================
# KONSULTASI
# =========================================================

elif menu == "💰 Konsultasi":

    st.title("💰 Konsultasi")

    st.subheader("Strategi Dana Pendidikan")

    col1, col2 = st.columns(2)

    with col1:

        target = float(st.number_input(
            "Target Dana Pendidikan (Rp)",
            value=500000000
        ))

        tahun = int(st.number_input(
            "Jangka Waktu Persiapan",
            value=10
        ))

    with col2:

        instrumen = st.selectbox(
            "Instrumen Investasi",
            [
                "Tabungan",
                "Deposito",
                "Reksa Dana",
                "Asuransi Pendidikan"
            ]
        )

        if instrumen == "Tabungan":
            investasi = 0.03
            risiko = "Rendah"

        elif instrumen == "Deposito":
            investasi = 0.05
            risiko = "Rendah"

        elif instrumen == "Reksa Dana":
            investasi = 0.10
            risiko = "Sedang"

        else:
            investasi = 0.07
            risiko = "Rendah"

    i_bulanan = investasi / 12

    n = tahun * 12

    if i_bulanan > 0 and n > 0:

        PMT = (
            target * i_bulanan
        ) / ((1 + i_bulanan) ** n - 1)

    else:

        PMT = target / max(n, 1)

    st.divider()

    c1, c2, c3 = st.columns(3)

    with c1:

        st.metric(
            "Target Dana",
            f"Rp {float(target):,.0f}"
        )

    with c2:

        st.metric(
            "Tabungan/Bulan",
            f"Rp {float(PMT):,.0f}"
        )

    with c3:

        st.metric(
            "Risiko",
            risiko
        )

    st.divider()

    st.header("📊 Analisis Strategi")

    if investasi < 0.05:

        st.error("""
        Return investasi masih rendah
        dan berpotensi kalah terhadap inflasi pendidikan.
        """)

    elif investasi < 0.08:

        st.warning("""
        Investasi cukup stabil,
        namun pertumbuhannya moderat.
        """)

    else:

        st.success("""
        Investasi cukup baik untuk
        perencanaan pendidikan jangka panjang.
        """)

    if PMT > 5000000:

        st.warning("""
        Target dana tergolong besar.

        Disarankan:
        - memperpanjang waktu investasi
        - meningkatkan return investasi
        """)

    elif PMT > 2000000:

        st.info("""
        Target dana masih realistis,
        tetapi membutuhkan disiplin investasi.
        """)

    else:

        st.success("""
        Target dana relatif realistis
        dan lebih mudah dicapai.
        """)

# =====================================================
# EDUKASI FINANSIAL
# =====================================================

elif menu == "📚 Edukasi Finansial":

    st.title("📚 Edukasi Finansial")

    st.markdown("""
    <div class="card">

    ## Apa itu inflasi pendidikan?

    Inflasi pendidikan adalah kenaikan biaya pendidikan
    setiap tahun akibat faktor ekonomi.

    ## Mengapa investasi penting?

    Karena nilai uang dapat menurun akibat inflasi.

    ## Mengapa dana pendidikan harus dipersiapkan?

    Agar keluarga tidak terbebani biaya pendidikan
    di masa depan.

    </div>
    """, unsafe_allow_html=True)

# =====================================================
# TENTANG
# =====================================================

elif menu == "ℹ Tentang Aplikasi":

    st.title("ℹ Tentang EduPlan+")

    st.markdown("""
    <div class="card">

    EduPlan+ merupakan aplikasi simulasi dana pendidikan
    berbasis matematika aktuaria dan nilai waktu uang.

    ### Teknologi:
    - Python
    - Streamlit
    - Pandas
    - Matplotlib

    ### Tujuan:
    Membantu masyarakat memahami pentingnya
    perencanaan dana pendidikan sejak dini.

    </div>
    """, unsafe_allow_html=True)

# =====================================================
# FOOTER
# =====================================================

st.divider()

st.markdown("""
<div class="footer">

EduPlan+ © 2026

</div>
""", unsafe_allow_html=True)
