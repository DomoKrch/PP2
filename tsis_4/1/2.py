import re

bin = re.compile(r'(?<=БИН\s).*')

f = open('doc.txt', 'r')
txt = f.read()

res = re.search(bin, txt)
print(res.group())

f.close()
