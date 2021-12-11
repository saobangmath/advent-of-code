a = [   "8271653836",
        "7567626775",
        "2315713316",
        "6542655315",
        "2453637333",
        "1247264328",
        "2325146614",
        "2115843171",
        "6182376282",
        "2384738675"]

b=["5483143223",
"2745854711",
"5264556173",
"6141336146",
"6357385478",
"4167524645",
"2176841721",
"6882881134",
"4846848554",
"5283751526"]

dirs = [[0,1],[0,-1],[1,0],[-1,0], [1,-1], [1,1],[-1,-1], [-1,1]]

def main():
    cnt=0
    q = []
    time = 0
    # part 1
    for iter in range(100):
        for r in range(10):
            a[r] = [int(_) for _ in a[r]]
        for r in range(10):
            for c in range(10):
                a[r][c] += 1
                if a[r][c]==10: q.append([r, c])
        while q:
            f = q.pop()
            cnt+=1
            for dir in dirs:
                new_x,new_y=f[0]+dir[0], f[1]+dir[1]
                if new_x>=0 and new_y>=0 and new_x<10 and new_y<10:
                    if a[new_x][new_y] <= 9:
                        a[new_x][new_y]+=1
                        if a[new_x][new_y] == 10:
                            q.append([new_x,new_y])

        for r in range(10):
            for c in range(10):
                if a[r][c] > 9: a[r][c] = 0
    print(cnt)
    # part 2
    for iter in range(1,100000):
        for r in range(10):
            a[r] = [int(_) for _ in a[r]]
        for r in range(10):
            for c in range(10):
                a[r][c] += 1
                if a[r][c] == 10: q.append([r, c])
        while q:
            f = q.pop()
            cnt += 1
            for dir in dirs:
                new_x, new_y = f[0] + dir[0], f[1] + dir[1]
                if new_x >= 0 and new_y >= 0 and new_x < 10 and new_y < 10:
                    if a[new_x][new_y] <= 9:
                        a[new_x][new_y] += 1
                        if a[new_x][new_y] == 10:
                            q.append([new_x, new_y])

        ok = True
        for r in range(10):
            for c in range(10):
                if a[r][c] > 9:
                    a[r][c] = 0
                else:
                    ok = False

        if ok:
            print(iter+100)
            break
    pass

main()