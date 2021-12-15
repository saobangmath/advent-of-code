import sys
import heapq

def main():
    b = []
    dp = []
    dirs = [[0,1],[1,0],[0,-1],[-1,0]]

    def next(num):
        num+=1
        if num==10:num-=9
        return num

    with open('input.txt') as f:
        for x in f:
          if x[-1]=='\n':
              x = x[:-1:]
          b.append([int(_) for _ in x])

        w = len(b[0])
        for r in range(len(b)):
            for c in range(w, 5 * w):
                b[r].append(next(b[r][c-w]))

        h = len(b)
        for r in range(h, 5 * h):
            b.append([])
            for c in range(len(b[0])):
                b[r].append(next(b[r-h][c]))

        dp = [[9e18 for _ in range(len(b[0]))] for __ in range(len(b))]

        pq = []
        h, w = len(b), len(b[0])
        dp[h-1][w-1] = b[h-1][w-1]
        heapq.heappush(pq, [b[h-1][w-1],[h-1, w-1]])
        while len(pq):
            top = heapq.heappop(pq)
            # print(top)
            x,y = top[1][0], top[1][1]
            if x==0 and y==0:
                print(top[0])
                break
            if (top[0] > dp[x][y]):
                continue
            for dir in dirs:
                new_x = x+dir[0]
                new_y = y+dir[1]
                if new_x>=0and new_y>=0 and new_x<h and new_y<w and dp[new_x][new_y]>top[0] + b[new_x][new_y]:
                    dp[new_x][new_y] = top[0] + b[new_x][new_y]
                    heapq.heappush(pq, [dp[new_x][new_y], [new_x, new_y]])
    pass


main()
