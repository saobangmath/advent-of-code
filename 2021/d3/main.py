from functools import reduce


def read():
    res = []
    with open("input.txt") as f:
        for x in f:
            res.append(x)
        f.close()
    return res


def part1(f):
    n, bits = len(f), len(f[0])
    eps, gamma = 0, 0
    for bit in range(bits-1):
        ones = reduce(lambda u, v: u+v, [int(f[_][bit]) for _ in range(n)])
        eps <<= 1
        gamma <<= 1
        if ones > n / 2:
            gamma += 1
        else:
            eps += 1

    print(eps * gamma)


def part2(f):
    n, bits = len(f), len(f[0])

    def find_oxygen():
        candices = f.copy()
        for bit in range(bits):
            c = '0'
            if sum([int(candices[_][bit]) for _ in range(len(candices))]) >= (len(candices)+1) // 2:
                c = '1'
            candices = [_ for _ in candices if _[bit] == c]
            if len(candices) == 1:
                return int(candices[0], 2)
        assert(False)
        return -1

    def find_co2():
        candices = f.copy()
        for bit in range(bits):
            c = '1'
            if sum([1 - int(candices[_][bit]) for _ in range(len(candices))]) <= len(candices) // 2:
                c = '0'
            candices = [_ for _ in candices if _[bit] == c]
            if len(candices) == 1:
                return int(candices[0], 2)
        assert (False)
        return -1

    print(find_oxygen() * find_co2())


def main():
    f = read()
    part1(f)
    part2(f)


main()
