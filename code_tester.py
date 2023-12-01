from functools import reduce

if __name__ == '__main__':
    teste = ["ab", "c"]
    result = ''
    print(reduce((lambda x, y: x + y), teste))

    print(teste.count('S'))