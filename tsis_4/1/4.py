import re

time = re.compile(r'(?<=Время:\s).*')

f = open('doc.txt', 'r')
txt = f.read()

res = re.search(time, txt)
print(res.group())

f.close()
