# Laporan Praktikum Kriptografi
Minggu ke-: 10    
Topik: Public Key Infrastructure (PKI & Certificate Authority)   
Nama: Reza Dwi Nugroho  
NIM: 230202781  

---

## 1. Tujuan
Tujuan dari praktikum ini adalah untuk memahami konsep Public Key Infrastructure (PKI), membuat sertifikat digital sederhana menggunakan Python, serta menjelaskan peran Certificate Authority (CA) dalam menjamin keaslian identitas dan keamanan komunikasi pada sistem modern seperti HTTPS dan TLS.  

---

## 2. Dasar Teori
Public Key Infrastructure (PKI) merupakan sebuah kerangka kerja yang digunakan untuk mengelola kunci publik, sertifikat digital, dan identitas dalam sistem kriptografi kunci publik. PKI memungkinkan pihak-pihak yang berkomunikasi melalui jaringan tidak aman untuk saling memverifikasi identitas dan membangun komunikasi yang aman.  

Certificate Authority (CA) adalah entitas terpercaya dalam PKI yang bertugas menerbitkan, memverifikasi, dan menandatangani sertifikat digital. Sertifikat digital berisi informasi identitas pemilik, kunci publik, masa berlaku, serta tanda tangan digital dari CA sebagai bukti keaslian.  

Dalam implementasi nyata seperti HTTPS/TLS, browser akan memverifikasi sertifikat server dengan memeriksa tanda tangan CA, masa berlaku sertifikat, serta kecocokan domain. Dengan demikian, PKI berperan penting dalam mencegah penyadapan dan serangan Man-in-the-Middle (MITM).  

---

## 3. Alat dan Bahan
- Python 3.13  
- Visual Studio Code  
- Git dan akun GitHub 

---

## 4. Langkah Percobaan
1. Membuat folder `praktikum/week10-pki/` sesuai struktur yang ditentukan.
2. Menginstal library tambahan dengan perintah:
   `pip install cryptography pyopenssl`
3. Membuat file pki_cert.py pada folder src/.
4. Menuliskan kode program untuk menghasilkan pasangan kunci RSA.
5. Membuat sertifikat digital self-signed menggunakan library cryptography.
6. Menyimpan sertifikat dalam format .pem.
7. Menjalankan program dengan perintah:
`python pki_cert.py`
8. Mengambil screenshot hasil pembuatan sertifikat.
9. Menyusun laporan praktikum dalam file laporan.md.

---

## 5. Source Code
```python
from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from datetime import datetime, timedelta

# Generate key pair
key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)

# Subject dan Issuer (self-signed certificate)
subject = issuer = x509.Name([
    x509.NameAttribute(NameOID.COUNTRY_NAME, u"ID"),
    x509.NameAttribute(NameOID.ORGANIZATION_NAME, u"UPB Kriptografi"),
    x509.NameAttribute(NameOID.COMMON_NAME, u"example.com"),
])

# Membangun sertifikat
cert = (
    x509.CertificateBuilder()
    .subject_name(subject)
    .issuer_name(issuer)
    .public_key(key.public_key())
    .serial_number(x509.random_serial_number())
    .not_valid_before(datetime.utcnow())
    .not_valid_after(datetime.utcnow() + timedelta(days=365))
    .sign(key, hashes.SHA256())
)

# Simpan sertifikat ke file
with open("cert.pem", "wb") as f:
    f.write(cert.public_bytes(serialization.Encoding.PEM))

print("Sertifikat digital berhasil dibuat: cert.pem")

```

---

## 6. Hasil dan Pembahasan
Hasil eksekusi program menunjukkan bahwa sertifikat digital self-signed berhasil dibuat dan disimpan dalam format cert.pem. Sertifikat ini berisi informasi identitas subjek, kunci publik, masa berlaku, serta tanda tangan digital.  
Sertifikat self-signed hanya cocok digunakan untuk keperluan pembelajaran atau pengujian. Pada sistem produksi, sertifikat harus ditandatangani oleh Certificate Authority terpercaya agar dapat diverifikasi oleh browser atau aplikasi klien.  

Hasil eksekusi program Caesar Cipher:

![Hasil Eksekusi](screenshots/output.png)
![Hasil Input](screenshots/input.png)
![Hasil Output](screenshots/output.png)
)

---

## 7. Jawaban Pertanyaan
1. Apa fungsi utama Certificate Authority (CA)?
Certificate Authority berfungsi sebagai pihak terpercaya yang memverifikasi identitas pemilik sertifikat dan menandatangani sertifikat digital agar dapat dipercaya oleh pihak lain.  

2. Mengapa self-signed certificate tidak cukup untuk sistem produksi?
Karena sertifikat self-signed tidak diverifikasi oleh CA terpercaya, sehingga browser atau klien tidak dapat memastikan keaslian identitas pemilik sertifikat dan berpotensi menimbulkan risiko keamanan.  

3. Bagaimana PKI mencegah serangan MITM dalam komunikasi TLS/HTTPS?
PKI mencegah serangan MITM dengan memastikan bahwa sertifikat server diverifikasi oleh CA terpercaya. Browser akan menolak koneksi jika sertifikat tidak valid atau tidak dapat dipercaya, sehingga pihak ketiga tidak dapat menyamar sebagai server asli.  
---

## 8. Kesimpulan
Praktikum ini menunjukkan bahwa PKI dan Certificate Authority memiliki peran penting dalam menjamin keamanan komunikasi digital. Pembuatan sertifikat digital self-signed berhasil dilakukan, namun untuk sistem nyata diperlukan CA terpercaya agar komunikasi aman dari serangan MITM.  
---

## 9. Daftar Pustaka
(Cantumkan referensi yang digunakan.  
Contoh:  
- Katz, J., & Lindell, Y. *Introduction to Modern Cryptography*.  
- Stallings, W. *Cryptography and Network Security*.  )

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
