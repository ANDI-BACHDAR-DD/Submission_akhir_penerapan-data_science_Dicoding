# Proyek Akhir: Menyelesaikan Permasalahan Institusi Pendidikan

## Business Understanding

### Latar Belakang Masalah

Jaya Jaya Institut merupakan salah satu institusi pendidikan tinggi yang telah berdiri sejak tahun 2000 dan telah mencetak ribuan lulusan dengan reputasi yang baik. Namun dalam beberapa tahun terakhir, institusi ini menghadapi tantangan serius berupa tingginya angka mahasiswa yang tidak menyelesaikan pendidikan mereka alias **dropout**.

Tingkat dropout yang tinggi membawa dampak multidimensional bagi institusi:

- **Dampak Akreditasi:** Angka dropout yang tinggi menjadi salah satu indikator negatif dalam penilaian akreditasi perguruan tinggi. Institusi dengan angka dropout tinggi berpotensi mengalami penurunan peringkat akreditasi yang secara langsung memengaruhi kepercayaan masyarakat dan daya saing kampus.
- **Dampak Reputasi:** Calon mahasiswa dan orang tua cenderung memilih institusi dengan tingkat kelulusan tinggi. Tingginya dropout merusak citra Jaya Jaya Institut di mata publik dan menurunkan daya tarik bagi calon mahasiswa baru.
- **Dampak Finansial:** Setiap mahasiswa yang dropout berarti kehilangan potensi pendapatan dari biaya pendidikan jangka panjang. Selain itu, investasi yang telah dikeluarkan institusi dalam bentuk fasilitas, dosen, dan sumber daya menjadi tidak optimal.
- **Dampak Operasional:** Tingginya angka dropout mempersulit perencanaan kapasitas kelas, alokasi dosen, dan pengelolaan fasilitas kampus sehingga efisiensi operasional terganggu.

Berdasarkan data yang dimiliki, sekitar **32.1%** mahasiswa Jaya Jaya Institut tidak menyelesaikan studi mereka. Angka ini jauh di atas ambang batas yang dapat ditoleransi dan memerlukan penanganan sistematis berbasis data.

Selama ini pendekatan yang dilakukan cenderung **reaktif** — institusi baru mengetahui mahasiswa akan dropout setelah prosesnya sudah terlanjur terjadi. Tidak ada sistem peringatan dini yang mampu mengidentifikasi mahasiswa berisiko sejak semester awal sehingga intervensi bisa dilakukan lebih cepat dan tepat sasaran.

Oleh karena itu dibutuhkan sebuah sistem prediksi berbasis **Machine Learning** yang mampu mendeteksi mahasiswa berpotensi dropout sejak dini, mengidentifikasi faktor utama penyebabnya, dan memberikan rekomendasi intervensi yang dapat ditindaklanjuti oleh pihak akademik.

### Permasalahan Bisnis

1. Bagaimana memprediksi status akhir mahasiswa (Graduate, Dropout, atau Enrolled) berdasarkan data akademik dan non-akademik yang tersedia sejak semester pertama, sehingga institusi dapat melakukan intervensi lebih awal sebelum mahasiswa benar-benar dropout?
2. Faktor-faktor apa saja yang paling signifikan memengaruhi risiko dropout mahasiswa di Jaya Jaya Institut?
3. Bagaimana membangun sistem early warning yang dapat diakses oleh tim akademik untuk memantau mahasiswa berisiko secara real-time?

### Cakupan Proyek

| Area | Deskripsi |
|------|-----------|
| **Analisis Data (EDA)** | Eksplorasi mendalam terhadap 4.424 data mahasiswa untuk menemukan pola distribusi, tren, korelasi, dan faktor penyebab dropout |
| **Business Dashboard** | Visualisasi interaktif menggunakan Looker Studio untuk monitoring status mahasiswa dan faktor risiko dropout |
| **Machine Learning** | Pembangunan model prediksi dropout dengan Logistic Regression dan Random Forest dilengkapi hyperparameter tuning |
| **Deployment** | Prototype sistem prediksi berbasis Streamlit yang dapat digunakan tim akademik untuk menginput data mahasiswa dan mendapat prediksi risiko |

### Persiapan

Sumber data:
```
https://raw.githubusercontent.com/dicodingacademy/dicoding_dataset/main/students_performance/data.csv
```

Setup environment:
```bash
# 1. Clone repository
git clone https://github.com/ANDI-BACHDAR-DD/Submission_akhir_penerapan-data_science_Dicoding.git
cd Submission_akhir_penerapan-data_science_Dicoding

# 2. Buat dan aktifkan virtual environment
python -m venv venv
source venv/bin/activate  # Mac/Linux
# venv\Scripts\activate   # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Jalankan notebook
jupyter notebook notebook.ipynb

# 5. Jalankan prototype Streamlit
streamlit run app.py
```

