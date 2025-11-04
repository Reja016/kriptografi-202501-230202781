# Laporan Praktikum Kriptografi
Minggu ke-: 4  
Topik: Entropy & Unicity Distance (Evaluasi Kekuatan Kunci dan Brute Force)  
Nama: Reza Dwi Nugroho  
NIM: 230202781  
Kelas: 5 IKRB    

---

## 1. Tujuan
Setelah mengikuti praktikum ini, mahasiswa diharapkan mampu:  
1. Menyelesaikan perhitungan sederhana terkait entropi kunci.  
2. Menggunakan teorema Euler pada contoh perhitungan modular & invers.  
3. Menghitung **unicity distance** untuk ciphertext tertentu.  
4. Menganalisis kekuatan kunci berdasarkan entropi dan unicity distance.  
5. Mengevaluasi potensi serangan brute force pada kriptosistem sederhana.  

---

## 2. Dasar Teori
1. **Entropi kunci** ini adalah cara mengukur seberapa banyak total kemungkinan kunci yang ada. Entropi diukur dalam "bit". Jika sebuah cipher memiliki entropi 8 bit, artinya ada 2^8 (atau 256) total kombinasi kunci. Semakin tinggi nilai entropinya (seperti AES-128 yang punya 128 bit), semakin banyak pilhan kuncinya, sehingga semakin kuat dan sulit ditebak.  
2. **Unicity Distance** ini adalah perkiraan seberapa panjang sebuah pesan terenkripsi (ciphertext) yang kita perlukan agar bisa menemukan satu-satunya kunci yang benar. Jika pesan rahasia yang kita punya lebih pendek dari nilai ini, kita mungkin akan menemukan bannyak kunci "palsu" yang sepertinya bisa membuka pesan, padahal aslinya salah.  
3. **Serangan Brute Force** ini adalah metode serang paling "dasar" atau "nekat". Penyerangan akan mencoba semua kemungkinan kunci satu persatu sampai menemukan kunci yang benar, seperti mencoba semua kombinasi gembok koper. Keberhasilan serangan ini hanya bergantung pada dua hal: seberapa banyak total kuncinya (entropi) dan seberapa cepat komputer si penyerang.  

---

## 3. Alat dan Bahan
- Python 3.13  
- Visual Studio Code  
- Git dan akun GitHub 

---

## 4. Langkah Percobaan
1. Membuat struktur folder proyek: `praktikum/week4-entropy-unicity/` yang berisi sub-folder `src/` dan `screenshots/`, serta file `laporan.md`.  
2. Membuat file Python baru bernama `entropy_unicity.py` di dalam folder `src/`.  
3. Mengimplementasikan tiga fungsi Python di dalam file tersebut sesuai panduan:  
- `entropy` untuk menghitung entropi kunci.  
- `unicity_distance` untuk menghitung unicity distance.  
- `brute_force_time` untuk mengestimasi waktu serangan brute force.  
4. Menambahkan blok `if __name__ == "__main__":` untuk menjalankan perhitungan pada dua kasus: Caesar Cipher.  
5. Menjalankan program dari terminal menggunakan perintah: `python src/entropy_unicity.py`.  
6. Mengambil screenshot dari output terminal dan menyimpannya sebagai `screenshots/hasil.png`.  
7. Melengkapi file `laporan.md` dengan semua bagian yang diminta, termasuk jawaban pertanyaan diskusi.  
8. Melakukan commit dan push ke repositori GitHub dengan pesan commit `week4-entropy-unicity`.  

---

## 5. Source Code
```python
#Perhitungan Entropi
import math

def entropy(keyspace_size):
    return math.log2(keyspace_size)

print("Entropy ruang kunci 26 =", entropy(26), "bit")
print("Entropy ruang kunci 2^128 =", entropy(2**128), "bit")

#Menghitung Unicity Distance
def unicity_distance(HK, R=0.75, A=26):
    return HK / (R * math.log2(A))

HK = entropy(26)
print("Unicity Distance untuk Caesar Cipher =", unicity_distance(HK))

#Analisis Brute Force
def brute_force_time(keyspace_size, attempts_per_second=1e6):
    seconds = keyspace_size / attempts_per_second
    days = seconds / (3600*24)
    return days

print("Waktu brute force Caesar Cipher (26 kunci) =", brute_force_time(26), "hari")
print("Waktu brute force AES-128 =", brute_force_time(2**128), "hari")
```

