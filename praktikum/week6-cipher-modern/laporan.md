# Laporan Praktikum Kriptografi
Minggu ke-: 6    
Topik: Cipher Modern (DES, AES, RSA)   
Nama: Reza Dwi Nugroho  
NIM: 230202781  

---

## 1. Tujuan
- Mengimplementasikan algoritma DES untuk blok data sederhana.  
- Menerapkan algoritma AES dengan panjang kunci 128 bit.  
- Menjelaskan proses pembangkitan kunci publik dan privat pada algoritma RSA.  

---

## 2. Dasar Teori
Cipher modern dibagi menjadi dua kategori utama: simetris dan asimetris. Cipher simetris, seperti DES (Data Encryption Standard) dan AES (Advanced Encryption Standard), menggunakan kunci rahasia yang sama untuk proses enkripsi dan dekripsi. DES adalah standar lama yang beroperasi pada blok 64-bit dengan kunci 56-bit, yang kini dianggap rentan terhadap serangan brute-force. AES adalah standar industri saat ini, beroperasi pada blok 128-bit dan mendukung panjang kunci 128, 192, atau 256 bit, menawarkan keamanan yang jauh lebih superior.  
Cipher asimetris, diwakili oleh RSA (Rivest-Shamir-Adleman), menggunakan sepasang kunci: kunci publik untuk enkripsi dan kunci privat untuk dekripsi. Kunci publik dapat didistribusikan secara bebas, sementara kunci privat harus dijaga kerahasiaannya oleh pemilik. Keamanan RSA bergantung pada kesulitan komputasi untuk memfaktorkan dua bilangan prima besar (yang membentuk modulus n). Algoritma ini sangat fundamental untuk pertukaran kunci yang aman (KEX) dan tanda tangan digital.  

---

## 3. Alat dan Bahan
- Python 3.13  
- Visual Studio Code  
- Git dan akun GitHub  
- Library tambahan: `pycryptodome`
---

## 4. Langkah Percobaan
1. Membuat struktur folder proyek: `praktikum/week6-cipher-modern/` yang berisi sub-folder `src/, screenshots/`, dan file `laporan.md.`  
2. Menginstal library `pycryptodome` menggunakan perintah `pip install pycryptodome` di terminal.  
3. Membuat file `src/des.py`, menyalin kode dari panduan untuk simulasi enkripsi dan dekripsi DES, dan menjalankannya.  
4. Membuat file `src/aes.py`, mengimplementasikan kode untuk enkripsi dan dekripsi menggunakan AES-128 dengan mode EAX, dan menjalankannya.  
5. Membuat file `src/rsa.py`, mengimplementasikan kode untuk generasi key pair RSA-2048, serta proses enkripsi (dengan public key) dan dekripsi (dengan private key) menggunakan padding OAEP, lalu menjalankannya.  
6. Mengambil screenshot dari hasil eksekusi ketiga program tersebut dan menyimpannya di folder `screenshots/`.  
7. Melengkapi `laporan.md` ini dengan menjawab pertanyaan diskusi dan mengisi semua bagian yang relevan.  
8. Melakukan commit dan push ke repositori Git dengan pesan commit: `week6-cipher-modern`.  

---

## 5. Source Code
```python
### Langkah 1 — Implementasi DES (Opsional, Simulasi)
from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes

key = get_random_bytes(8)  # kunci 64 bit (8 byte)
cipher = DES.new(key, DES.MODE_ECB)

plaintext = b"ABCDEFGH"
ciphertext = cipher.encrypt(plaintext)
print("Ciphertext:", ciphertext)

decipher = DES.new(key, DES.MODE_ECB)
decrypted = decipher.decrypt(ciphertext)
print("Decrypted:", decrypted)



### Langkah 2 — Implementasi AES-128
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

key = get_random_bytes(16)  # 128 bit key
cipher = AES.new(key, AES.MODE_EAX)

plaintext = b"Modern Cipher AES Example"
ciphertext, tag = cipher.encrypt_and_digest(plaintext)

print("Ciphertext:", ciphertext)

# Dekripsi
cipher_dec = AES.new(key, AES.MODE_EAX, nonce=cipher.nonce)
decrypted = cipher_dec.decrypt(ciphertext)
print("Decrypted:", decrypted.decode())



### Langkah 3 — Implementasi RSA
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# Generate key pair
key = RSA.generate(2048)
private_key = key
public_key = key.publickey()

# Enkripsi dengan public key
cipher_rsa = PKCS1_OAEP.new(public_key)
plaintext = b"RSA Example"
ciphertext = cipher_rsa.encrypt(plaintext)
print("Ciphertext:", ciphertext)

# Dekripsi dengan private key
decipher_rsa = PKCS1_OAEP.new(private_key)
decrypted = decipher_rsa.decrypt(ciphertext)
print("Decrypted:", decrypted.decode())
```
---

