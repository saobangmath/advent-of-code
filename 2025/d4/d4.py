g = []

dr = [1,1,1,0,0,-1,-1,-1]
dc = [1,0,-1,1,-1,1,0,-1]

res=0

with open('input.txt', 'r') as f:
    for line in f:
       g.append([_ for _ in line.strip()])

    h, w = len(g), len(g[0])
    changed = True 
    while changed:  
        toDel = [] 
        for r in range(h):
            for c in range(w):
                cnt=0
                if g[r][c] != '@':
                    continue
                for i in range(8):
                    nr = r + dr[i]
                    nc = c + dc[i]
                    if nr >= 0 and nr < h and nc >= 0 and nc < w and g[nr][nc] == '@': 
                        cnt += 1
                
                if cnt <4: 
                    res += 1
                    toDel.append((r, c))

        for r, c in toDel:
            g[r][c] = '.'

        changed = len(toDel) > 0

print(res)

        