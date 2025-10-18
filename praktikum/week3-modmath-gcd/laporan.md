# Laporan Praktikum Kriptografi
Minggu ke-: 3  
Topik: Modular Math (Aritmetika Modular, GCD, Bilangan Prima, Logaritma Diskrit) 
Nama: Reza Dwi Nugroho  
NIM: 230202781  
Kelas: 5 IKRB  

---

## 1. Tujuan
1. Mampu menyelesaikan operasi aritmatika modular.  
2. Mampu menentukan bilangan prima dan menghitung GCD (Greatest Common Divisor).  
3. Mampu menerapkan logaritma diskrit sederhana dalam simulasi kriptografi.  

---

## 2. Dasar Teori
Aritmetika modular adalah sistem aritmetika untuk bilangan bulat, di mana bilangan "berputar kembali" setelah mencapai nilai tertentu—modulus. Operasi dasar seperti penjumlahan, pengurangan, dan perkalian tetap berlaku, namun hasilnya selalu direduksi dalam rentang modulus. Konsep ini fundamental dalam kriptografi karena menciptakan grup matematika hingga (finite fields) yang menjadi dasar bagi banyak algoritma, terutama kriptografi kunci publik. Sifatnya yang periodik memungkinkan operasi yang mudah dihitung satu arah tetapi sulit untuk dibalik.  
Greatest Common Divisor (GCD) dari dua bilangan bulat adalah bilangan bulat positif terbesar yang dapat membagi habis keduanya. Algoritma Euclidean adalah metode yang sangat efisien untuk menemukan GCD. Pengembangan dari algoritma ini, yaitu Extended Euclidean Algorithm, tidak hanya menemukan GCD dari `a` dan `b`, tetapi juga menemukan koefisien `x` dan `y` yang memenuhi persamaan `ax + by = gcd(a, b)`. Hal ini sangat penting untuk menghitung invers modular, yaitu sebuah elemen kunci dalam algoritma seperti RSA untuk proses dekripsi.

---

## 3. Alat dan Bahan
- Python 3.13  
- Visual Studio Code  
- Git dan akun GitHub  

---

## 4. Langkah Percobaan
1. Membuat struktur direktori `praktikum/week3-modmath-gcd/`.  
2. Membuat file baru bernama `modular_math.py` di dalam direktori `src/`.  
3. Mengimplementasikan fungsi-fungsi untuk aritmetika modular (`mod_add, mod_sub, mod_mul, mod_exp`) sesuai panduan.    
4. Menambahkan fungsi `gcd` yang mengimplementasikan Algoritma Euclidean.  
5. Menambahkan fungsi `egcd` dan `modinv` untuk mencari invers modular menggunakan Extended Euclidean Algorithm.  
6. Mengimplementasikan fungsi `discrete_log` sederhana untuk mensimulasikan pencarian logaritma diskrit.  
7. Menjalankan skrip Python dari terminal dengan perintah `python src/modular_math.py` untuk menguji semua fungsi.  
8. Mengambil screenshot dari hasil eksekusi dan menyimpannya di folder `screenshots/`.  
9. Menyusun laporan ini (`laporan.md`) yang berisi seluruh dokumentasi praktikum.  
10. Melakukan commit semua perubahan ke repositori Git dengan pesan commit yang sesuai.  

---

## 5. Source Code
```python
#Langkah 1 — Aritmetika Modular
def mod_add(a, b, n): return (a + b) % n
def mod_sub(a, b, n): return (a - b) % n
def mod_mul(a, b, n): return (a * b) % n
def mod_exp(base, exp, n): return pow(base, exp, n)

print("7 + 5 mod 12 =", mod_add(7, 5, 12))
print("7 * 5 mod 12 =", mod_mul(7, 5, 12))
print("7^128 mod 13 =", mod_exp(7, 128, 13))


#Langkah 2 — GCD & Algoritma Euclidean
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

print("gcd(54, 24) =", gcd(54, 24))


#Langkah 3 — Extended Euclidean Algorithm
def egcd(a, b):
    if a == 0:
        return b, 0, 1
    g, x1, y1 = egcd(b % a, a)
    return g, y1 - (b // a) * x1, x1

def modinv(a, n):
    g, x, _ = egcd(a, n)
    if g != 1:
        return None
    return x % n

print("Invers 3 mod 11 =", modinv(3, 11))  # hasil: 4


#Langkah 4 — Logaritma Diskrit (Discrete Log)
def discrete_log(a, b, n):
    for x in range(n):
        if pow(a, x, n) == b:
            return x
    return None

print("3^x ≡ 4 (mod 7), x =", discrete_log(3, 4, 7))  # hasil: 4
```

