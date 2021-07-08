import re

address = re.compile(r'г\..*')

f = open('doc.txt', 'r')
txt = f.read()

res = re.search(address, txt)
print(res.group())

f.close()
