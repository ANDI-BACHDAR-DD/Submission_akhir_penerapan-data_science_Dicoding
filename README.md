# Laporan Proyek Data Science: Deteksi Dini Mahasiswa Dropout di Jaya Jaya Institut

---

## 1. Business Understanding

### Latar Belakang Masalah
Jaya Jaya Institut menghadapi tantangan serius terkait tingginya angka mahasiswa yang tidak menyelesaikan studi (dropout). Permasalahan ini tidak hanya berdampak pada mahasiswa secara individu, tetapi juga memengaruhi reputasi institusi serta efisiensi operasional kampus.

Pendekatan yang selama ini dilakukan cenderung reaktif. Oleh karena itu, diperlukan sistem yang mampu mendeteksi potensi dropout sejak dini sehingga intervensi dapat dilakukan lebih cepat.

---

### Problem Statement
Bagaimana mengidentifikasi mahasiswa yang berpotensi dropout berdasarkan data akademik dan non-akademik sehingga institusi dapat melakukan intervensi lebih awal?

---

### Goals
- Mengembangkan model Machine Learning untuk memprediksi status mahasiswa
- Mengidentifikasi faktor utama yang mempengaruhi dropout
- Membangun sistem monitoring berbasis data

---

### Business Impact
- Menurunkan angka dropout
- Meningkatkan tingkat kelulusan
- Mendukung pengambilan keputusan berbasis data

---

## 2. Data Understanding

Dataset terdiri dari **4.424 data mahasiswa** dengan **37 fitur** yang mencakup:

- Profil mahasiswa (usia, gender)
- Latar belakang pendidikan
- Kondisi keluarga
- Performa akademik semester 1 & 2
- Faktor eksternal (GDP, inflasi, unemployment rate)

---

### Insight Awal

- Performa akademik memiliki variasi yang signifikan antar mahasiswa  
- Banyak mahasiswa memiliki nilai 0 pada evaluasi tertentu, mengindikasikan ketidakterlibatan akademik  
- Faktor eksternal seperti kondisi ekonomi berpotensi mempengaruhi keberlanjutan studi  

Menariknya, dataset ini tidak hanya fokus pada performa akademik, tetapi juga mencoba menangkap konteks sosial-ekonomi yang lebih luas.

---

## 3. Data Preparation

Tahapan preprocessing dilakukan sebagai berikut:

- Tidak ditemukan missing values → data siap digunakan
- Seluruh fitur kategorikal diubah ke numerik menggunakan Label Encoding
- Dataset dibagi menjadi data train dan test (80:20)

---

### Insight Data Preparation

- Dataset dalam kondisi bersih tanpa missing values  
- Terdapat **class imbalance** pada target:
  - Kelas dominan: 2209
  - Kelas menengah: 1421
  - Kelas minoritas: 794  

Ketidakseimbangan ini berpotensi membuat model bias terhadap kelas mayoritas.

---

## 4. Exploratory Data Analysis (EDA)

Beberapa pola penting yang ditemukan:

- Mahasiswa dengan performa akademik rendah cenderung memiliki risiko dropout lebih tinggi  
- Ketidakhadiran dalam evaluasi menjadi indikator kuat kegagalan akademik  
- Faktor seperti pembayaran biaya kuliah juga memiliki pengaruh signifikan  

---

## 5. Modeling

Digunakan dua model:
- Logistic Regression (baseline)
- Random Forest (model utama)

---

### Hasil Evaluasi Model

#### Logistic Regression
- Accuracy: 71%
- Recall (kelas dropout rendah): 27%

#### Random Forest
- Accuracy: 76%
- Precision: 74%
- Recall: 76%
- F1 Score: 74%

---

### Analisis Model

- Random Forest memberikan performa lebih baik secara keseluruhan  
- Model sangat baik dalam memprediksi kelas mayoritas (hingga 92% recall)  
- Namun, performa untuk kelas dropout masih rendah (~30% recall)

---

## 6. Evaluation & Insight

### Insight Utama Model

- Model cenderung lebih akurat dalam memprediksi mahasiswa yang lulus dibandingkan yang dropout  
- Hal ini menunjukkan bahwa pola dropout lebih kompleks dan sulit diprediksi  
- Ketidakseimbangan data menjadi salah satu penyebab utama  

---

### Feature Importance

Faktor paling berpengaruh:

1. Performa akademik (jumlah lulus & nilai semester)
2. Status pembayaran kuliah
3. Nilai awal (admission grade)
4. Usia saat masuk

---

### Insight Bisnis

- Dropout tidak hanya disebabkan faktor akademik  
- Faktor finansial memiliki pengaruh signifikan  
- Ketidakterlibatan akademik (tidak ikut evaluasi) menjadi sinyal kuat risiko  

---

## 7. Conclusion

Model Random Forest mampu memberikan performa yang cukup baik dengan akurasi 76%.

Namun, tantangan utama terletak pada:
- Rendahnya kemampuan model dalam mendeteksi mahasiswa dropout
- Kompleksitas faktor penyebab dropout

Secara umum:
- Performa akademik menjadi faktor utama
- Faktor finansial menjadi indikator tambahan yang penting

Model ini dapat digunakan sebagai **early warning system**, namun masih perlu penyempurnaan.

---

## 8. Action Items

Berikut rekomendasi yang dapat diterapkan:

### 1. Early Warning System
Mahasiswa dengan:
- Nilai rendah
- Tidak mengikuti evaluasi  
langsung masuk kategori risiko tinggi

---

### 2. Monitoring Akademik
Mahasiswa dengan jumlah SKS tidak lulus tinggi harus dipantau secara khusus

---

### 3. Intervensi Finansial
Mahasiswa dengan status pembayaran bermasalah perlu diberikan:
- opsi cicilan
- bantuan beasiswa

---

### 4. Program Pendampingan
Mahasiswa berisiko wajib mengikuti:
- bimbingan akademik
- mentoring

---

## 9. Dashboard Recommendation

Dashboard harus menampilkan:

- Distribusi performa mahasiswa  
- Status risiko mahasiswa  
- Insight otomatis berdasarkan data  
- Filter interaktif (gender, course, dll)

---

## 10. Deployment (Streamlit)

Sistem dibangun menggunakan Streamlit dengan alur:

1. Input data mahasiswa  
2. Model melakukan prediksi  
3. Output:
   - Status risiko
   - Insight penyebab utama  
   - Rekomendasi tindakan  

Model ini dapat digunakan sebagai alat bantu dalam pengambilan keputusan akademik.