---

## 6. Hasil dan Pembahasan
Hasil eksekusi program:

![Hasil Eksekusi](/praktikum/week4-entropy-unicity/screenshots/hasil.png)

---

## 7. Jawaban Pertanyaan
1. Apa arti dari nilai entropy dalam konteks kekuatan kunci? Nilai entropi adalah ukuran logaritmik dari ukuran ruang kunci. Dalam konteks kekuatan kunci, entropi secara langsung menunjukkan tingkat ketidakpastian atau kerumitan yang dihadapi penyerang. Nilai entropi N bit berarti ada 2^N kemungkinan kunci. Semakin tinggi nilai entropi, semakin banyak jumlah kunci yang harus dicoba oleh penyerang, sehingga kunci tersebut semakin kuat terhadap serangan brute force.  
2.  Mengapa unicity distance penting dalam menentukan keamanan suatu cipher? Unicity distance (U) penting karena memberikan batas teoritis yang jelas. Ia memberitahu kita berapa banyak ciphertext yang minimal dibutuhkan oleh penyerang untuk secara unik menentukan kunci yang benar. Jika seorang penyerang memiliki ciphertext yang lebih sedikit dari U, maka akan ada banyak kunci "palsu" yang juga bisa mendekripsi ciphertext tersebut menjadi plaintext yang terlihat "masuk akal". Ini memaksa penyerang untuk mendapatkan lebih banyak data (ciphertext) sebelum dapat memastikan satu kunci yang benar.  
3. Mengapa brute force masih menjadi ancaman meskipun algoritma sudah kuat? Brute force masih menjadi ancaman karena beberapa alasan:  
- Implementasi yang Buruk: Meskipun algoritma (seperti AES) kuat, pengguna mungkin memilih kunci yang lemah, dapat ditebak, atau dihasilkan oleh generator angka acak (RNG) yang buruk. Ini secara drastis mengurangi ruang kunci efektif.  
- Algoritma Lama (Legacy): Algoritma lama seperti DES (56-bit) atau 2DES, yang dulu dianggap kuat, kini ruang kuncinya terlalu kecil dan rentan terhadap brute force dengan perangkat keras modern.  
- Peningkatan Eksponensial Komputasi: Kekuatan komputasi (terutama menggunakan GPU, FPGA, dan ASIC) terus meningkat. Serangan yang dulu dianggap tidak praktis (misal 70-80 bit) kini mulai mungkin dilakukan. Walaupun 128 bit masih aman, ancaman ini nyata untuk kunci berukuran sedang.  
- Serangan Terdistribusi: Penyerang dapat menggunakan jaringan komputer (botnet) atau layanan cloud untuk mendistribusikan upaya brute force, sehingga meningkatkan kecepatan percobaan secara masif.  

---

## 8. Kesimpulan
Praktikum ini menunjukkan bagaimana mengevaluasi kekuatan kriptosistem secara kuantitatif menggunakan entropi kunci, unicity distance, dan estimasi waktu brute force. Melalui perhitungan, terbukti bahwa cipher klasik seperti Caesar Cipher memiliki entropi yang sangat rendah (4.7 bit) dan dapat dipecahkan secara instan. Sebaliknya, kriptosistem modern seperti AES-128 memiliki entropi 128 bit, yang menyediakan ruang kunci sangat besar (2^128) sehingga membuatnya aman dari serangan brute force untuk waktu yang sangat lama.

---

## 9. Daftar Pustaka
---
---

## 10. Commit Log
```
commit d3b9688d1e768a692eb85d151f251048b98bfd1c  
Author: Reza Dwi Nugroho <rejadwi016@gmail.com>  
Date:   2025-11-04  

   week4-entropy-unicity  
```

