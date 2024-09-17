def encrypt(plaintext, key):
    plaintext += ' ' * (-len(plaintext) % key)
    cipher = [''] * key
    for i, ch in enumerate(plaintext):
        cipher[i % key] += ch
    return ''.join(cipher)

def decrypt(cipher, key):
    cipher += ' ' * (-len(cipher) % key)
    row = len(cipher) // key
    plaintext = [''] * row
    for i, ch in enumerate(cipher):
        plaintext[i % row] += ch
    return ''.join(plaintext)

if __name__ == '__main__':
    cipher = encrypt('THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG', 5)
    plaintext = decrypt(cipher, 5)
    print(cipher.encode())
    print(plaintext)