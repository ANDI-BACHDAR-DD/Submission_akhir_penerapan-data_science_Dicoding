# Proyek Akhir: Menyelesaikan Permasalahan Institusi Pendidikan

## Business Understanding

### Latar Belakang Masalah

Jaya Jaya Institut merupakan salah satu institusi pendidikan tinggi yang telah berdiri sejak tahun 2000 dan telah mencetak ribuan lulusan dengan reputasi yang baik. Namun dalam beberapa tahun terakhir, institusi ini menghadapi tantangan serius berupa tingginya angka mahasiswa yang tidak menyelesaikan pendidikan mereka alias **dropout**.

Tingkat dropout yang tinggi membawa dampak multidimensional bagi institusi. Dari sisi akreditasi, angka dropout yang tinggi menjadi indikator negatif dalam penilaian akreditasi perguruan tinggi dan berpotensi menurunkan peringkat serta kepercayaan masyarakat. Dari sisi reputasi, calon mahasiswa dan orang tua cenderung memilih institusi dengan tingkat kelulusan tinggi sehingga tingginya dropout merusak citra Jaya Jaya Institut. Dari sisi finansial, setiap mahasiswa yang dropout berarti kehilangan potensi pendapatan jangka panjang dan investasi fasilitas yang tidak optimal. Dari sisi operasional, tingginya angka dropout mempersulit perencanaan kapasitas kelas, alokasi dosen, dan pengelolaan fasilitas kampus.

Berdasarkan data yang dimiliki, sekitar **32.1%** mahasiswa Jaya Jaya Institut tidak menyelesaikan studi mereka — hampir 1 dari 3 mahasiswa. Selama ini pendekatan yang dilakukan cenderung **reaktif**, sehingga dibutuhkan sistem prediksi berbasis **Machine Learning** yang mampu mendeteksi mahasiswa berpotensi dropout sejak dini dan memberikan rekomendasi intervensi yang dapat ditindaklanjuti oleh pihak akademik.

### Permasalahan Bisnis

1. Bagaimana memprediksi apakah seorang mahasiswa akan **Dropout atau Graduate** berdasarkan data akademik dan non-akademik yang tersedia, sehingga institusi dapat melakukan intervensi lebih awal sebelum mahasiswa benar-benar dropout?
2. Faktor-faktor apa saja yang paling signifikan memengaruhi risiko dropout mahasiswa di Jaya Jaya Institut?
3. Bagaimana membangun sistem early warning yang dapat diakses oleh tim akademik untuk memantau mahasiswa berisiko secara real-time?

### Cakupan Proyek

| Area | Deskripsi |
|------|-----------|
| **Analisis Data (EDA)** | Eksplorasi mendalam terhadap 4.424 data mahasiswa untuk menemukan pola distribusi, tren, korelasi, dan faktor penyebab dropout |
| **Business Dashboard** | Visualisasi interaktif menggunakan Looker Studio untuk monitoring status mahasiswa dan faktor risiko dropout |
| **Machine Learning** | Pembangunan model prediksi Dropout vs Graduate menggunakan Logistic Regression dan Random Forest (data Enrolled dieksklusi dari training) |
| **Deployment** | Prototype sistem prediksi berbasis Streamlit untuk tim akademik |

### Persiapan

Sumber data:
```
https://raw.githubusercontent.com/dicodingacademy/dicoding_dataset/main/students_performance/data.csv
```

Setup environment:
```bash
# Clone repository
git clone https://github.com/ANDI-BACHDAR-DD/Submission_akhir_penerapan-data_science_Dicoding.git
cd Submission_akhir_penerapan-data_science_Dicoding

# Buat dan aktifkan virtual environment
python -m venv venv
source venv/bin/activate  # Mac/Linux

# Install dependencies
pip install -r requirements.txt

# Jalankan prototype Streamlit
streamlit run app.py
```

## Business Dashboard

Dashboard bisnis dibuat menggunakan **Looker Studio** untuk memberikan gambaran menyeluruh kepada manajemen akademik dan tim konselor Jaya Jaya Institut.

