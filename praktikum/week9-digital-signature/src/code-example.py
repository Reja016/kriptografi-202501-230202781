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