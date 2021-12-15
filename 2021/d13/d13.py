b = []

def isDigit(c):
    return ord(c) >= ord('0') and ord(c) <= ord('9')


def mergeByX(x):
    global b
    new_b = [[0 for _ in range(len(b[0]))] for __ in range(min(x, len(b) - x))]
    p1,p2 = x-1,x
    for c in range(len(new_b[0])):
        for r in range(len(new_b)):
            if p1 >= 0 and p2 < len(b):
                new_b[r][c] = max(b[p1][c], b[p2][c])
                p1 -= 1
                p2 += 1
            elif p1 >= 0:
                new_b[r][c] = b[p1][c]
                p1 -= 1
            elif p2 < len(b):
                new_b[r][c] = b[p2][c]
                p2 += 1
    b = new_b
    print(sum([sum(_) for _ in b]))



def mergeByY(y):
    global b
    new_b = [[0 for _ in range(min(y, len(b[0]) - y))] for __ in range(len(b))]
    p1, p2 = y - 1, y
    for r in range(len(new_b)):
        for c in range(len(new_b[0])):
            if p1 >= 0 and p2 < len(b[0]):
                new_b[r][c] = max(b[r][p1], b[r][p2])
                p1 -= 1
                p2 += 1
            elif p1 >= 0:
                new_b[r][c] = b[r][p1]
                p1 -= 1
            elif p2 < len(b[0]):
                new_b[r][c] = b[r][p2]
                p2 += 1
    b = new_b
    print(sum([sum(_) for _ in b]))


def main():
    global b
    with open('input.txt.txt') as f:
        for line in f:
            if line[-1] == '\n':
                line = line[:-1:]
            if isDigit(line[0]):
                x, y = [int(_) for _ in line.split(",")]
                b[x][y] = 1

            else:
                line = line.replace("fold along ", "")
                if line[0] == 'x':
                    mergeByX(int(line[2::]))
                else:
                    mergeByY(int(line[2::]))
    pass
main()
