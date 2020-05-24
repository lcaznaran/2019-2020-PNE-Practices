from Client0 import Client
from Seq1 import Seq


IP = "127.0.0.1"
PORT = 8080
PORT2= 8081
FOLDER = "../Session-04/"
EXT = ".txt"
GENE = "FRAT1"

c = Client(IP, PORT)
c1= Client(IP, PORT2)

print(c)


s = Seq().read_fasta(FOLDER + GENE + EXT)
b = str(s)
print(f"Gene {GENE}: {b}")
length=10

c.talk(f"Sending {GENE} Gene to the server..., in fragments of {length}")
c1.talk(f"Sending {GENE} Gene to the server..., in fragments of {length}")

for i in range(10):
    fragm = b[i*length: (i+1)*length]
    print(f"Fragment {i+1}: {fragm}")
    message= (f"Fragment {i+1}: {fragm}")
    if i % 2:
        c1.talk(message)
    else:
        c.talk(message)