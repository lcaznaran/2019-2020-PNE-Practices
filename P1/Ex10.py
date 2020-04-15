from Seq1 import Seq

BASES = ["A", "C", "T", "G"]
FOLDER = "../Session-04/"
GENES = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]
TXT = ".txt"
for gene in GENES:
    s = Seq()
    DNA_FILE = FOLDER + gene + TXT
    s1 = Seq(s.read_fasta(DNA_FILE)) #!!!!!!!
    d = s1.count()
    ld = list(d.values())
    m = max(ld)
    print(f"Gene {gene}: Most frequent base: {BASES[ld.index(m)]}")