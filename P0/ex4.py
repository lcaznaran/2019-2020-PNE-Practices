from Seq0 import *

FOLDER = "../Session-04/"
FILENAME = "U5.txt"
FILENAME2= "ADA.txt"
FILENAME3= "FRAT1.txt"
FILENAME4 = "FXN.txt"

genes = [FILENAME, FILENAME2, FILENAME3, FILENAME4 ]
BASES = ['A', 'C', 'T', 'G']

for gene in genes:
    seq= seq_read_fasta(FOLDER + gene)
    print()
    print(f"Gene {gene}:")
    for base in BASES:
        print(f" {base}: {seq_count_base(seq, base)}")