# Laporan Praktikum Kriptografi
Minggu ke-: 2  
Topik: Cryptosystem (Komponen, Enkripsi & Dekripsi, Simetris & Asimetris)  
Nama: Reza Dwi Nugroho  
NIM: 230202781  
Kelas: 5 IKRB  

---

## 1. Tujuan
- Memahami komponen-komponen dasar yang membentuk sebuah kriptosistem.
- Mampu mengimplementasikan algoritma enkripsi-dekripsi sederhana.
- Memahami perbedaan fundamental, kelebihan, dan kelemahan sistem simetris dan asimetris.
- Menganalisis masalah utama dalam sistem kriptografi, seperti distribusi kunci.

---

## 2. Dasar Teori
Kriptografi adalah ilmu dan seni untuk menjaga keamanan pesan. Sebuah sistem kriptografi atau kriptosistem terdiri dari serangkaian algoritma dan protokol untuk mengamankan komunikasi. Salah satu bentuk kriptografi paling awal adalah cipher klasik seperti Caesar Cipher, yang merupakan substitution cipher di mana setiap huruf digantikan oleh huruf lain berdasarkan kunci pergeseran. Meskipun sederhana, ia menjadi dasar untuk memahami konsep kunci, enkripsi, dan dekripsi.

Secara umum, kriptografi modern terbagi menjadi dua kategori utama berdasarkan cara penggunaan kuncinya: simetris dan asimetris.
- **Kriptografi Simetris (Private Key Cryptography)**  
Dalam sistem ini, satu kunci rahasia (private key) yang sama digunakan untuk proses enkripsi dan dekripsi. Pengirim dan penerima harus memiliki kunci yang identik sebelum berkomunikasi. Karena proses komputasinya yang sederhana, algoritma ini sangat cepat dan efisien untuk mengenkripsi data dalam jumlah besar. Tantangan utamanya adalah bagaimana cara membagikan kunci rahasia ini secara aman (masalah distribusi kunci).  
Contoh Algoritma Simetris:  
a. AES (Advanced Encryption Standard): Standar industri saat ini yang dianggap sangat aman dan efisien. AES digunakan secara luas di berbagai aplikasi, mulai dari keamanan Wi-Fi (WPA2/WPA3) hingga enkripsi database.  
b. DES (Data Encryption Standard): Standar yang lebih tua. Karena panjang kuncinya yang pendek (56-bit), DES sudah dianggap tidak aman untuk aplikasi modern karena rentan terhadap serangan brute-force.  
- **Kriptografi Asimetris (Public Key Cryptography)**  
Sistem ini menggunakan sepasang kunci yang saling berhubungan secara matematis: kunci publik (public key) dan kunci privat (private key).  
a. Kunci Publik: Dapat dibagikan secara bebas. Digunakan untuk mengenkripsi pesan.  
b. Kunci Privat: Harus dijaga kerahasiaannya oleh pemilik. Digunakan untuk mendekripsi pesan.  
Pesan yang dienkripsi dengan kunci publik seseorang hanya bisa didekripsi oleh kunci privat pasangannya. Sistem ini memecahkan masalah distribusi kunci, namun proses komputasinya jauh lebih lambat dibandingkan kriptografi simetris.  
Contoh Algoritma Asimetris:  
a. RSA (Rivest-Shamir-Adleman): Salah satu algoritma asimetris pertama dan paling terkenal. Keamanannya didasarkan pada kesulitan matematis untuk memfaktorkan bilangan prima yang sangat besar. RSA banyak digunakan untuk tanda tangan digital dan pertukaran kunci aman (misalnya dalam protokol TLS/SSL).  
b. ECC (Elliptic Curve Cryptography): Alternatif modern untuk RSA yang menawarkan tingkat keamanan yang sama dengan panjang kunci yang jauh lebih pendek. Ini membuatnya sangat efisien untuk perangkat dengan sumber daya terbatas, seperti smartphone.

---

