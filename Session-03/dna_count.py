dna = input("Insert a dna sequence: ")


def countera(seq):
    counta = 0
    for i in seq:
        if i == "A":
            counta += 1
    return counta


def countert(seq):
    countt = 0
    for i in seq:
        if i == "T":
            countt += 1
    return countt


def counterc(seq):
    countc = 0
    for i in seq:
        if i == "C":
            countc += 1
    return countc


def counterg(seq):
    countg = 0
    for i in seq:
        if i == "G":
            countg += 1
    return countg


print("Total length: ", len(dna))
print("A:", countera(dna))
print("T:", countert(dna))
print("C:", counterc(dna))
print("G:", counterg(dna))
