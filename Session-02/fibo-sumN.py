
def fibosum(n):
    sumf = 0
    x1 = 0
    x2 = 1
    if n >= 1:
        sumf += x1
    if n >= 2:
        sumf += x2
    if n >= 3:
        for n in range(3, n + 1):
            xn = x1 + x2
            sumf += xn
            x1 = x2
            x2 = xn
    return sumf


print("sum of the first 5 terms of the fibonacci series: ", fibosum(6))
print("sum of the first 10 terms of the fibonacci series: ", fibosum(11))
