# Day 10 solution

class Prob: 
    def __init__(self, target_state, ops, clicks):
        self.target_state = target_state
        self.ops = ops
        self.clicks = clicks

    def __str__(self):
        return f"Target State: {self.target_state}, Ops: {self.ops}, Clicks: {self.clicks}"

    def solve1(self):
        dp = dict()
        dp[0] = 0
        for op in self.ops: 
            ndp = dp.copy()
            for k in dp.keys(): 
                nk = k ^ op
                if nk not in ndp:
                    ndp[nk] = dp[k] + 1
                ndp[nk] = min(ndp[nk], dp[k] + 1)
            dp = ndp

        return dp[self.target_state]


    def solve2(self):
        return 0

def load():
    probs = []
    with open('input.txt', 'r') as f:
        for line in f: 
            target_state, clicks, ops = 0, [], []
        
            line = line.strip()
            lst = line.split(" ")

            i  = 0

            for e in lst:
                e = e[1:len(e)-1]
                if i == 0:
                    for j in range(len(e)):
                        if e[j] == '#':
                            target_state |= (1 << j)
                elif i == len(lst) - 1:
                    clicks = [(int)(_) for _ in e.split(",")]
                else:
                   ll = [(int)(_) for _ in e.split(",")]
                   st=0
                   for _ in ll:
                    st |= (1 << _)
                   ops.append(st)
                i += 1
        
            probs.append(Prob(target_state, ops, clicks))
    return probs 

def part1():
    res = 0 
    for p in probs:
        print(p)
        res += p.solve1()
    print(res)

def part2():
    res = 0
    for p in probs:
        res += p.solve2()
    print(res)

probs = load()
part1()
part2()