## 3. Alat dan Bahan
- Python 3.13 atau terbaru  
- Visual Studio Code
- Git dan akun GitHub  

---

## 4. Langkah Percobaan
1. Membuat direktori baru dengan nama `week2-cryptosystem` di dalam repositori praktikum.
2. Membuat file `simple_crypto.py` di dalam sub-direktori `src/`.
3. Menuliskan kode program untuk implementasi Caesar Cipher yang mencakup fungsi enkripsi dan dekripsi.
4. Menambahkan fungsi `main` untuk interaksi dengan pengguna, yang memungkinkan input teks, kunci, dan pilihan mode (enkripsi atau dekripsi).
5. Menjalankan program dari terminal dengan perintah `python src/simple_crypto.py`.
6. Melakukan beberapa pengujian dengan pesan dan kunci yang berbeda untuk memverifikasi fungsionalitas program.
7. Mengambil screenchot dari hasil eksekusi program untuk dilampirkan dalam laporan.

---

## 5. Source Code
```python
def encrypt(plaintext, key):
    result = ""
    for char in plaintext:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            result += chr((ord(char) - shift + key) % 26 + shift)
        elif char.isdigit():
            result += chr((ord(char) - ord('0') + key) % 10 + ord('0'))
        else:
            result += char
    return result

def decrypt(ciphertext, key):
    result = ""
    for char in ciphertext:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            result += chr((ord(char) - shift - key) % 26 + shift)
        elif char.isdigit():
            result += chr((ord(char) - ord('0') - key) % 10 + ord('0'))
        else:
            result += char
    return result

if __name__ == "__main__":
    message = "<230202781><Reza Dwi NUgroho>"
    key = 5

    enc = encrypt(message, key)
    dec = decrypt(enc, key)

    print("Plaintext :", message)
    print("Ciphertext:", enc)
    print("Decrypted :", dec)
```

---

## 6. Hasil dan Pembahasan
Program Caesar Cipher berhasil diimplementasikan sesuai dengan tujuan praktikum. Pengujian fungsionalitas dilakukan dengan beberapa skenario input untuk memvalidasii proses enkripsi dan dekripsi. Hasilnya disajikan dalam tabel berikut:

| Plaintext | Kunci | Mode | Hasil Program | Status |  
|-------------------------------|-----|-------|------------------------------|--------|  
| <230202781><Reza Dwi NUgroho> | 5 | enkrip | <785757236><Wjef Ibn SZlwtmt> | **Sesuai** |  
| <785757236><Wjef Ibn SZlwtmt> | 5 | dekrip | <230202781><Reza Dwi NUgroho> |**Sesuai**|  
| universitas putra bangsa | 2 | enkrip | wpkxgtukvcu rwvtc dcpiuc | **Sesuai** |  
| wpkxgtukvcu rwvtc dcpiuc | 2 | dekrip | universitas putra bangsa | **Sesuai** |  

Seperti yang ditunjukkan pada tabel, program berjalan tanpa error dan memberikan output yang benar sesuai dengan prinsip kerja Caesar Cipher. 

Hasil eksekusi program Caesar Cipher:
![Hasil Eksekusi](/praktikum/week2-cryptosystem/Screenshot/hasil_eksekusi.png)
![Diagram Kriptosistem](/praktikum/week2-cryptosystem/Screenshot/diagram_kriptosistem.png)

---

## 7. Jawaban Pertanyaan  
- Pertanyaan 1: Sebutkan komponen utama dalam sebuah kriptosistem.  
1. Plaintext: Data asli yang dapat dibaca dan dimengerti manusia atau mesin.
2. Ciphertext: Data dalam bentuk tersandi setelah melalui proses enkripsi.
3. Algoritma Enkripsi: Fungsi matematis atau serangkaian aturan yang mengubah plaintext menjadi ciphertext dengan menggunakan kunci.
4. Algoritma Dekripsi: Fungsi kebalikan dari enkripsi, yang mengubah ciphertext kembali menjadi plaintext dengan menggunakan kunci.
5. Kunci (Key): Sebuah parameter rahasia yang mengontrol operasi algoritma enkripsi dan dekripsi. Keamanan seluruh sistem bergantung pada kerahasiaan dan kompleksitas kunci ini.

