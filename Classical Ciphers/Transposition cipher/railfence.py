def encrypt(plaintext:str, key:int)->str:
    rails = [''] * key
    rail = 0
    dir = 1

    for char in plaintext:
        rails[rail] += char
        if rail == 0:
            dir = 1
        elif rail == key - 1:
            dir = -1
        rail += dir

    return ''.join(rails)

def decrypt(ciphertext:str, key:int):
    rails = [[] for _ in range(key)]
    rail_len = [0] * key
    rail = 0
    dir = 1

    for i in range(len(ciphertext)):
        rail_len[rail] += 1
        if rail == 0:
            dir = 1
        elif rail == key - 1:
            dir = -1
        rail += dir

    idx = 0
    for i in range(key):
        rails[i] = list(ciphertext[idx:idx + rail_len[i]])
        idx += rail_len[i]

    decrypted_text = []
    rail = 0
    dir = 1
    for i in range(len(ciphertext)):
        decrypted_text.append(rails[rail].pop(0))
        if rail == 0:
            dir = 1
        elif rail == key - 1:
            dir = -1
        rail += dir

    return ''.join(decrypted_text)

if __name__ == '__main__':
    cipher = encrypt('THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG', 5)
    plaintext = decrypt(cipher, 5)
    print(cipher)
    print(plaintext)