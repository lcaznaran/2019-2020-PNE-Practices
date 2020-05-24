from Client0 import Client
from Seq1 import Seq

IP = "127.0.0.1"
PORT = 8080

FOLDER = "../Session-04/"
EXT = ".txt"
GENE = "FRAT1"

c = Client(IP, PORT)

print(c)


s = Seq().read_fasta(FOLDER + GENE + EXT)
b = str(s)
print(f"Gene {GENE}: {b}")
length=10
c.debug_talk(f"Sending {GENE} Gene to the server..., in fragments of {length}")
for i in range(5):
    fragm = b[i*length: (i+1)*length]
    print(f"Fragment {i+10}: {fragm}")
    c.talk(f"Fragment {i+1}: {fragm}")
