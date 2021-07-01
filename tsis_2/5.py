n = int(input())
su = 0
pr = 1
s = str(n)

for i in range(len(s)):
    pr *= int(s[i])
    su += int(s[i])

print(pr - su)