## 6. Hasil dan Pembahasan
Hasil eksekusi program:

![Hasil RSA](/praktikum/week6-cipher-modern/screenshot/RSA.png)
![Hasil AES](/praktikum/week6-cipher-modern/screenshot/AES.png)
![Hasil DES](/praktikum/week6-cipher-modern/screenshot/DES.png)

---

## 7. Jawaban Pertanyaan
1. **Apa perbedaan mendasar antara DES, AES, dan RSA dalam hal kunci dan keamanan?**  
# Kunci:  
DES & AES: Keduanya adalah algoritma simetris. Mereka menggunakan satu kunci rahasia yang sama untuk enkripsi dan dekripsi.  
RSA: Adalah algoritma asimetris. Ia menggunakan sepasang kunci (dua kunci yang berbeda namun terkait secara matematis): public key (untuk enkripsi) dan private key (untuk dekripsi).  
# Keamanan:  
DES: Dianggap tidak aman. Panjang kuncinya yang efektif hanya 56-bit membuatnya sangat rentan terhadap serangan brute force dengan perangkat keras modern.  
AES: Dianggap sangat aman. Ini adalah standar industri saat ini. Dengan panjang kunci 128, 192, atau 256 bit, AES tahan terhadap serangan brute force dan serangan kriptanalisis canggih lainnya.  
RSA: Dianggap aman jika menggunakan panjang kunci yang memadai (minimal 2048-bit saat ini). Keamanannya bergantung pada kesulitan matematis dalam memfaktorkan bilangan prima besar.  

2. **Mengapa AES lebih banyak digunakan dibanding DES di era modern?**  
AES lebih banyak digunakan karena DES secara fundamental sudah tidak aman. Kunci 56-bit DES dapat dibobol (di-brute force) dalam hitungan jam atau bahkan menit dengan sumber daya komputasi modern. AES (sebagai pengganti DES) dirancang untuk mengatasi kelemahan ini dengan:  
- Ukuran Kunci Jauh Lebih Besar: Minimal 128-bit, yang secara eksponensial lebih sulit untuk di-brute force (triliunan tahun dengan teknologi saat ini).  
- Desain Algoritma Modern: Struktur internal (Substitusi-Permutasi) AES telah dianalisis secara ekstensif dan terbukti kuat terhadap berbagai teknik kriptanalisis.  
- Efisiensi: AES juga sangat efisien dalam implementasi perangkat keras dan perangkat lunak.  
3. **Mengapa RSA dikategorikan sebagai algoritma asimetris, dan bagaimana proses pembangkitan kuncinya?** 
RSA dikategorikan sebagai asimetris karena ia menggunakan dua kunci yang berbeda (publik dan privat) untuk operasi kriptografi. Apa yang dienkripsi dengan public key hanya bisa didekripsi dengan private key yang sesuai, dan sebaliknya (untuk tanda tangan digital).  
Proses pembangkitan kuncinya (secara garis besar) adalah:  
- Pilih Primas (p, q): Pilih dua bilangan prima acak yang sangat besar, p dan q.  
- Hitung Modulus (n): Hitung n = p \times q. Nilai n ini akan digunakan untuk public dan private key.  
- Hitung Totient (\phi(n)): Hitung totient Euler, \phi(n) = (p-1) \times (q-1).  
- Pilih Eksponen Publik (e): Pilih sebuah bilangan bulat e (biasanya nilai kecil seperti 65537) sedemikian rupa sehingga 1 < e < \phi(n) dan e relatif prima terhadap \phi(n) (yaitu, \gcd(e, \phi(n)) = 1).  
- Hitung Eksponen Privat (d): Hitung d sebagai inversi perkalian modular e terhadap \phi(n). Artinya, d adalah angka yang memenuhi persamaan (d \times e) \mod \phi(n) = 1.
Hasil:  
- Kunci Publik: Pasangan (n, e).  
- Kunci Privat: Pasangan (n, d). (Nilai p dan q harus dirahasiakan atau dibuang dengan aman).  
---

## 8. Kesimpulan  
Praktikum ini berhasil mengimplementasikan tiga algoritma cipher modern (DES, AES, RSA) menggunakan library pycryptodome di Python. Melalui implementasi ini, perbedaan mendasar antara cipher simetris (AES/DES) yang cepat dan menggunakan satu kunci, dengan cipher asimetris (RSA) yang lebih lambat namun penting untuk manajemen kunci, menjadi jelas. Percobaan ini mengkonfirmasi bahwa AES (untuk enkripsi data) dan RSA (untuk pertukaran kunci/tanda tangan) adalah fondasi keamanan data modern, sementara DES sudah usang dan tidak aman.

---

## 9. Daftar Pustaka

---

## 10. Commit Log
```
commit 4962a7738b4f24a02766ce271ca145d71e7174b9  
Author: Reza Dwi Nugroho <rejadwi016@gmail.com>  
Date:   2025-11-18  
```
