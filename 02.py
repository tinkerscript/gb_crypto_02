from binascii import unhexlify


def find_equal_blocks_count(encrypted):
    count = 0
    chunks = [encrypted[x:x + 16] for x in range(0, len(encrypted), 16)]

    for i in range(len(chunks)):
        for j in range(len(chunks)):
            if i == j:
                continue

            if chunks[i] == chunks[j]:
                count += 1

    return count


def main():
    with open('x.txt', 'r') as file1:
        encoded_lines = file1.read().splitlines()

    for line in encoded_lines:
        equal_blocks_count = find_equal_blocks_count(unhexlify(line))

        if equal_blocks_count > 0:
            print(f'{equal_blocks_count} одинаковых блоков в строке {line}')


if __name__ == '__main__':
    main()
