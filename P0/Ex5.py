from Seq0 import *

FOLDER = "../Session-04/"
FILENAME = "U5.txt"
FILENAME2= "ADA.txt"
FILENAME3= "FRAT1.txt"
FILENAME4 = "FXN.txt"

genes = [FILENAME, FILENAME2, FILENAME3, FILENAME4 ]
for gene in genes:
    seq= seq_read_fasta(FOLDER + gene)
    print()
    print(f"Gene {gene}:")
    print(seq_count(seq))
