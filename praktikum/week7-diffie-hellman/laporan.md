# Laporan Praktikum Kriptografi
Minggu ke-: 7    
Topik: Diffie-Hellman Key Exchange   
Nama: Reza Dwi Nugroho  
NIM: 230202781  

---

## 1. Tujuan
Tujuan dari praktikum ini adalah untuk memahami dan mengimplementasikan protokol Diffie-Hellman sebagai mekanisme pertukaran kunci rahasia melalui saluran publik. Selain itu, praktikum ini bertujuan untuk menganalisis aspek keamanan Diffie-Hellman, khususnya terhadap potensi serangan Man-in-the-Middle (MITM), serta memahami pentingnya mekanisme autentikasi dalam protokol kriptografi modern.  
---

## 2. Dasar Teori
Diffie-Hellman Key Exchange merupakan salah satu protokol kriptografi kunci publik yang digunakan untuk menghasilkan kunci rahasia bersama antara dua pihak yang berkomunikasi melalui saluran tidak aman. Protokol ini diperkenalkan oleh Whitfield Diffie dan Martin Hellman pada tahun 1976. Keamanan Diffie-Hellman didasarkan pada kesulitan penyelesaian masalah logaritma diskrit dalam aritmetika modular.  

Dalam protokol Diffie-Hellman, kedua pihak menyepakati dua parameter publik, yaitu bilangan prima besar dan sebuah generator. Masing-masing pihak memilih kunci privat secara acak dan menghasilkan kunci publik menggunakan operasi perpangkatan modulo. Kunci rahasia bersama diperoleh dari hasil kombinasi kunci privat dengan kunci publik lawan komunikasi.  

Meskipun efektif untuk pertukaran kunci, Diffie-Hellman tidak menyediakan mekanisme autentikasi secara bawaan. Hal ini menyebabkan protokol ini rentan terhadap serangan Man-in-the-Middle, di mana pihak ketiga dapat menyusup dan mengendalikan proses pertukaran kunci.  
---

## 3. Alat dan Bahan
- Python 3.13  
- Visual Studio Code  
- Git dan akun GitHub  
- Library tambahan: `pycryptodome`
---

## 4. Langkah Percobaan
1. Membuat folder `praktikum/week7-diffie-hellman/` sesuai struktur yang ditentukan.  
2. Membuat file `diffie_hellman.py` pada folder `src/`.  
3. Menuliskan kode simulasi Diffie-Hellman Key Exchange.  
4. Menjalankan program menggunakan perintah:  
   `python diffie_hellman.py`  
5. Mengamati hasil kunci rahasia yang dihasilkan oleh Alice dan Bob.  
6. Menambahkan simulasi serangan Man-in-the-Middle (MITM).  
7. Mendokumentasikan hasil dan analisis ke dalam laporan.  
---

## 5. Source Code
```python
import random

# parameter publik
p = 23  # bilangan prima
g = 5   # generator

# private key
a = random.randint(1, p-1)  # Alice
b = random.randint(1, p-1)  # Bob

# public key
A = pow(g, a, p)
B = pow(g, b, p)

# shared secret normal
shared_secret_A = pow(B, a, p)
shared_secret_B = pow(A, b, p)

print("=== Diffie-Hellman Normal ===")
print("Kunci bersama Alice :", shared_secret_A)
print("Kunci bersama Bob   :", shared_secret_B)

# Simulasi MITM
e = random.randint(1, p-1)  # Eve
E = pow(g, e, p)

secret_A_eve = pow(E, a, p)
secret_B_eve = pow(E, b, p)

print("\n=== Serangan MITM ===")
print("Kunci Alice-Eve :", secret_A_eve)
print("Kunci Bob-Eve   :", secret_B_eve)
```
---

## 6. Hasil dan Pembahasan
Pada simulasi Diffie-Hellman tanpa serangan, kunci rahasia yang dihasilkan oleh Alice dan Bob memiliki nilai yang sama. Hal ini menunjukkan bahwa protokol Diffie-Hellman berhasil menghasilkan kunci bersama melalui saluran publik.  

Pada simulasi serangan Man-in-the-Middle, Alice dan Bob tidak lagi memiliki kunci yang sama. Sebaliknya, masing-masing pihak secara tidak sadar membentuk kunci rahasia dengan pihak ketiga (Eve). Hal ini membuktikan bahwa Diffie-Hellman murni tanpa autentikasi memiliki kelemahan keamanan yang signifikan.  

Screenshot hasil eksekusi program:   

![Hasil Eksekusi](/praktikum/week7-diffie-hellman/src/image.png)
---

## 7. Jawaban Pertanyaan
1. Mengapa Diffie-Hellman memungkinkan pertukaran kunci di saluran publik?
Karena nilai yang dipertukarkan merupakan parameter publik dan kunci publik yang tidak dapat digunakan secara langsung untuk menghitung kunci rahasia. Keamanan protokol ini bergantung pada sulitnya masalah logaritma diskrit.  

2. Apa kelemahan utama protokol Diffie-Hellman murni?
Kelemahan utama Diffie-Hellman murni adalah tidak adanya mekanisme autentikasi, sehingga rentan terhadap serangan Man-in-the-Middle.  

3. Bagaimana cara mencegah serangan MITM pada protokol ini?
Serangan MITM dapat dicegah dengan menambahkan autentikasi, seperti penggunaan sertifikat digital, tanda tangan digital, atau dengan mengintegrasikan Diffie-Hellman ke dalam protokol TLS.  
---

## 8. Kesimpulan
Diffie-Hellman Key Exchange mampu menghasilkan kunci rahasia bersama melalui saluran publik secara aman. Namun, tanpa mekanisme autentikasi, protokol ini rentan terhadap serangan Man-in-the-Middle. Oleh karena itu, implementasi Diffie-Hellman dalam sistem nyata harus dikombinasikan dengan metode autentikasi yang kuat.  

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
