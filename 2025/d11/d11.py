# Day 11 solution

from collections import defaultdict
from functools import lru_cache

def load(): 
    g = defaultdict(lambda: [])
    with open('input.txt', 'r') as f:
        for line in f:
            lst = line.strip().split(" ")
            u = lst[0][:len(lst[0])-1:]
            for v in lst[1:]:
                if u not in g:
                    g[u] = []
                g[u].append(v)
    return g

def part1(g):
    @lru_cache(maxsize=None)
    def calc1(u):
        res = 0
        if u == "out":
            res = 1
        else:
            for v in g[u]:
                res += calc1(v)

        return res

    return calc1("you")

def part2(g):
    @lru_cache(maxsize=None)
    def calc2(u, st):
        res = 0
        if u == "out":
            return 1 if st == 3 else 0
        
        for v in g[u]:
            nst = st
            if v == "dac":
                nst |= (1 << 0)
            if v == "fft":
                nst |= (1 << 1)
            res += calc2(v, nst)
        return res 

    return calc2("svr", 0)

if __name__ == '__main__':
    g = load()
    print(part1(g))
    print(part2(g))
