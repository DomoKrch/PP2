import re

title = re.compile(r'(?<=\d\.\n).*')
t_pr = re.compile(r'(?<=Стоимость\n).*')

f = open('doc.txt', 'r')
txt = f.read()

tiRes = re.findall(title, txt)
print(tiRes)

tPrRes = re.findall(t_pr, txt)
print(tPrRes)

f.close()
