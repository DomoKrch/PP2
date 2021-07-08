def fact(num, res):
    if num == 1:
        print(res)
        return

    res *= num - 1
    num = num - 1
    fact(num, res)

num = int(input())

fact(num + 1, 1)
