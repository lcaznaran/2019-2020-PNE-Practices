import sys

import termcolor
from termcolor import colored, cprint
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
    def length(self):
        return len(self.strbases)

def print_seqs(seqs):
    if seqs == seq_list1:
      for seq in seqs:
        termcolor.cprint(f"Sequence{seqs.index(seq)}: (Length: {seq.length()}) {seq}", "blue")
    elif seqs == seq_list2:
      for seq in seqs:
        termcolor.cprint(f"Sequence{seqs.index(seq)}: (Length: {seq.length()}) {seq}", "green")
    #this is because for each generate_Seqs, you will  obtain a list of sequences, each one has its own info
def generate_seqs(patter, number):
    i = 1
    seqlist = [] #because you have to do a list of sequences
    while i <= (number):
        seqlist.append(Seq(patter * i)) #x times the pattern
        i += 1
        if i > (number):
            break
    return seqlist

seq_list1 = generate_seqs("A", 3)
seq_list2 = generate_seqs("AC", 5)

termcolor.cprint("List 1:", "blue")
print_seqs(seq_list1)

print()
termcolor.cprint("List 2:", "green")
print_seqs(seq_list2)