- Pertanyaan 2: Apa kelebihan dan kelemahan sistem simetris dibandingkan asimetris?  

| Aspek | Kriptografi Simetris (Contoh: AES, DES) | Kriptografi Asimetris (Contoh: RSA, ECC) |  
|-------|-----------------------------------------------------------------------|------------------------------------------------------------------------------|  
| Kunci | Menggunakan satu kunci rahasia yang sama untuk enkripsi dan dekripsi | Menggunakan sepasang kunci: satu kunci publik (untuk enkripsi) dan satu kunci privat (untuk dekripsi) |  
| Kelebihan | Kecepatan Tinggi | Manajemen Kunci Aman: Memecahkan masalah distribusi kunci. Kunci publik bisa disebar bebas tanpa risiko keamanan |  
Kelemahan | Masalah Distribusi Kunci: Tantangan terbesarnya adalah bagaimana cara membagikan kunci rahasia secara aman kepada penerima |
  Kecepatan Lambat |  

- Pertanyaan 3: Mengapa distribusi kunci menjadi masalah utama dalam kriptografi simetris?  
Distribusi kunci adalah "tumit Achilles" dari kriptografi simetris. Masalah ini muncul karena prasyarat utama agar komunikasi aman dapat terjadi adalah kedua belah pihak harus sudah memiliki kunci rahasia yang identik. Ini menciptakan dilema logis:  
Bagaimana cara mengirimkan kunci rahasia ini pertama kali kepada penerima?  
a. Jika kunci dikirim melalui saluran yang sama (misalnya, internet) yang ingin diamankan, seorang penyadap dapat mencegat kunci tersebut.  
b. Begitu kunci bocor, seluruh kerahasiaan komunikasi di masa depan akan hilang, karena penyadap memiliki "kunci utama" untuk membuka semua pesan.  
Masalah ini sering diselesaikan dengan menggunakan sistem hibrida, di mana kriptografi asimetris yang lambat digunakan hanya untuk tujuan awal yang sangat penting: mengenkripsi dan bertukar kunci simetris (session key) secara aman. Setelah itu, komunikasi selanjutnya menggunakan kunci simetris yang cepat tersebut.

---

## 8. Kesimpulan
Praktikum ini berhasil mencapai tujuannya dalam mendemonstrasikan komponen dan proses dasar sebuah kriptosistem melalui implementasi Caesar Cipher. Kesimpulan utama yang dapat ditarik adalah:
1. Konsep Kriptosistem Terbukti: Implementasi Caesar Cipher secara nyata menunjukkan bagaimana plaintext, ciphertext, kunci, serta algoritma enkripsi dan dekripsi bekerja sama sebagai satu sistem.
2. Keamanan Bergantung pada Desain Algoritma dan Kunci: Meskipun fungsional, analisis terhadap Caesar Cipher membuktikan bahwa algoritma dengan ruang kunci kecil sangat tidak aman dan mudah dipecahkan dengan teknik brute-force dan analisis frekuensi.
3. Pentingnya Manajemen Kunci: Percobaan ini secara implisit menyoroti masalah fundamental dalam kriptografi simetris, yaitu distribusi kunci yang aman, yang menjadi pembeda utama dengan kriptografi asimetris.
Secara keseluruhan, praktikum ini memberikan fondasi pemahaman bahwa kriptografi modern memerlukan algoritma yang jauh lebih kompleks dan protokol manajemen kunci yang canggih untuk mencapai keamanan yang sesungguhnya.

---

## 9. Daftar Pustaka

---

## 10. Commit Log
```
commit 33775367dfe810083124f4857e6b62521b4caafa
Author: Reza Dwi Nugroho <rejadwi016@gmail.com>
Date:   2025-10-12

    week2-cryptosystem: implementasi Caesar Cipher dan laporan
```
