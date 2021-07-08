def countCh(s):
    l = 0
    cap = 0

    for i in s:
        if i >= 'a' and i <= 'z':
            l += 1
        if i >= 'A' and i <= 'Z':
            cap += 1

    print("lower: {}, capital: {}".format(l, cap))

s = input()
countCh(s)
