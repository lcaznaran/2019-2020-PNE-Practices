from Seq0 import *

gene = "U5.txt"
FOLDER = "../Session-04/"
seq= seq_read_fasta(FOLDER + gene)
seqn = seq[:20]
print("Gene", gene)
print(f"Frag: {seqn}")
print(f"Rev: {seq_reverse(seqn)}")
