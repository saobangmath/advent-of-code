def read():
    res = []
    with open('input.txt', 'r') as f:
        for _ in f:
            res.append(int(_))
        f.close()
    return res


def part1(f):
    prev, ans = 1e18, 0
    for x in f:
        if x > prev:
            ans += 1
        prev = x
    print(ans)


def part2(f):
    prev, ans = 1e18, 0
    for i in range(len(f) - 2):
        tot = sum(f[i:i+3])
        if tot > prev:
            ans += 1
        prev = tot
    print(ans)


def main():
    f = read()
    part1(f)
    part2(f)


main()

