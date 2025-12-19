from functools import reduce

def part1(): 
    with open('input.txt', 'r') as f:
        vals = []
        tot = 0 
        for line in f:
            ll = line.strip().split(" ")
            vals.append([_ for _ in ll if _])
        
        tot = 0
        for c in range(len(vals[0])):
            match vals[-1][c]:
                case '+':   
                    res=0
                    for r in range(len(vals) - 1):
                        res += int(vals[r][c])
                    tot += res
                case '*':
                    res=1
                    for r in range(len(vals) - 1):
                        res *= int(vals[r][c])
                    tot += res

        print(tot)

def part2(): 
    with open('input.txt', 'r') as f:
        vals = []
        tot = 0 
        for line in f:
            vals.append(line)
        
        for c in range(len(vals[-1])):
            op = vals[-1][c]
            if op == ' ':
                continue
            
            params = []
            for c1 in range(c, 10000): 
                v = 0
                for r in range(len(vals) - 1):
                    if c1 >= len(vals[r]) or not vals[r][c1].isdigit():
                        continue

                    v = v * 10 + int(vals[r][c1])
                    
                if v == 0:
                    break
                params.append(v)

            print(op, params)
            match op:
                case '+':
                    tot += reduce(lambda x, y: x + y, params)
                case '*':
                    tot += reduce(lambda x, y: x * y, params)
        print(tot)
part2()