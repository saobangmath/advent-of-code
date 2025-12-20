from functools import lru_cache

g = []
who = []
split = 0 

def dfs(r, c): 
    global split
    if r == len(g):
        return 

    assert(r < len(who) and c < len(who[0]))
    if who[r][c]: 
        return  
    
    who[r][c] = 1
    if g[r][c] == '^':
        split += 1
        if c + 1 < len(g[0]): 
            dfs(r, c + 1)
        if c - 1 >= 0: 
            dfs(r, c - 1)
    else:
        dfs(r + 1, c)

def read():
    with open('input.txt', 'r') as f:
        for line in f:
            g.append([_ for _ in line.strip()])

def part1():     
    global who
    h, w = len(g), len(g[0])
    who = [[0 for _ in range(len(g[0]))] for _ in range(len(g))]
    for c in range(w):
        if g[0][c] == 'S':
            dfs(0, c)
            break

    print(split) 

@lru_cache()
def dfs2(r, c):
    if c < 0 or c >= len(g[0]):
        return 0 
    
    if r == len(g):
        return 1 
    
    if g[r][c] != '^':
        return dfs2(r + 1, c)
    else:
        return dfs2(r, c + 1) + dfs2(r, c - 1)

def part2():
    for c in range(len(g[0])):
        if g[0][c] == 'S':
            print(dfs2(0, c))

read()
# part1()
part2()