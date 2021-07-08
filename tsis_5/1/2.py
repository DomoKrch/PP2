f = open("text.txt", "r")

lines = [next(f) for x in range(1)]
print(lines)

f.close()
