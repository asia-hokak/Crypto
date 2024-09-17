alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def encrypt(plaintext:str, key:str)->str:
    cipher = ""
    for ch in plaintext.upper():
        if ch.isalpha():
            pos = alphabet.index(ch)
            ch = key[pos]
        cipher += ch
    return cipher

def decrypt(cipher:str, key:str)->str:
    plaintext = ""
    for ch in cipher.upper():
        if ch.isalpha():
            pos = key.index(ch)
            ch = alphabet[pos]
        plaintext += ch
    return plaintext

if __name__ == '__main__':
    key = 'GHAWQYKIJBXSTUVFOPCDRNMEZL'
    cipher = encrypt('THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG', key)
    plaintext = decrypt(cipher, key)
    print(cipher)
    print(plaintext)