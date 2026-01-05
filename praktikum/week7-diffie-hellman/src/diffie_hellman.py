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
