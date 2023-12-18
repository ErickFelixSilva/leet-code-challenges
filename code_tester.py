from functools import reduce

if __name__ == '__main__':
    teste = [0, 1, 2, 3]
    it = teste.__iter__()
    it.__next__()
    it.__next__()
    print(it.__next__())