topX, topY, botX, botY = 206, -68, 169, -108
def main():
    global topX, topY, botX, botY
    def simulate(speed_x, speed_y):
        ans = 0
        found = False
        startX, startY = 0,0
        while True:
            startX += abs(speed_x)
            startY += speed_y
            speed_y -= 1
            speed_x = max(0, speed_x-1)
            ans = max(ans, startY)
            if startX <= topX and startX >= botX and startY <= topY and startY >= botY:
                found = True
                break
            if startX > topX or startY < botY:
                break
        if found:
            return ans
        return -1
    # part 1: highest_y
    # part 2: how many initial velocity that the probe to be within the target area
    highest_y, options = 0, 0
    for speed_x in range(1, 301):
        for speed_y in range(-169, 169):
            f = simulate(speed_x, speed_y)
            highest_y = max(highest_y, f)
            if f!=-1: options+=1

    print(highest_y, options)
    pass
main()