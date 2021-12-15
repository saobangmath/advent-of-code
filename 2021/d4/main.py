from functools import reduce

moves = []
boards = []
d = dict()
N = 5


def read():
    global moves
    with open('input.txt.txt', 'r') as f:
        moves = [int(_) for _ in f.readline().split(",")]
        stop = False
        id = 0
        while not stop:
            f.readline()
            boards.append([])
            for row in range(N):
                x = f.readline().strip().replace("  ", " ")
                if not x:
                    stop = True
                    break
                boards[id].append([int(_) for _ in x.split(" ")])
            id += 1
        boards.pop()
        f.close()


def check(board):
    for row in range(N):
        if sum([1 if board[row][col] in d.keys() else 0 for col in range(N)]) == N:
            return True
    for col in range(N):
        if sum([1 if board[row][col] in d.keys() else 0 for row in range(N)]) == N:
            return True
    return False


def get_sum(board):
    return sum([sum([__ for __ in _ if __ not in d.keys()]) for _ in board])


def part1():
    tot = 0
    for move in moves:
        tot += move
        found = False
        d[move] = 1
        for board in boards:
            if check(board):
                print(move * (get_sum(board)))
                found = True
                break
        if found:
            break


def part2():
    tot = 0
    win = [False for _ in range(len(boards))]
    latest_score = 0
    for move in moves:
        tot += move
        d[move] = 1
        for id in range(len(boards)):
            board = boards[id]
            if not win[id] and check(board):
                latest_score = move * (get_sum(board))
                win[id] = True

    print(latest_score)


def main():
    read()
    part1()
    part2()


main()
