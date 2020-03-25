seq = input("Introduce the sequence: ")

a = 0
t = 0
c = 0
g = 0

for b in seq:
    if b == "A":
        a += 1
    if b == "C":
        c +=1
    if b == "G":
        g +=1
    if b == "T":
        t +=1

total_length = a + t + c + g

print("Total length:", total_length)
print("A:", a)
print("C:", c)
print("G:", g)
print("T:", t)