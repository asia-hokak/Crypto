alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def encrypt(plaintext:str, key:int)->str:
    cipher = ""
    for ch in plaintext.upper():
        if ch.isalpha():
            pos = alphabet.index(ch)
            ch = alphabet[(pos + key) % 26]
        cipher += ch
    return cipher

def decrypt(cipher:str, key:int)->str:
    plaintext = ""
    for ch in cipher.upped():
        if ch.isalpha():
            pos = alphabet.index(ch)
            ch = alphabet[(pos + key) % 26]
        plaintext += ch
    return plaintext

if __name__ == '__main__':
    cipher = encrypt('THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG', 13)
    plaintext = decrypt(cipher, 13)
    print(cipher)
    print(plaintext)
