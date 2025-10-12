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
    message = "universitas putra bangsa"
    key = 2

    enc = encrypt(message, key)
    dec = decrypt(enc, key)

    print("Plaintext :", message)
    print("Ciphertext:", enc)
    print("Decrypted :", dec)