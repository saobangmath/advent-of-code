from collections import defaultdict

g = defaultdict(lambda : [])


def check(s):
    c = ord(s[0]) - ord('a')
    return c >= 0 and c < 26


# part 1 just more easy...
# part 2
def dfs(start, goal, d, canTwice):
    if start == goal:
        return 1
    else:
        cnt = 0
        for v in g[start]:
            if v == "start":
                continue
            if v in d.keys():
                if canTwice:
                    new_d = defaultdict()
                    for key in d.keys():
                        new_d[key] = d[key]
                    new_d[v] = 2
                    cnt += dfs(v, goal, d, False)

            elif check(v):
                new_d = defaultdict()
                for key in d.keys():
                    new_d[key] = d[key]
                new_d[v] = 1
                cnt += dfs(v, goal, new_d, canTwice)
            else:
                cnt += dfs(v, goal, d, canTwice)

        return cnt


def main():
    with open('input.txt.txt') as f:
        for x in f:
            if x[-1] == '\n': x = x[:-1:]
            u, v = x.split("-")
            g[u].append(v)
            g[v].append(u)
    d = defaultdict(lambda : 0)
    print(dfs("start", "end", d, True))
    pass


main()