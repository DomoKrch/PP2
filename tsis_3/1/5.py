from collections import deque

list = deque([int(x) for x in input().split()])
n = int(input())

list.rotate(n)
for i in list:
    print(i)
