from collections import defaultdict

DD = ["abcefg", "cf", "acdeg", "acdfg", "bcdf",
     "abdfg", "abdefg", "acf", "abcdefg", "abcdfg"]


decoder = dict()


def get(s):
    s = ''.join(sorted([decoder[_] for _ in s]))
    for d in range(10):
        if DD[d] == s:
            return d
    return -1

def fuck(x, d):
    for _ in x:
        if (len(_)==d): return _
    return ""

def main():
    tot = 0
    with open("input.txt.txt") as f:
        for x in f:
            if x[-1] == '\n': x = x[:-1:]
            x = x.split("|")
            num=0
            decoder.clear()
            counter = defaultdict(lambda:0)
            info = x[0].split(" ")
            for _ in info:
                for c in _:
                    counter[c]+=1
            for key in counter.keys():
                val=counter[key]
                if val==4:decoder[key] = 'e'
                elif val==6: decoder[key] = 'b'
                elif val==9: decoder[key] = 'f'
            # 1
            for c in fuck(info, 2):
                if c not in decoder.keys():
                    decoder[c] = 'c'
                    break
            # 4
            for c in fuck(info, 4):
                if c not in decoder.keys():
                    decoder[c] = 'd'
                    break
            # 7
            for c in fuck(info, 3):
                if c not in decoder.keys():
                    decoder[c] = 'a'
                    break
            #8
            for c in fuck(info, 7):
                if c not in decoder.keys():
                    decoder[c] = 'g'
                    break
            print(decoder)
            for _ in x[1].split(" "):
                if _:
                    num=num*10+get(_)
            tot+=num

    print(tot)


main()
