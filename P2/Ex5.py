from Client0 import Client
from Seq1 import Seq

PRACTICE = 2
EXERCISE = 5

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = "127.0.0.1"
PORT = 8080

FOLDER = "../Session-04/"
EXT = ".txt"
GENE = "U5"

c = Client(IP, PORT)

print(c)


s = Seq().read_fasta(FOLDER + GENE + EXT)

c.debug_talk(f"Sending {GENE} Gene to the server...")
c.debug_talk(str(s))