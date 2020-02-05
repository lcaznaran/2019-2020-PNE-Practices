def fibon(number):
    x1 = 0
    x2 = 1
    listoff= []
    if number >= 1:
        listoff.append(x1)
    if number >=2:
        listoff.append(x2)
    if number >=3:
        for n in range (3, number + 1):
            xn = x1 + x2
            listoff.append(xn)
            x1 = x2
            x2 = xn
    return listoff
fibonacci = fibon(20)
print("The 5th fibonacci number is:", fibonacci[5])
print("The 10th fibonacci number is:", fibonacci[10])
print("The 15th fibonacci number is:",fibonacci[15])