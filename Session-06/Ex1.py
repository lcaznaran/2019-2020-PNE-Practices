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


s1 = Seq("ACCTGC")
s2 = Seq("Hello? Am I a valid sequence?")

print(f"Sequence 1 : {s1}")
print(f"Sequence 2: {s2}")