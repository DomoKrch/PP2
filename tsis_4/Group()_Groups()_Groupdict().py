import re

noDup = True
s = input()

for i, ch in enumerate(s):
    if ch.isalnum():
        if i + 1 != len(s):
            if s[i] == s[i+1]:
                noDup = False
                print(ch)
                break
            else:
                continue


if noDup:
    print(-1)
