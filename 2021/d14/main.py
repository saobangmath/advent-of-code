from collections import defaultdict
s = ""

d = defaultdict(lambda : "")
ITERS = 40
dp = [defaultdict(lambda:defaultdict(lambda : 0)) for _ in range(ITERS + 1)]


def calc(s: str, iter: int):
    if len(dp[iter][s]):
        return dp[iter][s]
    if iter == 0:
        dp[iter][s][s[0]] = 1
        dp[iter][s][s[1]] += 1
        return dp[iter][s]
    if s in d.keys():
        left = calc(s[0] + d[s], iter-1)
        right = calc(d[s] + s[1], iter-1)
        for x in left.keys():
            dp[iter][s][x] += left[x]
        for x in right.keys():
            dp[iter][s][x] += right[x]
        dp[iter][s][d[s]] -= 1
    else:
        assert(False)
        dp[iter][s] = calc(s, iter-1)
    return dp[iter][s]


def main():
    global s
    with open('input.txt') as f:
        for x in f:
            if x[-1] == '\n':
                x = x[:-1:]
            if s == "":
                s = x
            else:
                u, v = x.split(" -> ")
                d[u] = v

    big = defaultdict(lambda: 0)
    for i in range(0, len(s) - 1):
        f = calc(s[i:i+2:], ITERS)
        for x in f.keys():
            big[x] += f[x]
        if i:
            big[s[i]] -= 1

    print(big)
    print(max([_ for _ in big.values()]) - min([_ for _ in big.values()]))
    pass


main()