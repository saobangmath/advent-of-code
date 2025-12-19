mode=0 

ranges = []
ingredients=set()

with open('input.txt', 'r') as f:
    for line in f:
        line = line.strip()
        if len(line) == 0:
            mode=1 
            continue 

        if mode == 0: 
            l = line.split("-")
            ranges.append((int(l[0]), int(l[1])))
        else:
            ingredients.add(int(line))

cnt=0
for i in ingredients: 
    ok=False
    for r in ranges:
        if i >= r[0] and i <= r[1]:
            ok = True
            break 
    cnt += 1 if ok else 0

ranges.sort() 
merged_ranges = []
for r in ranges:
    if merged_ranges and merged_ranges[-1][1] >= r[0]:
        merged_ranges[-1][1] = max(merged_ranges[-1][1], r[1])
    else:
        merged_ranges.append([r[0], r[1]])

fresh_cnt = 0 
for r in merged_ranges:
    fresh_cnt += r[1] - r[0] + 1

print(cnt)
print(fresh_cnt)