import streamlit as st
import pandas as pd
import joblib
import os

# Set Konfigurasi Halaman Streamlit
st.set_page_config(
    page_title="Jaya Jaya Institut: Dropout Detection",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load Model
@st.cache_resource
def load_model():
    if os.path.exists('model.pkl'):
        return joblib.load('model.pkl')
    return None

pipeline = load_model()

if not pipeline:
    st.error("⚠️ Model belum ditemukan. Pastikan Anda telah menjalankan `train.py` terlebih dahulu untuk menghasilkan `model.pkl`.")
    st.stop()

scaler = pipeline['scaler']
model = pipeline['model']
expected_features = pipeline['features']

# Header dan Deskripsi
st.title("🎓 Sistem Peringatan Dini: Potensi Mahasiswa Dropout")
st.markdown("""
Selamat datang di **Jaya Jaya Institut Dropout Detection System**. 
Aplikasi ini memanfaatkan algoritma *Machine Learning* untuk mendeteksi potensi **dropout** mahasiswa berdasarkan data akademik dan profil sosial-ekonomi mereka. 
Gunakan panel di sebelah kiri untuk memasukkan profil mahasiswa.
""")

# Sidebar Input
st.sidebar.header("Data Profil Mahasiswa")

# Membagi Sidebar menjadi beberapa kategori logis dengan expander
with st.sidebar.expander("💳 Finansial & Sosial Ekonomi", expanded=True):
    debtor = st.selectbox("Status Debitur (Punya Utang Akademik?)", options=["Tidak", "Ya"])
    tuition = st.selectbox("Apakah Uang Kuliah (SPP) Lunas?", options=["Belum Lunas", "Lunas"])
    scholarship = st.selectbox("Penerima Beasiswa?", options=["Tidak", "Ya"])
    age = st.number_input("Usia saat Mendaftar", min_value=15, max_value=60, value=19)

with st.sidebar.expander("📚 Performa Semester 1"):
    sem1_enrolled = st.number_input("Jumlah SKS Diambil (Sem 1)", min_value=0, max_value=30, value=20)
    sem1_approved = st.number_input("Jumlah SKS Lulus (Sem 1)", min_value=0, max_value=30, value=15)
    sem1_grade = st.number_input("Nilai Rata-rata (Sem 1) [0-14]", min_value=0.0, max_value=14.0, value=12.0)

with st.sidebar.expander("📈 Performa Semester 2"):
    sem2_enrolled = st.number_input("Jumlah SKS Diambil (Sem 2)", min_value=0, max_value=30, value=20)
    sem2_approved = st.number_input("Jumlah SKS Lulus (Sem 2)", min_value=0, max_value=30, value=15)
    sem2_grade = st.number_input("Nilai Rata-rata (Sem 2) [0-14]", min_value=0.0, max_value=14.0, value=12.0)

# Menampung klik prediksi
st.sidebar.markdown("---")
predict_btn = st.sidebar.button("🔍 Deteksi Risiko Dropout", use_container_width=True)

# Main Area / Logic Prediksi
if predict_btn:
    # Memetakan UI ke nilai model
    debtor_val = 1 if debtor == "Ya" else 0
    tuition_val = 1 if tuition == "Lunas" else 0
    scholarship_val = 1 if scholarship == "Ya" else 0
    
    # Feature Engineering
    approved_ratio_1st = sem1_approved / (max(sem1_enrolled, 1e-5))
    approved_ratio_2nd = sem2_approved / (max(sem2_enrolled, 1e-5))
    
    # Clip ke 1.0 maksimal
    approved_ratio_1st = min(approved_ratio_1st, 1.0)
    approved_ratio_2nd = min(approved_ratio_2nd, 1.0)
    
    # Construct expected features
    input_data = {feat: 0 for feat in expected_features}
    
    input_data['Debtor'] = debtor_val
    input_data['Tuition_fees_up_to_date'] = tuition_val
    input_data['Scholarship_holder'] = scholarship_val
    input_data['Age_at_enrollment'] = age
    input_data['Curricular_units_1st_sem_enrolled'] = sem1_enrolled
    input_data['Curricular_units_1st_sem_approved'] = sem1_approved
    input_data['Curricular_units_1st_sem_grade'] = sem1_grade
    input_data['Curricular_units_2nd_sem_enrolled'] = sem2_enrolled
    input_data['Curricular_units_2nd_sem_approved'] = sem2_approved
    input_data['Curricular_units_2nd_sem_grade'] = sem2_grade
    input_data['approved_ratio_1st_sem'] = approved_ratio_1st
    input_data['approved_ratio_2nd_sem'] = approved_ratio_2nd
    
    df_input = pd.DataFrame([input_data])[expected_features]
    X_scaled = scaler.transform(df_input)
    
    # Prediksi Probabilitas
    probability = model.predict_proba(X_scaled)[0]
    dropout_prob = probability[1]
    
    # Logika Threshold Tingkat Risiko
    if dropout_prob > 0.7:
        status_label = "RISIKO TINGGI"
        status_color = "red"
        alert_box = st.error
    elif dropout_prob > 0.4:
        status_label = "RISIKO MENENGAH"
        status_color = "orange"
        alert_box = st.warning
    else:
        status_label = "AMAN"
        status_color = "green"
        alert_box = st.success

    st.markdown("---")
    st.header("Hasil Analisis:")
    
    # Layout Kolom
    col1, col2 = st.columns(2)
    
    with col1:
        st.metric(label="Probabilitas Dropout", value=f"{dropout_prob * 100:.1f} %")
        st.markdown(f"**Tingkat Risiko Dropout:**")
        # Visual Progress Bar
        st.progress(float(dropout_prob))
    
    with col2:
        alert_box(f"🎯 Prediksi Sistem: **{status_label}**")

    st.markdown("---")
    st.subheader("Detail Analisis & Rekomendasi:")
    
    # Ekstraksi Faktor Utama secara Dinamis
    factors = []
    
    if tuition_val == 0:
        factors.append("Tunggakan SPP")
        
    if debtor_val == 1:
        factors.append("Status Debitur")

    if approved_ratio_1st < 0.5 or approved_ratio_2nd < 0.5:
        factors.append("Performa akademik rendah")

    if not factors:
        factors.append("Performa akademik stabil")

    # Tampilkan Faktor
    st.markdown(f"**Indikator Utama Pembentuk Risiko:** {', '.join(factors)}")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Narasi Output Profesional
    if status_label == "AMAN":
        st.info("""
        **Mahasiswa memiliki risiko rendah untuk dropout.**
        
        **Indikator Utama:**
        - Performa akademik stabil
        - Tidak terdapat masalah finansial
        - Tingkat kelulusan mata kuliah tinggi
        
        **Rekomendasi Tindakan:**
        - Lanjutkan monitoring berkala pada setiap akhir semester
        - Berikan apresiasi jika nilai akademik terus meningkat
        """)
    else:
        # Untuk Risiko Menengah dan Tinggi
        st.warning(f"""
        **Mahasiswa memiliki indikasi {status_label.lower()} untuk putus studi.**
        
        **Akar Permasalahan yang Terdeteksi:**
        - {"⚠️ " + ", ".join(factors) if factors[0] != "Performa akademik stabil" else "Performa mulai menurun"}
        
        **Rekomendasi Tindakan:**
        - **Bimbingan & Konseling:** Panggil mahasiswa bersangkutan untuk sesi Bimbingan Konseling / Dosen Wali.
        - **Bantuan Finansial:** Tawarkan skema cicilan SPP / penangguhan pembayaran (jika terdapat kendala finansial).
        - **Academic Recovery:** Pantau ketat progres kehadiran dan nilai tugas harian.
        """)
        
else:
    st.markdown("### 👈 Silakan isi data di panel kiri dan klik **Deteksi Risiko Dropout**")
    
st.markdown("---")
st.caption("Developed by AI Data Scientist. Model: Random Forest | Evaluasi berdasarkan parameter deteksi dini (High Recall).")
