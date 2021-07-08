list = [int(x) for x in input().split()]
max = list[0]

for i in list:
    if (max < i):
        max = i

print(max)
