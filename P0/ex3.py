from Seq0 import *

FOLDER = "../Session-04/"
FILENAME = "U5.txt"
FILENAME2= "ADA.txt"
FILENAME3= "FRAT1.txt"
FILENAME4 = "FXN.txt"

genes = [FILENAME, FILENAME2, FILENAME3, FILENAME4 ]

for i in range(len(genes)):
    DNA = FOLDER + genes[i]
    lenght = seq_len(DNA)
    print(f"Gene {genes[i]} --> Lenght: {lenght}")
    i += 1
    if i == 4:
        break
