alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def encrypt(plaintext:str, a:int, b:int)->str:
    cipher = ""
    for ch in plaintext:
        if ch.isalpha():
            pos = alphabet.index(ch.upper())
            ch = alphabet[(pos * a + b) % 26]
        cipher += ch
    return cipher

def decrypt(cipher:str, a:int, b:int)->str:
    plaintext = ""
    inv = pow(a, -1, 26)
    for ch in cipher:
        if ch.isalpha():
            pos = alphabet.index(ch.upper())
            ch = alphabet[(pos - b) * inv % 26]
        plaintext += ch
    return plaintext

if __name__ == '__main__':
    cipher = encrypt('THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG', 15, 3)
    plaintext = decrypt(cipher, 15, 3)
    print(cipher)
    print(plaintext)
