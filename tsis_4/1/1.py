import re

company = re.compile(r'(?<=Филиал\s)\w*\s\w*(?<=\w)')

f = open('doc.txt', 'r')
txt = f.read()

res = re.search(company, txt)
print(res.group())

f.close()