Dashboard menampilkan visualisasi:
- **Distribusi Status Mahasiswa** — proporsi Graduate (49.9%), Dropout (32.1%), dan Enrolled (17.9%)
- **Performa Akademik vs Status** — mahasiswa dengan nilai akademik rendah cenderung berisiko dropout lebih tinggi
- **SKS Lulus vs Status** — mahasiswa dengan jumlah SKS yang disetujui rendah memiliki kecenderungan dropout lebih tinggi
- **Finansial vs Dropout** — mahasiswa yang tidak melunasi biaya kuliah memiliki tingkat dropout jauh lebih tinggi

🔗 **Link Dashboard:** https://lookerstudio.google.com/reporting/97c68282-4d17-454c-84fc-eb81f64408b7

## Menjalankan Sistem Machine Learning

Sistem prediksi dropout dibangun menggunakan **Streamlit**. Model dilatih hanya menggunakan data mahasiswa dengan status **Dropout dan Graduate**. Data Enrolled digunakan untuk inferensi prediksi status akhir mahasiswa yang masih aktif, bukan sebagai data latih.

```bash
streamlit run app.py
```

🔗 **Link Prototype:** https://submissionakhirpenerapan-datasciencedicoding-yrxhuip4mdm9gasti.streamlit.app/

## Conclusion

Berdasarkan hasil analisis data dan visualisasi dashboard terhadap 4.424 mahasiswa Jaya Jaya Institut, ditemukan beberapa temuan utama:

**Distribusi Status Mahasiswa** — Dari total 4.424 mahasiswa, 49.9% berhasil Graduate, 32.1% Dropout, dan 17.9% masih Enrolled. Angka dropout hampir 1 dari 3 mahasiswa menunjukkan urgensi penanganan berbasis data.

**Performa Akademik** adalah faktor paling dominan — mahasiswa dengan nilai akademik rendah dan jumlah SKS lulus sedikit cenderung berisiko dropout lebih tinggi, sebagaimana terlihat jelas pada visualisasi "Performa Akademik vs Status" dan "SKS Lulus vs Status" di dashboard.

**Faktor Finansial** terbukti kritis — mahasiswa yang tidak melunasi biaya kuliah memiliki tingkat dropout yang jauh lebih tinggi dibandingkan yang membayar tepat waktu, sesuai visualisasi "Finansial vs Dropout" di dashboard.

**Model Machine Learning** — Logistic Regression yang dilatih hanya dengan data Dropout dan Graduate (mengeksklusi data Enrolled) menghasilkan performa tinggi dengan akurasi **94.2%** dan AUC **0.973**, membuktikan bahwa faktor akademik dan finansial yang teridentifikasi dari EDA memang menjadi prediktor kuat untuk mendeteksi risiko dropout.

### Rekomendasi Action Items

- **Early Warning System** — Implementasikan sistem prediksi ini ke dashboard akademik untuk memantau mahasiswa dengan nilai rendah dan SKS lulus sedikit sejak semester 1
- **Intervensi Finansial** — Buat program keringanan pembayaran, cicilan fleksibel, dan perluas akses beasiswa bagi mahasiswa yang menunggak biaya kuliah
- **Program Pendampingan Akademik** — Wajibkan bimbingan konseling bagi mahasiswa dengan performa akademik rendah di semester pertama
- **Prediksi Mahasiswa Enrolled** — Manfaatkan model untuk memprediksi kemungkinan status akhir mahasiswa yang masih Enrolled sebagai langkah proaktif deteksi dini
- **Integrasi Sistem Akademik** — Integrasikan model prediksi dengan sistem informasi akademik kampus agar berjalan otomatis setiap akhir semester

---

🔗 **GitHub:** https://github.com/ANDI-BACHDAR-DD/Submission_akhir_penerapan-data_science_Dicoding.git

🌐 **Streamlit:** https://submissionakhirpenerapan-datasciencedicoding-yrxhuip4mdm9gasti.streamlit.app/

📊 **Dashboard:** https://lookerstudio.google.com/reporting/97c68282-4d17-454c-84fc-eb81f64408b7

*Proyek ini dibuat sebagai submission Dicoding — Belajar Penerapan Data Science | © 2026 Andi Bachdar*