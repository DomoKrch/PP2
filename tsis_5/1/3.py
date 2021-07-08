f = open("text.txt", "a")

f.write("The following message is appended")

f.close()

f = open("text.txt", "r")

print(f.read())
