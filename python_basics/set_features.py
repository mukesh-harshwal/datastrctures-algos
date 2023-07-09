s={10,20,30,"XYZ",10,20,30}

s.update([88,99])
print(s)
s.remove("XYZ")
print("after removal ",s)
s.add(89)
print(s)
for e in s:
    print(e)

f = frozenset(s)
print(type(s))
print(type(f))
