def pkcs7_padding(block, target_length):
    padding = 16 if len(block) == target_length else target_length - len(block) % target_length
    return block + bytes([padding] * padding)


def main():
    print(pkcs7_padding(b'YELLOW SUBMARINE', 16))


if __name__ == '__main__':
    main()
