alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def encrypt(plaintext:str, key:str)->str:
    cipher = ""
    key_pos = 0
    for ch in plaintext.upper():
        ch2 = key[key_pos % len(key)].upper()
        if ch.isalpha():
            pos = alphabet.index(ch)
            offset = alphabet.index(ch2)
            ch = alphabet[(pos + offset) % 26]
            key_pos += 1
        cipher += ch
    return cipher

def decrypt(cipher:str, key:str)->str:
    plaintext = ""
    key_pos = 0
    for ch in cipher.upper():
        ch2 = key[key_pos % len(key)].upper()
        if ch.isalpha():
            pos = alphabet.index(ch)
            offset = alphabet.index(ch2)
            ch = alphabet[(pos - offset) % 26]
            key_pos += 1
        plaintext += ch
    return plaintext

if __name__ == '__main__':
    cipher = encrypt('THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG', 'ABCD')
    plaintext = decrypt(cipher, 'ABCD')
    print(cipher)
    print(plaintext)
