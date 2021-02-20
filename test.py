from sys import argv

s, f = argv
o = open(f)
o.seek(1)
print(o.readline())
#print(o.readline())
