# Laporan Praktikum Kriptografi
Minggu ke-: 9      
Topik: Digital Signature (RSA)   
Nama: Reza Dwi Nugroho  
NIM: 230202781   

---

## 1. Tujuan
Tujuan dari praktikum ini adalah untuk mengimplementasikan mekanisme tanda tangan digital menggunakan algoritma RSA, melakukan proses verifikasi tanda tangan digital, serta memahami peran tanda tangan digital dalam menjamin keaslian (otentikasi) dan integritas suatu pesan.  

---

## 2. Dasar Teori
Tanda tangan digital (digital signature) merupakan mekanisme kriptografi yang digunakan untuk menjamin keaslian pengirim pesan, integritas data, dan non-repudiation. Berbeda dengan enkripsi yang bertujuan menjaga kerahasiaan pesan, tanda tangan digital bertujuan untuk membuktikan bahwa pesan benar-benar berasal dari pihak yang sah dan tidak mengalami perubahan selama transmisi.  

Pada algoritma RSA, tanda tangan digital dibuat dengan cara mengenkripsi nilai hash dari pesan menggunakan kunci privat pengirim. Hash berfungsi sebagai representasi unik dari pesan, sehingga perubahan sekecil apa pun pada pesan akan menghasilkan nilai hash yang berbeda. Proses verifikasi dilakukan dengan menggunakan kunci publik pengirim untuk memeriksa kesesuaian tanda tangan dengan pesan.  

Dalam sistem modern, tanda tangan digital sering dikombinasikan dengan infrastruktur kunci publik (Public Key Infrastructure/PKI), di mana Certificate Authority (CA) berperan untuk menjamin keaslian kepemilikan kunci publik. Hal ini memastikan bahwa kunci publik benar-benar milik pihak yang mengklaim identitas tertentu.  

---

## 3. Alat dan Bahan
- Python 3.13  
- Visual Studio Code  
- Git dan akun GitHub

---

## 4. Langkah Percobaan
1. Membuat folder `praktikum/week9-digital-signature/` sesuai struktur yang ditentukan.  
2. Membuat file signature.py pada folder src/.
3. Menuliskan kode program untuk:
4. Generate pasangan kunci RSA
5. Membuat tanda tangan digital
6. Memverifikasi tanda tangan
7. Menguji kegagalan verifikasi pada pesan yang dimodifikasi
8. Menjalankan program menggunakan perintah:
`python signature.py`
9. Mengambil screenshot hasil eksekusi program.

10. Menyusun laporan praktikum dalam file laporan.md.

---

## 5. Source Code
```python
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

# Generate pasangan kunci RSA
key = RSA.generate(2048)
private_key = key
public_key = key.publickey()

# Pesan asli
message = b"Hello, ini pesan penting."
hash_message = SHA256.new(message)

# Membuat tanda tangan digital
signature = pkcs1_15.new(private_key).sign(hash_message)
print("Signature:", signature.hex())

# Verifikasi tanda tangan (pesan asli)
try:
    pkcs1_15.new(public_key).verify(hash_message, signature)
    print("Verifikasi berhasil: tanda tangan valid.")
except (ValueError, TypeError):
    print("Verifikasi gagal: tanda tangan tidak valid.")

# Modifikasi pesan
fake_message = b"Hello, ini pesan palsu."
hash_fake = SHA256.new(fake_message)

# Verifikasi tanda tangan (pesan palsu)
try:
    pkcs1_15.new(public_key).verify(hash_fake, signature)
    print("Verifikasi berhasil (seharusnya gagal).")
except (ValueError, TypeError):
    print("Verifikasi gagal: tanda tangan tidak cocok dengan pesan.")

```
---

## 6. Hasil dan Pembahasan
Hasil pengujian menunjukkan bahwa tanda tangan digital berhasil diverifikasi ketika pesan yang digunakan masih asli dan tidak mengalami perubahan. Hal ini membuktikan bahwa mekanisme tanda tangan digital RSA berjalan dengan benar.  

Pada pengujian dengan pesan yang dimodifikasi, proses verifikasi gagal. Hal ini terjadi karena nilai hash dari pesan palsu berbeda dengan nilai hash pesan asli yang digunakan saat pembuatan tanda tangan. Dengan demikian, tanda tangan digital mampu menjamin integritas pesan dan mendeteksi adanya perubahan data.  

Hasil eksekusi program :

![Hasil Eksekusi](/praktikum/week9-digital-signature/src/image.png)
---

## 7. Jawaban Pertanyaan
1. Apa perbedaan utama antara enkripsi RSA dan tanda tangan digital RSA?
Enkripsi RSA digunakan untuk menjaga kerahasiaan pesan dengan mengenkripsi pesan menggunakan kunci publik penerima. Sebaliknya, tanda tangan digital RSA digunakan untuk menjamin keaslian dan integritas pesan dengan mengenkripsi hash pesan menggunakan kunci privat pengirim.  

2. Mengapa tanda tangan digital menjamin integritas dan otentikasi pesan?
Karena tanda tangan digital dibuat dari hash pesan dan kunci privat pengirim. Jika pesan diubah, nilai hash akan berbeda sehingga verifikasi gagal. Selain itu, hanya pemilik kunci privat yang dapat membuat tanda tangan yang valid, sehingga identitas pengirim dapat diverifikasi.  

3. Bagaimana peran Certificate Authority (CA) dalam sistem tanda tangan digital modern?
Certificate Authority berperan sebagai pihak terpercaya yang memverifikasi identitas pemilik kunci publik dan menerbitkan sertifikat digital. Dengan adanya CA, penerima pesan dapat yakin bahwa kunci publik yang digunakan benar-benar milik pengirim yang sah.  
---

## 8. Kesimpulan
Praktikum ini membuktikan bahwa tanda tangan digital menggunakan RSA mampu menjamin integritas dan keaslian pesan. Proses verifikasi berhasil pada pesan asli dan gagal pada pesan yang dimodifikasi. Oleh karena itu, tanda tangan digital merupakan komponen penting dalam sistem keamanan informasi modern.

---

## 9. Daftar Pustaka

---

## 10. Commit Log
(Tuliskan bukti commit Git yang relevan.  
Contoh:
```
commit abc12345
Author: Nama Mahasiswa <email>
Date:   2025-09-20

    week2-cryptosystem: implementasi Caesar Cipher dan laporan )
```