---

## 6. Hasil dan Pembahasan
Program dieksekusi tanpa erroe dan menghasilkan output yang sesuai.

Hasil eksekusi program :
![Hasil Eksekusi](/praktikum/week3-modmath-gcd/screenshot/hasil.png)  

---

## 7. Jawaban Pertanyaan
1. *Apa peran aritmetika modular dalam kriptografi modern?*  Aritmetika modular adalah tulang punggung dari kriptografi kunci publik. Perannya adalah untuk menciptakan struktur matematika (seperti grup dan field hingga) di mana operasi "mudah" dilakukan dalam satu arah tetapi sangat "sulit" untuk dibalik. Sifat one-way function ini, contohnya pada eksponensiasi modular vs. logaritma diskrit, memungkinkan pembuatan kunci publik dan privat yang aman. Algoritma seperti RSA, Diffie-Hellman, dan Elliptic Curve Cryptography (ECC) semuanya bergantung pada properti aritmetika modular.  

2. *Mengapa invers modular penting dalam algoritma kunci publik (misalnya RSA)?*  
Dalam RSA, invers modular sangat krusial untuk proses dekripsi. Kunci publik terdiri dari `(e, n)` dan kunci privat terdiri dari `(d, n)`, di mana `d` adalah invers modular dari `e` pada modulus `φ(n)` (phi Euler dari n). Artinya, `d * e ≡ 1 (mod φ(n))`. Proses enkripsi adalah `C = M^e (mod n)`. Untuk mendekripsi, kita menghitung `M = C^d (mod n)`. Tanpa `d` sebagai invers modular dari `e`, operasi dekripsi tidak akan dapat mengembalikan pesan asli `M`. Jadi, invers modular adalah jembatan matematis yang menghubungkan kunci privat dengan kunci publik dan memungkinkan pesan dienkripsi dan didekripsi dengan benar.  

3. *Apa tantangan utama dalam menyelesaikan logaritma diskrit untuk modulus besar?*  
Tantangan utamanya adalah kompleksitas waktu. Tidak ada algoritma efisien yang diketahui (untuk komputer klasik) yang dapat menyelesaikan masalah logaritma diskrit dalam waktu polinomial. Metode paling sederhana adalah brute-force, yang mencoba setiap kemungkinan nilai eksponen `x`, yang menjadi tidak mungkin dilakukan `(infeasible)` ketika modulus `n` sangat besar (misalnya, 2048-bit). Algoritma yang lebih canggih seperti Number Field Sieve memang ada, tetapi kompleksitasnya masih cukup tinggi sehingga dengan memilih ukuran modulus yang cukup besar, keamanannya tetap terjamin. Kesulitan komputasional inilah yang menjadi dasar keamanan dari banyak sistem kriptografi.

---

## 8. Kesimpulan
Praktikum ini berhasil mengimplementasikan konsep-konsep dasar teori bilangan yang menjadi fondasi kriptografi modern. Melalui implementasi fungsi untuk aritmetika modular, GCD, invers modular, dan logaritma diskrit sederhana menggunakan Python, dapat dipahami secara praktis bagaimana operasi-operasi ini bekerja. Percobaan ini juga menegaskan pentingnya kesulitan komputasional dari masalah seperti logaritma diskrit sebagai penjamin keamanan dalam sistem kriptografi kunci publik.

---

## 9. Daftar Pustaka

---

## 10. Commit Log
```
commit abc12345
Author: Reza Dwi Nugroho <rejadwi016@gmail.com>
Date:   2025-10-18

    week3-modmath-gcd 
```
