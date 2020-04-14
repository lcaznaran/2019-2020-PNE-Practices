from pathlib import Path
class Seq:
    """A class for representing sequence objects"""
    NULL = "NULL"
    def __init__(self, strbases=NULL):
        if strbases == self.NULL:
            self.strbases = self.NULL
            print("NULL Seq created")
        else:
            Ac = strbases.count("A")
            Tc = strbases.count("T")
            Gc = strbases.count("G")
            Cc = strbases.count("C")
            if (Ac + Tc + Gc + Cc) != len(strbases):
                print("INVALID Seq!")
                self.strbases = "ERROR"
            else:
                print("New sequence created!")
                self.strbases = strbases
    def __str__(self):
        return self.strbases
    def length(self):
       return len(self.strbases)

