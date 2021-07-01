listF = [int(x) for x in input().split()]
listS = [int(x) for x in input().split()]
final = []

for i in listF:
    if i in listS:
        final.append(i)

final.sort()

for i in final:
    print(i)
