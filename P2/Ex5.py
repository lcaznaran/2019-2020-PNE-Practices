from Client0 import Client
from Seq1 import Seq



IP = "127.0.0.1"
PORT = 8080

FOLDER = "../Session-04/"
txt = ".txt"
GENE = "U5"

c = Client(IP, PORT)

print(c)


s = Seq().read_fasta(FOLDER + GENE + txt)

c.debug_talk(f"Sending {GENE} Gene to the server...")
c.debug_talk(str(s))
