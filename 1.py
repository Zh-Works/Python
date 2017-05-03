def countdown():
    i=5
    while i>0:
        yield i
        i -= 1
print (countdown())

for a in countdown():
    print(a+3)
