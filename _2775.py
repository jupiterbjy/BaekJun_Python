from functools import lru_cache


@lru_cache(maxsize=256)
def func(k, n):
    if k:
        lower_floor = sum((func(k - 1, room) for room in range(1, n + 1)))
        return lower_floor
    else:
        return n


if __name__ == '__main__':
    test = []
    for i in range(int(input())):
        test.append((int(input()), int(input())))

    for t in test:
        print(func(*t))
