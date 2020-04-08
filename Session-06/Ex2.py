class Seq:
    """A class for representing sequence objects"""
    def __init__(self, strbases):
        Ac = strbases.count("A")
        Tc = strbases.count("T")
        Gc = strbases.count("G")
        Cc = strbases.count("C")
        if (Ac + Tc + Gc + Cc) != len(strbases):
            print("ERROR")
            self.strbases = "Error"
        else:
            print("New sequence created!")
            self.strbases = strbases
    def __str__(self):
        return self.strbases
    def len(self):
       return len(self.strbases)

seq_list = [Seq("ACT"), Seq("GATA"), Seq("CAGATA")]

for seq in seq_list:
    print(f"Sequence {seq_list.index(seq)}:(Length:{seq.len()}){seq}")