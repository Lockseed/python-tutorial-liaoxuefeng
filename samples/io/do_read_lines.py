with open('/Users/qliu/Desktop/刘琦周报.txt', 'r') as f:
    # for line in f:
    #     print(line, end='')
    for index, line in enumerate(f.readlines()):
        print(f"{index} {line.strip()}")