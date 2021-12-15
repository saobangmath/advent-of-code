g = []
dirs = [[0,1],[0,-1], [1,0],[-1,0]]
tot = 0

def main():
    with open('input.txt.txt') as f:
        for x in f:
            if x[-1] == "\n":
                x = x[:-1:]
            g.append([int(_) for _ in x])

    # part 1
    cnt = 0
    for r in range(len(g)):
        for c in range(len(g[0])):
            ok = True
            for dir in dirs:
                new_r, new_c = r + dir[0], c + dir[1]
                if new_r >= 0 and new_c >= 0:
                    if new_r < len(g) and new_c < len(g[0]):
                        if g[new_r][new_c] <= g[r][c]:
                            ok = False
                            break
            if ok:
                cnt += g[r][c] + 1
    print(cnt)
    # part 2
    basins = []
    vis = [[False for i in range(len(g[0]))] for j in range(len(g))]

    def dfs(r,c):
        tot = 0
        if vis[r][c] or g[r][c] == 9:
            return 0
        vis[r][c] = True
        tot += 1
        for dir in dirs:
            new_r, new_c = r + dir[0], c + dir[1]
            if new_r>=0 and new_c>=0 and new_r < len(g) and new_c < len(g[0]) and g[new_r][new_c] != 9:
                tot += dfs(new_r, new_c)
        return tot

    for r in range(len(g)):
        for c in range(len(g[0])):
            tot = dfs(r, c)
            if tot: basins.append(tot)

    basins.sort()
    print(basins)
    print(basins[-1] * basins[-2] * basins[-3])



main()