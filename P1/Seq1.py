from pathlib import Path

class Seq:
    """A class for representing sequence objects"""
    NULL = "NULL"
    ERROR = "ERROR"
    def __init__(self, strbases=NULL):
        if strbases == self.NULL:
            self.strbases = self.NULL #this is to define the strbases
            print("NULL Seq created")
        else:
            Ac = strbases.count("A")
            Tc = strbases.count("T")
            Gc = strbases.count("G")
            Cc = strbases.count("C")
            if (Ac + Tc + Gc + Cc) != len(strbases):
                print("INVALID Seq!")
                self.strbases = self.ERROR #also to define the Error strbases
            else:
                print("New sequence created!")
                self.strbases = strbases
    def __str__(self):
        return self.strbases
    def length(self):
        if self.strbases in [self.ERROR, self.NULL]:
            return 0
        else:
            return len(self.strbases)

    def count_base(self, base):
        return self.strbases.count(base)

    def count(self):
        dict = {"A": self.count_base("A"), "C": self.count_base("C"), "T": self.count_base("T"), "G": self.count_base("G")}
        return dict

    def seq_reverse(self):
        if self.strbases in self.NULL:
            return "NULL"
        elif self.strbases in self.ERROR:
            return "ERROR"
        else:
            return self.strbases[::-1]

    def seq_complement(self):
        if self.strbases in self.NULL:
            return "NULL"
        elif self.strbases in self.ERROR:
            return "ERROR"
        else:
            basec = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
            comp = ""
            for b in self.strbases:
                comp += basec[b] #b is the key
            return comp

    def read_fasta(self, f):
        file_contents = Path(f).read_text()
        lines = file_contents.split("\n")[1:]
        body = "".join(lines)
        return body
