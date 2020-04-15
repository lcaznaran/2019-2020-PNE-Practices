from Seq1 import Seq
BASES = ["A", "C", "T", "G"]
seq = Seq("ACTGA")
seq1 = Seq()
seq2 = Seq("ATCGHY")
seqlist = [seq, seq1, seq2]
for s in seqlist:
    print(f"Sequence {seqlist.index(s)}: (Length {s.length()}){s}")
    for b in BASES:
        print(f"{b}: {s.count_base(b)}", end=", ")
    print("")