## Business Dashboard

Dashboard bisnis dibuat menggunakan **Looker Studio** untuk memberikan gambaran menyeluruh kepada manajemen akademik dan tim konselor Jaya Jaya Institut tentang kondisi dropout mahasiswa.

Dashboard menampilkan visualisasi interaktif mencakup distribusi status mahasiswa, dropout rate berdasarkan gender (pria 45.1% vs wanita 25.1%), pengaruh status keuangan terhadap dropout (mahasiswa menunggak memiliki dropout rate 86.6%), pengaruh beasiswa (penerima beasiswa hanya 12.2% dropout), serta performa akademik rata-rata per status mahasiswa. Tersedia juga filter interaktif berdasarkan gender, program studi, dan status beasiswa.

🔗 **Link Dashboard:** https://lookerstudio.google.com/reporting/97c68282-4d17-454c-84fc-eb81f64408b7

## Menjalankan Sistem Machine Learning

Sistem prediksi dropout dibangun menggunakan **Streamlit** yang memungkinkan tim akademik menginput data mahasiswa secara langsung dan mendapatkan prediksi risiko dropout beserta faktor utama yang berkontribusi.

```bash
streamlit run app.py
```

Sistem menerima input data akademik mahasiswa (nilai, jumlah SKS, evaluasi) dan data non-akademik (status keuangan, beasiswa, usia), kemudian memberikan prediksi status mahasiswa beserta probabilitas setiap kelas dan faktor risiko utama yang terdeteksi.

🔗 **Link Prototype:** https://submissionakhirpenerapan-datasciencedicoding-yrxhuip4mdm9gasti.streamlit.app/

## Conclusion

Berdasarkan analisis menyeluruh terhadap dataset 4.424 mahasiswa Jaya Jaya Institut, ditemukan bahwa dropout mahasiswa dipicu oleh kombinasi faktor akademik dan non-akademik yang saling berinteraksi:

1. **Performa Akademik Rendah** adalah prediktor terkuat — mahasiswa dropout rata-rata hanya lulus 2.5 SKS di semester 1, jauh lebih rendah dibandingkan mahasiswa lulus yang rata-rata 6.2 SKS
2. **Status Pembayaran Kuliah** menjadi faktor finansial paling kritis — 86.6% mahasiswa yang menunggak biaya kuliah mengalami dropout
3. **Tidak Memiliki Beasiswa** meningkatkan risiko dropout signifikan — 38.7% vs hanya 12.2% pada penerima beasiswa
4. **Usia Masuk Lebih Tua** berkorelasi dengan risiko dropout lebih tinggi — rata-rata usia dropout 26.1 tahun vs lulusan 21.8 tahun
5. **Gender** — mahasiswa pria memiliki dropout rate 45.1%, jauh lebih tinggi dari wanita 25.1%

Model **Random Forest** yang telah dituning menghasilkan akurasi **76%** dan mampu digunakan sebagai sistem early warning untuk mendeteksi mahasiswa berisiko sejak semester pertama.

### Rekomendasi Action Items

- **Early Warning System** — Implementasikan sistem prediksi ini ke dashboard akademik untuk memantau mahasiswa dengan nilai rendah dan ketidakterlibatan evaluasi di semester 1
- **Intervensi Finansial** — Buat program keringanan pembayaran, cicilan fleksibel, dan perluas akses beasiswa bagi mahasiswa yang menunggak karena kelompok ini memiliki dropout rate 86.6%
- **Program Pendampingan Akademik** — Wajibkan bimbingan konseling bagi mahasiswa dengan kurang dari 3 SKS lulus di semester 1
- **Program Khusus Mahasiswa Pria** — Buat program mentoring dan engagement khusus mengingat dropout rate pria jauh lebih tinggi
- **Intervensi Mahasiswa Usia Dewasa** — Sediakan kelas malam atau program fleksibel untuk mahasiswa berusia di atas 25 tahun
- **Pengembangan Model** — Tingkatkan performa model terutama untuk deteksi kelas dropout dengan teknik oversampling (SMOTE)
- **Integrasi Sistem Akademik** — Integrasikan model prediksi dengan sistem informasi akademik kampus agar berjalan otomatis setiap akhir semester

---

🔗 **GitHub:** https://github.com/ANDI-BACHDAR-DD/Submission_akhir_penerapan-data_science_Dicoding.git

🌐 **Streamlit:** https://submissionakhirpenerapan-datasciencedicoding-yrxhuip4mdm9gasti.streamlit.app/

📊 **Dashboard:** https://lookerstudio.google.com/reporting/97c68282-4d17-454c-84fc-eb81f64408b7

*Proyek ini dibuat sebagai submission Dicoding — Belajar Penerapan Data Science | © 2026 Andi Bachdar*