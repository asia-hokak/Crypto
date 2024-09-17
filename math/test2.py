from pwn import *
cipher = cipher = [131553, 993956, 964722, 1359381, 43851, 1169360, 950105, 321574, 1081658, 613914, 0, 1213211, 306957, 73085, 993956, 0, 321574, 1257062, 14617, 906254, 350808, 394659, 87702, 87702, 248489, 87702, 380042, 745467, 467744, 716233, 380042, 102319, 175404, 248489]
cipher = [(char // 311 // 47) for char in cipher]
print(len(cipher))
print(cipher)
semi_plaintext = []
for i in range(len(cipher) -1, -1, -1):
    semi_plaintext.append(cipher[i])
def dynamic_xor_encrypt(plaintext, text_key):
    cipher_text = ""
    key_length = len(text_key)
    for i, char in enumerate(plaintext[::-1]):
        key_char = text_key[i % key_length]
        print(i, char, key_char)
        encrypted_char = chr(char ^ ord(key_char))
        cipher_text = encrypted_char + cipher_text
    return cipher_text
print(dynamic_xor_encrypt(semi_plaintext, "trudeau"))
    