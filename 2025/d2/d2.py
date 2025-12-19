def bad(n):
    n = str(n)
    if len(n) % 2 == 1:
        return False
    
    return n[:len(n)//2] == n[len(n)//2:]

def bad2(n):
    n = str(n)
    for i in range(1, len(n) // 2 + 1):
        if len(n) % i > 0:
            continue 
        
        allEq = True
        for s in range(0, len(n), i):
            if n[s:s+i] != n[0:i]:
                allEq = False
                break 
        if allEq:
            return True
    return False

tot = 0 

with open('input.txt', 'r') as f:
    for line in f:
        l = line.split(',')
        for r in l:
            ll = r.split('-')
            s, e = int(ll[0]), int(ll[1])
            for d in range(s, e + 1):
                
                if bad2(d):
                    tot += d
                    
print(tot)