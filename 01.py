import base64
from Cryptodome.Cipher import AES


def aes128_decrypt(block, key):
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.decrypt(block)


def main():
    with open('1.txt', 'r') as file1:
        encoded = file1.read()

    text = base64.b64decode(encoded)
    decrypted = aes128_decrypt(text, b'YELLOW SUBMARINE')
    print(decrypted)


if __name__ == '__main__':
    main()
