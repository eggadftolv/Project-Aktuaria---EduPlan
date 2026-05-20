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

st.sidebar.title("🎓FutureFund")

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

# =====================================================
# HOME
# =====================================================

if menu == "🏠 Home":

    # =================================================
    # HERO SECTION
    # =================================================

    st.markdown("""
    <div style="
        background: linear-gradient(
            135deg,
            #1E3A8A 0%,
            #2563EB 100%
        );
        padding: 50px;
        border-radius: 25px;
        color: white;
        margin-bottom: 30px;
        box-shadow: 0px 8px 24px rgba(0,0,0,0.15);
    ">

    <h1 style="
        font-size:60px;
        font-weight:800;
        margin-bottom:10px;
    ">
    🎓 FutureFund
    </h1>

    <p style="
        font-size:28px;
        margin-bottom:20px;
    ">
    “Plan Education, Secure the Future”
    </p>

    <p style="
        font-size:20px;
        line-height:1.8;
    ">
    FutureFund membantu masyarakat memahami inflasi pendidikan, investasi, serta perencanaan dana pendidikan 
    secara modern, mudah, dan realistis.
    </p>

    </div>
    """, unsafe_allow_html=True)

    # =================================================
    # QUICK INFORMATION
    # =================================================

    st.markdown("## 📊 Kondisi Pendidikan Saat Ini")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "Inflasi Pendidikan",
            "10%",
            "+ setiap tahun"
        )

    with col2:

        st.metric(
            "Kenaikan Biaya Pendidikan",
            "2-3x",
            "dalam 10 tahun"
        )

    with col3:

        st.metric(
            "Nilai Rupiah",
            "Melemah",
            "terhadap USD & EUR"
        )

    st.divider()

    # =================================================
    # Tujuan FutureFund
    # =================================================

    st.markdown("""
    <div class="card">

    <h1>📈 Mengapa FutureFund Dibuat?</h1>

    <p style='font-size:19px'>
    Biaya pendidikan terus meningkat setiap tahun, sementara banyak masyarakat belum memahami
    pentingnya perencanaan dana pendidikan.
    </p>

    <p style='font-size:19px'>
    FutureFund hadir sebagai solusi digital berbasis matematika aktuaria dan nilai waktu uang
    untuk membantu masyarakat mempersiapkan dana pendidikan secara terstruktur.
    </p>

    <hr>

    <h2>🎯 FutureFund Membantu Pengguna:</h2>

    <ul style='font-size:18px; line-height:2'>
        <li>✔ Menghitung biaya pendidikan masa depan</li>
        <li>✔ Memahami dampak inflasi pendidikan</li>
        <li>✔ Menentukan target tabungan bulanan</li>
        <li>✔ Memilih strategi investasi pendidikan</li>
        <li>✔ Memahami risiko ekonomi dan inflasi</li>
    </ul>

    </div>
    """, unsafe_allow_html=True)

    # =================================================
    # FITUR
    # =================================================

    st.markdown("## 🚀 Fitur Utama FutureFund")

    col1, col2 = st.columns(2)

    with col1:

        st.markdown("""
        <div class="card">

        <h2>🎓 Simulasi Dana Pendidikan</h2>

        <p style='font-size:18px'>
        Menghitung estimasi biaya pendidikan masa depan berdasarkan inflasi dan investasi.
        </p>

        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="card">

        <h2>📉 Analisis Risiko Inflasi</h2>

        <p style='font-size:18px'>
        Membandingkan dampak inflasi stabil, normal, dan krisis ekonomi
        terhadap biaya pendidikan.
        </p>

        </div>
        """, unsafe_allow_html=True)

    with col2:

        st.markdown("""
        <div class="card">

        <h2>💰 Konsultasi Strategi Pendidikan</h2>

        <p style='font-size:18px'>
        Memberikan rekomendasi investasi, estimasi tabungan, 
        dan strategi pendidikan terbaik.
        </p>

        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="card">

        <h2>📚 Edukasi Finansial</h2>

        <p style='font-size:18px'>
        Membantu pengguna memahami:
        inflasi pendidikan,
        investasi,
        dan nilai waktu uang.
        </p>

        </div>
        """, unsafe_allow_html=True)

    # =================================================
    # ILUSTRASI MASALAH
    # =================================================

    st.divider()

    st.markdown("""
    <div class="card">

    <h1>⚠ Mengapa Harus Mempersiapkan Dana Pendidikan Sejak Dini?</h1>

    <p style='font-size:18px'>
    Jika biaya kuliah saat ini sebesar:
    </p>

    <h2 style='color:#2563EB'>
    Rp20.000.000
    </h2>

    <p style='font-size:18px'>
    dengan inflasi pendidikan sekitar:
    </p>

    <h2 style='color:#DC2626'>
    10% per tahun
    </h2>

    <p style='font-size:18px'>
    maka dalam 10 tahun,
    biaya tersebut dapat meningkat menjadi:
    </p>

    <h1 style='color:#16A34A'>
    Rp51.874.849
    </h1>

    <p style='font-size:18px'>
    Oleh karena itu,
    perencanaan dana pendidikan sangat penting
    untuk mengurangi risiko finansial di masa depan.
    </p>

    </div>
    """, unsafe_allow_html=True)

    # =================================================
    # QUOTE
    # =================================================

    st.markdown("""
    <div style="
        background:#1E293B;
        padding:35px;
        border-radius:20px;
        color:white;
        text-align:center;
        margin-top:20px;
    ">

    <h2 style='font-size:34px'>
    “Pendidikan adalah investasi terbaik
    untuk masa depan.”
    </h2>

    <p style='font-size:18px; color:#CBD5E1'>
    — FutureFund
    </p>

    </div>
    """, unsafe_allow_html=True)
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
                    value=17695
                ))

            else:

                kurs = float(st.number_input(
                    "Kurs Euro (Rp)",
                    value=20535
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

    <h2>📌 Apa itu inflasi pendidikan?</h2>

    <p style='font-size:18px'>
    Inflasi pendidikan adalah kenaikan biaya pendidikan
    dari tahun ke tahun akibat peningkatan biaya operasional,
    fasilitas sekolah, teknologi pendidikan, serta kondisi ekonomi global.
    </p>

    <p style='font-size:18px'>
    Biaya pendidikan umumnya meningkat lebih cepat dibandingkan
    inflasi biasa. Oleh karena itu, orang tua perlu
    mempersiapkan dana pendidikan sejak dini.
    </p>

    <p style='font-size:16px; color:gray'>
    Sumber:
    Badan Pusat Statistik (BPS),
    Otoritas Jasa Keuangan (OJK),
    dan Bank Indonesia.
    </p>

    <hr>

    <h2>💰 Mengapa investasi penting?</h2>

    <p style='font-size:18px'>
    Nilai uang dapat menurun akibat inflasi.
    Jika uang hanya disimpan tanpa investasi,
    maka daya beli uang akan semakin berkurang di masa depan.
    </p>

    <p style='font-size:18px'>
    Investasi membantu pertumbuhan dana agar
    dapat mengejar kenaikan biaya pendidikan.
    </p>

    <p style='font-size:18px'>
    Contohnya:
    jika inflasi pendidikan mencapai 10% per tahun,
    maka biaya kuliah Rp20 juta saat ini
    dapat menjadi lebih dari Rp50 juta dalam 10 tahun.
    </p>

    <p style='font-size:16px; color:gray'>
    Sumber:
    Otoritas Jasa Keuangan (OJK),
    Bank Indonesia,
    dan CNBC Indonesia.
    </p>

    <hr>

    <h2>🎓 Mengapa dana pendidikan harus dipersiapkan?</h2>

    <p style='font-size:18px'>
    Pendidikan merupakan kebutuhan jangka panjang
    yang membutuhkan biaya besar.
    Tanpa perencanaan yang baik,
    keluarga dapat mengalami kesulitan finansial
    ketika biaya pendidikan meningkat drastis.
    </p>

    <p style='font-size:18px'>
    Perencanaan dana pendidikan membantu:
    </p>

    <ul style='font-size:18px'>
        <li>Mengurangi risiko kekurangan dana pendidikan</li>
        <li>Menghindari utang pendidikan</li>
        <li>Meningkatkan kesiapan finansial keluarga</li>
        <li>Memberikan rasa aman terhadap masa depan anak</li>
    </ul>

    <p style='font-size:16px; color:gray'>
    Sumber:
    OJK, Bank Indonesia, dan Kementerian Pendidikan Indonesia.
    </p>

    <hr>

    <h2>📈 Apa itu nilai waktu uang (Time Value of Money)?</h2>

    <p style='font-size:18px'>
    Konsep nilai waktu uang menjelaskan bahwa
    uang saat ini lebih berharga dibandingkan
    uang di masa depan karena uang dapat diinvestasikan
    dan menghasilkan keuntungan.
    </p>

    <p style='font-size:18px'>
    Dalam matematika aktuaria,
    konsep ini digunakan untuk menghitung:
    </p>

    <ul style='font-size:18px'>
        <li>Future Value (Nilai Masa Depan)</li>
        <li>Present Value (Nilai Sekarang)</li>
        <li>Anuitas</li>
        <li>Perencanaan investasi pendidikan</li>
    </ul>

    <p style='font-size:16px; color:gray'>
    Sumber:
    Ross, Westerfield & Jordan (Fundamentals of Corporate Finance),
    serta literatur Matematika Keuangan dan Aktuaria.
    </p>

    <hr>

    <h2>🌍 Mengapa kurs dollar dan euro penting untuk kuliah luar negeri?</h2>

    <p style='font-size:18px'>
    Biaya pendidikan luar negeri dipengaruhi
    oleh nilai tukar mata uang asing seperti
    Dollar Amerika (USD) dan Euro (EUR).
    </p>

    <p style='font-size:18px'>
    Ketika nilai rupiah melemah,
    maka biaya kuliah luar negeri menjadi lebih mahal.
    Oleh karena itu,
    perencanaan dana pendidikan luar negeri
    harus mempertimbangkan risiko perubahan kurs.
    </p>

    <p style='font-size:16px; color:gray'>
    Sumber:
    Bank Indonesia dan data kurs internasional.
    </p>

    </div>
    """, unsafe_allow_html=True)

# =====================================================
# TENTANG APLIKASI
# =====================================================

elif menu == "ℹ Tentang Aplikasi":

    st.title("ℹ Tentang EduPlan+")

    st.markdown("""
    <div class="card">

    <h2>🎓 Apa itu EduPlan+?</h2>

    <p style='font-size:18px'>
    EduPlan+ adalah aplikasi simulasi dan perencanaan
    dana pendidikan berbasis matematika aktuaria,
    inflasi pendidikan, dan konsep nilai waktu uang
    (Time Value of Money).
    </p>

    <p style='font-size:18px'>
    Aplikasi ini dirancang untuk membantu masyarakat,
    khususnya orang tua dan mahasiswa,
    dalam memahami pentingnya persiapan dana pendidikan
    sejak dini.
    </p>

    <p style='font-size:18px'>
    Di tengah kondisi ekonomi yang tidak stabil,
    kenaikan inflasi pendidikan,
    serta melemahnya nilai rupiah terhadap dollar dan euro,
    perencanaan dana pendidikan menjadi semakin penting.
    </p>

    </div>
    """, unsafe_allow_html=True)

    # =====================================================
    # VISI MISI
    # =====================================================

    st.markdown("""
    <div class="card">

    <h2>🚀 Visi EduPlan+</h2>

    <p style='font-size:18px'>
    Menjadi aplikasi edukasi dan simulasi keuangan pendidikan
    yang membantu masyarakat memahami pentingnya
    perencanaan dana pendidikan secara mudah,
    modern, dan berbasis ilmu aktuaria.
    </p>

    <hr>

    <h2>🎯 Misi EduPlan+</h2>

    <ul style='font-size:18px'>
        <li>Meningkatkan literasi finansial masyarakat</li>
        <li>Membantu keluarga merencanakan dana pendidikan</li>
        <li>Memberikan simulasi inflasi pendidikan secara realistis</li>
        <li>Mengintegrasikan konsep aktuaria dalam kehidupan sehari-hari</li>
        <li>Membantu pengguna mengambil keputusan finansial yang lebih baik</li>
    </ul>

    </div>
    """, unsafe_allow_html=True)

    # =====================================================
    # FITUR
    # =====================================================

    st.markdown("""
    <div class="card">

    <h2>✨ Fitur Utama EduPlan+</h2>

    <h3>🎓 Simulasi Dana Pendidikan</h3>

    <p style='font-size:18px'>
    Menghitung estimasi biaya pendidikan masa depan
    berdasarkan inflasi pendidikan dan jangka waktu persiapan.
    </p>

    <hr>

    <h3>📉 Analisis Risiko Inflasi</h3>

    <p style='font-size:18px'>
    Membantu pengguna memahami dampak inflasi
    terhadap kenaikan biaya pendidikan di masa depan.
    </p>

    <hr>

    <h3>💰 Konsultasi Strategi Pendidikan</h3>

    <p style='font-size:18px'>
    Memberikan rekomendasi strategi investasi
    dan estimasi tabungan bulanan
    berdasarkan target dana pendidikan pengguna.
    </p>

    <hr>

    <h3>🌍 Simulasi Kuliah Luar Negeri</h3>

    <p style='font-size:18px'>
    Menghitung estimasi biaya pendidikan luar negeri
    dengan mempertimbangkan kurs dollar dan euro.
    </p>

    <hr>

    <h3>📚 Edukasi Finansial</h3>

    <p style='font-size:18px'>
    Memberikan edukasi mengenai:
    inflasi pendidikan,
    investasi,
    nilai waktu uang,
    dan pentingnya perencanaan keuangan.
    </p>

    </div>
    """, unsafe_allow_html=True)

    # =====================================================
    # KEUNGGULAN
    # =====================================================

    st.markdown("""
    <div class="card">

    <h2>🌟 Keunggulan EduPlan+</h2>

    <ul style='font-size:18px'>
        <li>✔ Mudah digunakan oleh masyarakat umum</li>
        <li>✔ Menggunakan konsep matematika aktuaria</li>
        <li>✔ Simulasi realistis berbasis inflasi pendidikan</li>
        <li>✔ Tampilan modern dan interaktif</li>
        <li>✔ Mendukung perencanaan pendidikan luar negeri</li>
        <li>✔ Membantu meningkatkan literasi finansial</li>
    </ul>

    </div>
    """, unsafe_allow_html=True)

    # =====================================================
    # TEKNOLOGI
    # =====================================================

    st.markdown("""
    <div class="card">

    <h2>🛠 Teknologi yang Digunakan</h2>

    <ul style='font-size:18px'>
        <li>Python</li>
        <li>Streamlit</li>
        <li>Pandas</li>
        <li>Matplotlib</li>
    </ul>

    </div>
    """, unsafe_allow_html=True)

    # =====================================================
    # PENUTUP
    # =====================================================

    st.markdown("""
    <div class="card">

    <h2>💡 EduPlan+ untuk Masa Depan Pendidikan</h2>

    <p style='font-size:18px'>
    EduPlan+ hadir bukan hanya sebagai aplikasi simulasi,
    tetapi juga sebagai sarana edukasi finansial
    agar masyarakat lebih siap menghadapi
    kenaikan biaya pendidikan di masa depan.
    </p>

    <p style='font-size:18px'>
    Dengan perencanaan yang baik,
    pendidikan berkualitas dapat dipersiapkan
    sejak dini secara lebih terukur dan realistis.
    </p>

    <hr>

    <p style='font-size:16px; color:gray'>
    EduPlan+ © 2026
    <br>
    Smart Education Financial Planner
    </p>

    </div>
    """, unsafe_allow_html=True)

# =====================================================
# FOOTER
# =====================================================

st.divider()

st.markdown("""
<div class="footer">

FutureFund © 2026

</div>
""", unsafe_allow_html=True)
