list = [int(x) for x in input().split()]
prod = list[0]

for i in list:
    prod *= i

print(prod)
