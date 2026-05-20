import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

st.set_page_config(
    page_title="EduPlan+",
    page_icon="🎓",
    layout="wide"
)

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
        '<p class="sub-title">Smart Education Financial Planner</p>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="card">

    ## 📈 Mengapa EduPlan Dibuat?

    EduPlan dibuat untuk membantu masyarakat memahami:
    - inflasi pendidikan
    - pentingnya investasi
    - perencanaan dana pendidikan

    Biaya pendidikan terus meningkat setiap tahun,
    sedangkan banyak masyarakat belum memahami
    cara mempersiapkan dana pendidikan secara optimal.

    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Inflasi Pendidikan", "10%")

    with col2:
        st.metric("Kenaikan Biaya Kuliah", "2-3x")

    with col3:
        st.metric("Nilai Rupiah", "Melemah")

# =========================================================
# DANA PENDIDIKAN
# =========================================================

elif menu == "🎓 Dana Pendidikan":

    st.title("🎓 Simulasi Dana Pendidikan")

    col1, col2 = st.columns(2)

    with col1:

        jenis_pendidikan = st.selectbox(
            "Jenis Pendidikan",
            [
                "Pendidikan Dalam Negeri",
                "Pendidikan Luar Negeri"
            ]
        )

        tahun = st.number_input(
            "Jangka Waktu Persiapan (Tahun)",
            min_value=1,
            max_value=30,
            value=10
        )

    with col2:

        # =====================================================
        # DALAM NEGERI
        # =====================================================

        if jenis_pendidikan == "Pendidikan Dalam Negeri":

            biaya = st.number_input(
                "Biaya Pendidikan Saat Ini (Rp)",
                min_value=100000,
                value=20000000,
                step=1000000
            )

            inflasi = st.number_input(
                "Inflasi Pendidikan (% per tahun)",
                min_value=1.0,
                max_value=25.0,
                value=10.0,
                step=0.5
            )

        # =====================================================
        # LUAR NEGERI
        # =====================================================

        else:

            mata_uang = st.selectbox(
                "Mata Uang",
                [
                    "USD (Dollar Amerika)",
                    "EUR (Euro)"
                ]
            )

            biaya_ln = st.number_input(
                "Biaya Kuliah per Tahun",
                min_value=1000,
                value=20000,
                step=1000
            )

            if "USD" in mata_uang:

                kurs = st.number_input(
                    "Kurs Dollar (Rp)",
                    value=17000
                )

            else:

                kurs = st.number_input(
                    "Kurs Euro (Rp)",
                    value=19000
                )

            biaya = biaya_ln * kurs

            inflasi = st.number_input(
                "Inflasi Pendidikan Global (% per tahun)",
                min_value=1.0,
                max_value=25.0,
                value=15.0,
                step=0.5
            )

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
    # MENCEGAH ERROR PEMBAGIAN NOL
    # =====================================================

    if i_bulanan > 0:

        PMT = (
            FV * i_bulanan
        ) / ((1 + i_bulanan) ** n - 1)

    else:

        PMT = FV / n

    # =====================================================
    # METRIC
    # =====================================================

    st.divider()

    c1, c2, c3 = st.columns(3)

    with c1:

        st.metric(
            "Biaya Masa Depan",
            f"Rp {FV:,.0f}"
        )

    with c2:

        st.metric(
            "Tabungan per Bulan",
            f"Rp {PMT:,.0f}"
        )

    with c3:

        st.metric(
            "Return Investasi",
            f"{investasi*100:.1f}%"
        )

    # =====================================================
    # PENJELASAN
    # =====================================================

    st.divider()

    st.info(f"""
    Inflasi pendidikan diperkirakan sebesar
    {inflasi:.1f}% per tahun.

    Return investasi dari instrumen {instrumen}
    diperkirakan sebesar {investasi*100:.1f}% per tahun.
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

    for t in range(tahun + 1):

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
        label='Pertumbuhan Investasi'
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

    biaya = st.number_input(
        "Biaya Pendidikan Saat Ini (Rp)",
        value=20000000,
        step=1000000
    )

    tahun = st.number_input(
        "Jangka Waktu Persiapan",
        min_value=1,
        max_value=30,
        value=10
    )

    inflasi_rendah = biaya * (1 + 0.05) ** tahun
    inflasi_sedang = biaya * (1 + 0.10) ** tahun
    inflasi_tinggi = biaya * (1 + 0.15) ** tahun

    data = pd.DataFrame({
        "Kondisi Ekonomi": [
            "Stabil",
            "Normal",
            "Krisis"
        ],
        "Inflasi": [
            "5%",
            "10%",
            "15%"
        ],
        "Biaya Masa Depan": [
            round(inflasi_rendah),
            round(inflasi_sedang),
            round(inflasi_tinggi)
        ]
    })

    st.dataframe(data, use_container_width=True)

    selisih = inflasi_tinggi - inflasi_rendah

    st.error(f"""
    Jika ekonomi memburuk,
    biaya pendidikan dapat meningkat sekitar:

    Rp {selisih:,.0f}
    """)

# =========================================================
# KONSULTASI
# =========================================================

elif menu == "💰 Konsultasi":

    st.title("💰 Konsultasi")

    st.subheader("Strategi Dana Pendidikan")

    col1, col2 = st.columns(2)

    with col1:

        target = st.number_input(
            "Target Dana Pendidikan (Rp)",
            min_value=1000000,
            value=500000000,
            step=10000000
        )

        tahun = st.number_input(
            "Jangka Waktu Persiapan",
            min_value=1,
            max_value=30,
            value=10
        )

    with col2:

        instrumen = st.selectbox(
            "Pilih Instrumen Investasi",
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

    if i_bulanan > 0:

        PMT = (
            target * i_bulanan
        ) / ((1 + i_bulanan) ** n - 1)

    else:

        PMT = target / n

    st.divider()

    c1, c2, c3 = st.columns(3)

    with c1:

        st.metric(
            "Target Dana",
            f"Rp {target:,.0f}"
        )

    with c2:

        st.metric(
            "Tabungan/Bulan",
            f"Rp {PMT:,.0f}"
        )

    with c3:

        st.metric(
            "Risiko Investasi",
            risiko
        )

    st.divider()

    st.header("📊 Analisis Strategi")

    if investasi < 0.05:

        st.error("""
        Instrumen investasi yang dipilih
        cenderung kalah terhadap inflasi pendidikan.
        """)

    elif investasi < 0.08:

        st.warning("""
        Instrumen investasi cukup stabil,
        tetapi pertumbuhannya relatif moderat.
        """)

    else:

        st.success("""
        Instrumen investasi cukup baik
        untuk perencanaan pendidikan jangka panjang.
        """)

# =========================================================
# EDUKASI FINANSIAL
# =========================================================

elif menu == "📚 Edukasi Finansial":

    st.title("📚 Edukasi Finansial")

    st.markdown("""
    <div class="card">

    ## Apa itu inflasi pendidikan?

    Inflasi pendidikan adalah kenaikan biaya pendidikan
    setiap tahun akibat faktor ekonomi dan kenaikan harga.

    ## Mengapa investasi penting?

    Karena nilai uang dapat menurun akibat inflasi.

    ## Mengapa dana pendidikan harus dipersiapkan?

    Agar keluarga tidak terbebani biaya pendidikan
    di masa depan.

    </div>
    """, unsafe_allow_html=True)

# =========================================================
# TENTANG
# =========================================================

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

    </div>
    """, unsafe_allow_html=True)

# =========================================================
# FOOTER
# =========================================================

st.divider()

st.markdown("""
<div class="footer">

EduPlan+ © 2026

</div>
""", unsafe_allow_html=True)
