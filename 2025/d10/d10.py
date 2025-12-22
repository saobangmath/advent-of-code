#from z3 import *
# Day 10 solution without using z3

class Prob: 
    def __init__(self, target_state, ops, clicks):
        self.target_state = target_state
        self.ops = ops
        self.clicks = clicks
        self.memo = dict()

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
        return self.helper(self.clicks)
    
    def helper(self, clicks):
        s = str(clicks)
        if s in self.memo:
            return self.memo[s]

        if sum(clicks) == 0:
            return 0 
        
        res = 1000000
        for mask in range(1 << len(self.ops)): 
            bit_cnt = 0 
            _clicks = [_ for _ in clicks]
            for i in range(len(self.ops)):
                if mask & (1 << i):
                    bit_cnt += 1
                    for j in range(len(self.clicks)):
                        if self.ops[i] & (1 << j):
                            _clicks[j] -= 1
            ok = True
            for i in range(len(clicks)):
                if _clicks[i] < 0 or _clicks[i] % 2 == 1:
                    ok = False
                    break
                else:
                    _clicks[i] >>= 1 
            if ok:
                res = min(res, bit_cnt + self.helper(_clicks) * 2)

        self.memo[s] = res
        return res

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
        res += p.solve1()
    print(res)

def part2():
    res = 0
    i = 0
    for p in probs:
        res += p.solve2()
        i += 1
    print(res)

probs = load()
part1()
part2()