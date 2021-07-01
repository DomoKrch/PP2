listF = [int(x) for x in input().split()]
listS = [int(x) for x in input().split()]
cnt = 0

for i in listF:
     if i in listS: cnt += 1

print(cnt)
