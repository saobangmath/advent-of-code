def part1(): 
    cur = 50
    pw = 0 
    with open('input.txt', 'r') as f:
        for line in f:
            dir, d = line[0], int(line[1:])
            if dir == 'L':
                cur = (cur - d + 100) % 100
            else:
                cur = (cur + d)  % 100
            if cur == 0: 
                pw += 1
    print(pw)

def part2(): 
    cur = 50
    pw = 0 
    with open('input.txt', 'r') as f:
        for line in f:
            dir, d = line[0], int(line[1:])
            pw += d // 100
            d %= 100
            if dir == 'L':
                if cur != 0 and cur <= d:
                    pw += 1 
                
                cur = (cur - d + 100) % 100

            else:   
                if cur!=0 and cur + d >= 100:
                    pw += 1 

                cur = (cur + d)  % 100
            
    print(pw)

def main():
    part2()

main()