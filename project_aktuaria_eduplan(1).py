import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="FutureFund",
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
        #1E40AF 0%,
        #2563EB 50%,
        #1D4ED8 100%
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

    # =====================================================
    # INPUT
    # =====================================================

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

        instrumen = st.selectbox(
            "Instrumen",
            [
                "Tabungan",
                "Deposito",
                "Reksa Dana",
                "Asuransi Pendidikan"
            ]
        )

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
                "Biaya Pendidikan per Tahun",
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

    nama_instrumen = instrumen
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
            f"{nama_instrumen}/Bulan",
            f"Rp {float(PMT):,.0f}"
        )

    with c3:

        st.metric(
            f"Return {nama_instrumen}",
            f"{investasi*100:.1f}%"
        )

    # =====================================================
    # INFORMASI
    # =====================================================

    st.divider()

    st.info(f"""
    Inflasi pendidikan diperkirakan sebesar
    {inflasi:.1f}% per tahun.

    Return dari instrumen {nama_instrumen}
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

        f"Nilai {nama_instrumen}": investasi_list

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
        label=f'Nilai {nama_instrumen}'
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

    # =====================================================
    # INPUT
    # =====================================================

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
            "Instrumen Keuangan",
            [
                "Tabungan",
                "Deposito",
                "Reksa Dana",
                "Asuransi Pendidikan"
            ]
        )

    # =====================================================
    # RETURN & RISIKO
    # =====================================================

    if instrumen == "Tabungan":

        investasi = 0.03
        risiko = "Rendah"

        nama_bulanan = "Tabungan/Bulan"
        aktivitas = "menabung"

    elif instrumen == "Deposito":

        investasi = 0.05
        risiko = "Rendah"

        nama_bulanan = "Deposito/Bulan"
        aktivitas = "deposito"

    elif instrumen == "Reksa Dana":

        investasi = 0.10
        risiko = "Sedang"

        nama_bulanan = "Investasi Reksa Dana/Bulan"
        aktivitas = "berinvestasi"

    else:

        investasi = 0.07
        risiko = "Rendah"

        nama_bulanan = "Premi Asuransi/Bulan"
        aktivitas = "membayar premi"

    # =====================================================
    # PERHITUNGAN
    # =====================================================

    i_bulanan = investasi / 12

    n = tahun * 12

    if i_bulanan > 0 and n > 0:

        PMT = (
            target * i_bulanan
        ) / ((1 + i_bulanan) ** n - 1)

    else:

        PMT = target / max(n, 1)

    # =====================================================
    # DASHBOARD
    # =====================================================

    st.divider()

    c1, c2, c3 = st.columns(3)

    with c1:

        st.metric(
            "Target Dana",
            f"Rp {float(target):,.0f}"
        )

    with c2:

        st.metric(
            nama_bulanan,
            f"Rp {float(PMT):,.0f}"
        )

    with c3:

        st.metric(
            "Risiko",
            risiko
        )

    # =====================================================
    # ANALISIS STRATEGI
    # =====================================================

    st.divider()

    st.header("📊 Analisis Strategi")

    # =====================================================
    # ANALISIS RETURN
    # =====================================================

    if investasi < 0.05:

        st.error(f"""
        Return dari instrumen {instrumen}
        masih relatif rendah dan berpotensi
        kalah terhadap inflasi pendidikan.
        """)

    elif investasi < 0.08:

        st.warning(f"""
        Instrumen {instrumen}
        cukup stabil untuk perencanaan pendidikan,
        namun pertumbuhannya masih moderat.
        """)

    else:

        st.success(f"""
        Instrumen {instrumen}
        cukup baik untuk perencanaan pendidikan
        jangka panjang.
        """)

    # =====================================================
    # ANALISIS TARGET
    # =====================================================

    if PMT > 5000000:

        st.warning(f"""
        Target dana tergolong besar.

        Disarankan:
        - memperpanjang waktu {aktivitas}
        - meningkatkan return investasi
        - mulai perencanaan lebih dini
        """)

    elif PMT > 2000000:

        st.info(f"""
        Target dana masih realistis,
        namun membutuhkan disiplin dalam {aktivitas}.
        """)

    else:

        st.success(f"""
        Target dana relatif realistis
        dan lebih mudah dicapai melalui strategi {instrumen.lower()}.
        """)

    # =====================================================
    # REKOMENDASI
    # =====================================================

    st.divider()

    st.header("💡 Rekomendasi FutureFund")

    if instrumen == "Tabungan":

        st.info("""
        Cocok untuk:
        - profil risiko rendah
        - jangka pendek
        - pengguna yang mengutamakan keamanan dana
        """)

    elif instrumen == "Deposito":

        st.info("""
        Cocok untuk:
        - dana pendidikan menengah
        - pengguna yang ingin return stabil
        - risiko rendah
        """)

    elif instrumen == "Reksa Dana":

        st.info("""
        Cocok untuk:
        - persiapan pendidikan jangka panjang
        - mengejar inflasi pendidikan
        - pertumbuhan dana yang lebih optimal
        """)

    else:

        st.info("""
        Cocok untuk:
        - perlindungan pendidikan anak
        - perencanaan pendidikan jangka panjang
        - kombinasi proteksi dan investasi
        """)
        
# =====================================================
# EDUKASI FINANSIAL
# =====================================================

elif menu == "📚 Edukasi Finansial":

    st.title("📚 Edukasi Finansial")

    # =====================================================
    # INFLASI PENDIDIKAN
    # =====================================================

    st.markdown("""
    <div class="card">

    <h1>📌 Apa itu Inflasi Pendidikan?</h1>

    <p style='font-size:18px'>
    Inflasi pendidikan adalah kenaikan biaya pendidikan
    dari tahun ke tahun akibat peningkatan biaya operasional,
    fasilitas sekolah, teknologi pendidikan,
    biaya tenaga pengajar,
    serta kondisi ekonomi global.
    </p>

    <p style='font-size:18px'>
    Inflasi pendidikan umumnya lebih tinggi dibandingkan
    inflasi biasa karena sektor pendidikan terus berkembang
    dan membutuhkan fasilitas yang semakin modern.
    </p>

    <p style='font-size:18px'>
    Sebagai contoh,
    biaya kuliah Rp20 juta saat ini
    dapat meningkat menjadi lebih dari Rp50 juta
    dalam 10 tahun apabila inflasi pendidikan mencapai 10% per tahun.
    </p>

    <p style='font-size:16px; color:gray'>
    Sumber:
    BPS, OJK, Bank Indonesia, CNBC Indonesia
    </p>

    </div>
    """, unsafe_allow_html=True)

    # =====================================================
    # PENTINGNYA PERENCANAAN
    # =====================================================

    st.markdown("""
    <div class="card">

    <h1>🎓 Mengapa Dana Pendidikan Harus Dipersiapkan?</h1>

    <p style='font-size:18px'>
    Pendidikan merupakan kebutuhan jangka panjang
    yang membutuhkan biaya besar.
    Tanpa perencanaan yang baik,
    keluarga dapat mengalami kesulitan finansial
    akibat kenaikan biaya pendidikan di masa depan.
    </p>

    <h2>📌 Manfaat Perencanaan Dana Pendidikan:</h2>

    <ul style='font-size:18px; line-height:2'>
        <li>✔ Mengurangi risiko kekurangan dana pendidikan</li>
        <li>✔ Menghindari utang pendidikan</li>
        <li>✔ Membantu mencapai pendidikan berkualitas</li>
        <li>✔ Memberikan rasa aman finansial keluarga</li>
        <li>✔ Membantu menghadapi inflasi pendidikan</li>
    </ul>

    </div>
    """, unsafe_allow_html=True)

    # =====================================================
    # TABUNGAN
    # =====================================================

    st.markdown("""
    <div class="card">

    <h1>🏦 Tabungan</h1>

    <p style='font-size:18px'>
    Tabungan merupakan produk perbankan
    untuk menyimpan uang dengan tingkat risiko sangat rendah.
    </p>

    <h2>✅ Kelebihan Tabungan</h2>

    <ul style='font-size:18px; line-height:2'>
        <li>✔ Risiko sangat rendah</li>
        <li>✔ Dana mudah dicairkan</li>
        <li>✔ Cocok untuk dana darurat</li>
        <li>✔ Aman dan mudah dipahami masyarakat umum</li>
    </ul>

    <h2>❌ Kekurangan Tabungan</h2>

    <ul style='font-size:18px; line-height:2'>
        <li>✖ Return relatif kecil</li>
        <li>✖ Sering kalah terhadap inflasi pendidikan</li>
        <li>✖ Pertumbuhan dana lambat</li>
    </ul>

    <h2>🎯 Cocok Untuk</h2>

    <p style='font-size:18px'>
    Jangka pendek dan pengguna dengan profil risiko rendah.
    </p>

    <p style='font-size:16px; color:gray'>
    Return rata-rata: 2% - 3% per tahun
    </p>

    </div>
    """, unsafe_allow_html=True)

    # =====================================================
    # DEPOSITO
    # =====================================================

    st.markdown("""
    <div class="card">

    <h1>🏛 Deposito</h1>

    <p style='font-size:18px'>
    Deposito adalah simpanan berjangka
    dengan bunga lebih tinggi dibandingkan tabungan.
    Dana disimpan dalam periode tertentu
    sesuai kesepakatan dengan bank.
    </p>

    <h2>✅ Kelebihan Deposito</h2>

    <ul style='font-size:18px; line-height:2'>
        <li>✔ Return lebih tinggi dari tabungan</li>
        <li>✔ Risiko rendah</li>
        <li>✔ Cocok untuk dana pendidikan menengah</li>
        <li>✔ Stabil dan aman</li>
    </ul>

    <h2>❌ Kekurangan Deposito</h2>

    <ul style='font-size:18px; line-height:2'>
        <li>✖ Dana tidak fleksibel</li>
        <li>✖ Ada penalti jika dicairkan lebih awal</li>
        <li>✖ Return masih dapat kalah terhadap inflasi tinggi</li>
    </ul>

    <h2>🎯 Cocok Untuk</h2>

    <p style='font-size:18px'>
    Pengguna dengan profil risiko rendah
    dan target pendidikan jangka menengah.
    </p>

    <p style='font-size:16px; color:gray'>
    Return rata-rata: 4% - 6% per tahun
    </p>

    </div>
    """, unsafe_allow_html=True)

    # =====================================================
    # REKSA DANA
    # =====================================================

    st.markdown("""
    <div class="card">

    <h1>📈 Reksa Dana</h1>

    <p style='font-size:18px'>
    Reksa dana adalah instrumen investasi
    yang dikelola oleh manajer investasi
    untuk mengembangkan dana investor.
    </p>

    <h2>✅ Kelebihan Reksa Dana</h2>

    <ul style='font-size:18px; line-height:2'>
        <li>✔ Potensi return lebih tinggi</li>
        <li>✔ Cocok untuk melawan inflasi pendidikan</li>
        <li>✔ Dikelola profesional</li>
        <li>✔ Cocok untuk jangka panjang</li>
    </ul>

    <h2>❌ Kekurangan Reksa Dana</h2>

    <ul style='font-size:18px; line-height:2'>
        <li>✖ Nilai investasi dapat naik turun</li>
        <li>✖ Memiliki risiko pasar</li>
        <li>✖ Membutuhkan pemahaman investasi</li>
    </ul>

    <h2>🎯 Cocok Untuk</h2>

    <p style='font-size:18px'>
    Perencanaan pendidikan jangka panjang
    dan pengguna dengan profil risiko menengah.
    </p>

    <p style='font-size:16px; color:gray'>
    Return rata-rata: 8% - 12% per tahun
    </p>

    </div>
    """, unsafe_allow_html=True)

    # =====================================================
    # ASURANSI PENDIDIKAN
    # =====================================================

    st.markdown("""
    <div class="card">

    <h1>🛡 Asuransi Pendidikan</h1>

    <p style='font-size:18px'>
    Asuransi pendidikan merupakan produk keuangan
    yang menggabungkan perlindungan jiwa
    dan dana pendidikan anak di masa depan.
    </p>

    <h2>✅ Kelebihan Asuransi Pendidikan</h2>

    <ul style='font-size:18px; line-height:2'>
        <li>✔ Memberikan perlindungan finansial</li>
        <li>✔ Dana pendidikan lebih terencana</li>
        <li>✔ Cocok untuk jangka panjang</li>
        <li>✔ Memberikan manfaat proteksi keluarga</li>
    </ul>

    <h2>❌ Kekurangan Asuransi Pendidikan</h2>

    <ul style='font-size:18px; line-height:2'>
        <li>✖ Premi relatif lebih besar</li>
        <li>✖ Return tidak setinggi reksa dana</li>
        <li>✖ Kurang fleksibel dibanding investasi biasa</li>
    </ul>

    <h2>🎯 Cocok Untuk</h2>

    <p style='font-size:18px'>
    Orang tua yang menginginkan
    perlindungan sekaligus dana pendidikan.
    </p>

    <p style='font-size:16px; color:gray'>
    Return rata-rata: 5% - 8% per tahun
    </p>

    </div>
    """, unsafe_allow_html=True)

    # =====================================================
    # PERBANDINGAN
    # =====================================================

    st.markdown("""
    <div class="card">

    <h1>⚖ Perbandingan Instrumen Keuangan</h1>

    <table style='width:100%; font-size:18px'>

    <tr>
        <th>Instrumen</th>
        <th>Risiko</th>
        <th>Return</th>
        <th>Likuiditas</th>
        <th>Cocok Untuk</th>
    </tr>

    <tr>
        <td>Tabungan</td>
        <td>Rendah</td>
        <td>2%-3%</td>
        <td>Tinggi</td>
        <td>Jangka Pendek</td>
    </tr>

    <tr>
        <td>Deposito</td>
        <td>Rendah</td>
        <td>4%-6%</td>
        <td>Sedang</td>
        <td>Jangka Menengah</td>
    </tr>

    <tr>
        <td>Reksa Dana</td>
        <td>Sedang</td>
        <td>8%-12%</td>
        <td>Tinggi</td>
        <td>Jangka Panjang</td>
    </tr>

    <tr>
        <td>Asuransi Pendidikan</td>
        <td>Rendah-Sedang</td>
        <td>5%-8%</td>
        <td>Rendah</td>
        <td>Proteksi + Pendidikan</td>
    </tr>

    </table>

    </div>
    """, unsafe_allow_html=True)

    # =====================================================
    # TIME VALUE OF MONEY
    # =====================================================

    st.markdown("""
    <div class="card">

    <h1>📈 Apa itu Time Value of Money?</h1>

    <p style='font-size:18px'>
    Time Value of Money (TVM)
    adalah konsep bahwa uang saat ini
    lebih berharga dibandingkan uang di masa depan
    karena uang dapat diinvestasikan
    dan menghasilkan keuntungan.
    </p>

    <p style='font-size:18px'>
    Konsep ini digunakan dalam:
    </p>

    <ul style='font-size:18px; line-height:2'>
        <li>✔ Perencanaan dana pendidikan</li>
        <li>✔ Future Value</li>
        <li>✔ Present Value</li>
        <li>✔ Anuitas</li>
        <li>✔ Investasi jangka panjang</li>
    </ul>

    <p style='font-size:16px; color:gray'>
    Sumber:
    Ross, Westerfield & Jordan
    (Fundamentals of Corporate Finance)
    </p>

    </div>
    """, unsafe_allow_html=True)

    # =====================================================
    # KULIAH LUAR NEGERI
    # =====================================================

    st.markdown("""
    <div class="card">

    <h1>🌍 Dana Pendidikan Luar Negeri</h1>

    <p style='font-size:18px'>
    Kuliah di luar negeri membutuhkan perencanaan finansial
    yang lebih kompleks karena dipengaruhi:
    </p>

    <ul style='font-size:18px; line-height:2'>
        <li>✔ Kurs dollar dan euro</li>
        <li>✔ Inflasi global</li>
        <li>✔ Biaya hidup internasional</li>
        <li>✔ Kenaikan tuition fee universitas</li>
    </ul>

    <p style='font-size:18px'>
    Ketika nilai rupiah melemah,
    maka biaya pendidikan ke luar negeri
    akan menjadi lebih mahal.
    </p>

    <p style='font-size:18px'>
    Oleh karena itu,
    perencanaan dana pendidikan luar negeri
    perlu dilakukan lebih awal.
    </p>

    <p style='font-size:16px; color:gray'>
    Sumber:
    Bank Indonesia,
    QS World University Rankings,
    dan data kurs internasional.
    </p>

    </div>
    """, unsafe_allow_html=True)

    # =====================================================
    # PENUTUP
    # =====================================================

    st.markdown("""
    <div style="
        background: linear-gradient(
            135deg,
            #1E3A8A 0%,
            #2563EB 100%
        );
        padding:40px;
        border-radius:20px;
        color:white;
        text-align:center;
        margin-top:20px;
    ">

    <h1>💡 FutureFund</h1>

    <p style='font-size:22px'>
    “Plan Education, Secure the Future”
    </p>

    <p style='font-size:18px'>
    FutureFund hadir untuk membantu masyarakat
    memahami pentingnya perencanaan dana pendidikan
    sejak dini melalui edukasi finansial,
    simulasi aktuaria,
    dan strategi investasi pendidikan.
    </p>

    </div>
    """, unsafe_allow_html=True)
# =====================================================
# TENTANG APLIKASI
# =====================================================

elif menu == "ℹ Tentang Aplikasi":

    st.markdown("""
    <div style="
        background: linear-gradient(
            135deg,
            #1E3A8A 0%,
            #2563EB 100%
        );
        padding:50px;
        border-radius:25px;
        color:white;
        text-align:center;
        margin-bottom:30px;
    ">

    <h1 style="
        font-size:60px;
        font-weight:800;
    ">
    🎓 FutureFund
    </h1>

    <p style="
        font-size:28px;
        margin-top:10px;
    ">
    Smart Education Financial Planner
    </p>

    <p style="
        font-size:20px;
        line-height:1.8;
        margin-top:20px;
    ">
    FutureFund membantu masyarakat
    merencanakan dana pendidikan
    secara lebih mudah,
    modern,
    dan realistis.
    </p>

    </div>
    """, unsafe_allow_html=True)

    # =====================================================
    # TENTANG
    # =====================================================

    st.markdown("""
    <div class="card">

    <h1>📌 Tentang FutureFund</h1>

    <p style='font-size:18px'>
    FutureFund merupakan aplikasi simulasi
    dana pendidikan berbasis matematika aktuaria,
    inflasi pendidikan,
    dan konsep nilai waktu uang.
    </p>

    <p style='font-size:18px'>
    Platform ini dibuat untuk membantu masyarakat
    memahami pentingnya persiapan dana pendidikan
    sejak dini.
    </p>

    <p style='font-size:18px'>
    Dengan FutureFund,
    pengguna dapat memperkirakan
    biaya pendidikan masa depan,
    menghitung target dana,
    serta memahami strategi investasi pendidikan.
    </p>

    </div>
    """, unsafe_allow_html=True)

    # =====================================================
    # FOOTER
    # =====================================================

    st.markdown("""
    <div style="
        text-align:center;
        padding:30px;
        color:gray;
    ">

    <h2>
    “Plan Education, Secure the Future”
    </h2>

# =====================================================
# FOOTER
# =====================================================

st.divider()

st.markdown("""
<div class="footer">

FutureFund © 2026

</div>
""", unsafe_allow_html=True)
