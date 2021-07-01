list = [int(x) for x in input().split()]
pos = []
minPos = 0

for i in range(len(list)):
    if list[i] >= 0:
        pos.append(list[i])

for i in range(len(pos)):
    if i == 0:
        minPos = pos[i]
    if minPos > pos[i]:
        minPos = pos[i]

print(minPos)
