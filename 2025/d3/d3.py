def part1(): 
    ans = 0 

    with open('input.txt', 'r') as f:
        for line in f:
            line = line.strip()
            mx = 0 
            md = 0 
            for d in line:
                mx = max(mx, md * 10 + int(d))
                md = max(md, int(d))
            ans += mx
    print(ans)

def part2(): 
    ans = 0 

    with open('input.txt', 'r') as f:
        for line in f:
            line = line.strip()
            dp = [0 for _ in range(13)] 
            for d in line: 
                for i in range(11, -1, -1):
                    dp[i+1] = max(dp[i+1], dp[i] * 10 + int(d))
            ans += dp[12]
            
    print(ans)

part2()