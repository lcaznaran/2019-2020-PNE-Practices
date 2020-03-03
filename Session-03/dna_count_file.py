from pathlib import Path

file = Path("dna")

print("File:", file)

data = file.read_text()

print("Data: ", data)

# -- Initialize the bases counters
a = 0
t = 0
c = 0
g = 0
spa = 0

for b in data:
    if b == 'A':
        a += 1
    elif b == 'T':
        t += 1
    elif b == 'C':
        c += 1
    elif b == 'G':
        g += 1
    else:
        spa += 1

total_length = a + t + c + g

# Print the results:
print("Total length: {}".format(total_length))
print("A:", a)
print("C:", c)
print("T:", t)
print("G:", g)
print("Unk:", spa)  #blank spaces
