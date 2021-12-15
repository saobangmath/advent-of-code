from functools import reduce


def read() -> list[tuple[int]]:
    res = []
    with open("input.txt.txt") as f:
        for _ in f:
            op, change = _.split(" ")
            change = int(change)
            if op == "forward":
                res.append((0, change))
            if op == "down":
                res.append((1, change))
            if op == "up":
                res.append((1, -change))
        f.close()
    return res


def part1(changes):
    dims = [0, 0]
    for change in changes:
        dims[change[0]] += change[1]
    print(reduce(lambda u, v: abs(u) * abs(v), dims))


def part2(changes):
    dims = [0, 0]
    aim = 0
    for change in changes:
        if change[0] == 1:
            aim += change[1]
        else:
            dims[0] += change[1]
            dims[1] += change[1] * aim
    print(reduce(lambda u, v: abs(u) * abs(v), dims))


def main():
    changes = read()
    part1(changes)
    part2(changes)


main()