from Seq1 import Seq

BASES = ["A", "C", "T", "G"]
FOLDER = "../Session-04/"
FILENAME = "U5.txt"

s = Seq()

DNA_FILE = FOLDER + FILENAME

s1= Seq(s.read_fasta(DNA_FILE)) #!!!!!!!

print(f"Sequence: (Length {s1.length()}){s1}")
print(s1.count())
print(f"Reversed: {s1.seq_reverse()}")
print(f"Complement: {s1.seq_complement()}")

