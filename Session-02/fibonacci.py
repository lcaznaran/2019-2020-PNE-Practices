
number = 11
x1 = 0
x2 = 1

if number >= 1:
    print (x1)
if number >=2:
    print(x2)
if number >=3:
    for n in range (3, number + 1):
        xn = x1 + x2
        print (xn)
        x1 = x2
        x2 = xn