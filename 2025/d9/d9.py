# Day 9 solution
def read():
    with open('input.txt', 'r') as f:
        return [list(map(int, line.strip().split(','))) for line in f]

def part1(g):
    res = 0
    for i in range(len(g)):
        for j in range(i + 1, len(g)):
            dx = max(g[i][0], g[j][0]) - min(g[i][0], g[j][0]) + 1 
            dy = max(g[i][1], g[j][1]) - min(g[i][1], g[j][1]) + 1 
            res = max(res, dx * dy) 
    
    print(res)

# 4595056840
def part2(g):
    res = 0
    x_to_y_ranges = dict()
    y_to_x_ranges = dict()
    
    for i in range(len(g)):
        if g[i][0] not in x_to_y_ranges:
            x_to_y_ranges[g[i][0]] = (g[i][1], g[i][1])
        
        if g[i][1] not in y_to_x_ranges:
            y_to_x_ranges[g[i][1]] = (g[i][0], g[i][0])

        x_to_y_ranges[g[i][0]] = (min(x_to_y_ranges[g[i][0]][0], g[i][1]), max(x_to_y_ranges[g[i][0]][1], g[i][1]))
        y_to_x_ranges[g[i][1]] = (min(y_to_x_ranges[g[i][1]][0], g[i][0]), max(y_to_x_ranges[g[i][1]][1], g[i][0]))

    l1 = list(x_to_y_ranges.items())
    l2 = list(y_to_x_ranges.items())

    for x, v in l1:
        for y in range(v[0], v[1] + 1):
            if y not in y_to_x_ranges.keys():
                y_to_x_ranges[y] = (x, x)

            y_to_x_ranges[y] = (min(y_to_x_ranges[y][0], x), max(y_to_x_ranges[y][1], x))

    for y, v in l2:
        for x in range(v[0], v[1] + 1):
            if x not in x_to_y_ranges.keys():
                x_to_y_ranges[x] = (y, y)

            x_to_y_ranges[x] = (min(x_to_y_ranges[x][0], y), max(x_to_y_ranges[x][1], y))


    for i in range(len(g)):
        for j in range(i + 1, len(g)):
            ok = True
            for x in [g[i][0], g[j][0]]:  
                for y in [g[i][1], g[j][1]]:
                    if not (y >= x_to_y_ranges[x][0] and 
                            y <= x_to_y_ranges[x][1] and  
                            x >= y_to_x_ranges[y][0] and 
                            x <= y_to_x_ranges[y][1]):
                        ok = False
                        break

            if not ok:
                continue

            dx = max(g[i][0], g[j][0]) - min(g[i][0], g[j][0]) + 1 
            dy = max(g[i][1], g[j][1]) - min(g[i][1], g[j][1]) + 1 

            res = max(res, dx * dy) 
    
    print(res)

if __name__ == '__main__':
    g = read()
    m1 = dict(), m2 = dict()
    for r in g: 
        
    # part1(g)
    part2(g)