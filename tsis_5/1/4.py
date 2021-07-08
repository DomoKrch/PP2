f = open("text.txt", "r")

lines = f.readlines()
last = lines[-1:]
print(last)

f.close()
