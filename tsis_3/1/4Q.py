list = [int(x) for x in input().split()]

for i in range(len(list)):
    if list[i] == 0:
        j = len(list) - 1
        while j > i:
            if (list[j] != 0):
                temp = list[i]
                list[i] = list[j]
                list[j] = temp
            j -= 1

for i in list:
    print(i)
