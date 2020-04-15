from Seq1 import Seq
from Seq1 import Seq
BASES = ["A", "C", "T", "G"]
seq = Seq("ACTGA")
seq1 = Seq()
seq2 = Seq("ATCGHY")
seqlist = [seq, seq1, seq2]
for s in seqlist:
    print(f"Sequence {seqlist.index(s)}: (Length {s.length()}){s}")
    print(s.count())
    print(f"Reversed: {s.seq_reverse()}")


