lines = []
boards = [[0 for i in range(1000)] for _ in range(1000)]
cnt = 0


def read():
    with open('input.txt', 'r') as f:
        for x in f:
            left, right = x.split(" -> ")
            x1, y1 = [int(_) for _ in left.split(",")]
            x2, y2 = [int(_) for _ in right.split(",")]
            lines.append([[x1, y1], [x2, y2]])


def part1():
    global cnt
    for line in lines:
        if line[0][0] == line[1][0]:
            m = min(line[0][1], line[1][1])
            M = max(line[0][1], line[1][1])
            for _ in range(m, M+1):
                boards[line[0][0]][_] += 1

        if line[0][1] == line[1][1]:
            m = min(line[0][0], line[1][0])
            M = max(line[0][0], line[1][0])
            for _ in range(m, M+1):
                boards[_][line[1][1]] += 1

    for r in range(1000):
        for c in range(1000):
            cnt += max(0, min(boards[r][c] - 1, 1))

    print(cnt)


def part2():
    global cnt
    cnt = 0
    for line in lines:
        x1, y1, x2, y2 = line[0][0], line[0][1], line[1][0], line[1][1]
        if abs(x2-x1) == abs(y1-y2):
            dx = (x2-x1) // abs(x2-x1)
            dy = (y2-y1) // abs(y2-y1)
            while x1 != x2:
                boards[x1][y1] += 1
                x1 += dx
                y1 += dy

            boards[x1][y1] += 1

    for r in range(1000):
        for c in range(1000):
            cnt += max(0, min(boards[r][c] - 1, 1))

    print(cnt)


def main():
    read()
    part1()
    part2()


main()
