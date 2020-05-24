from Client0 import Client

IP= "127.0.0.1"
PORT = 8080

c = Client(IP, PORT)

print(c)

print("· Testing PING...")
print(c.talk("PING")) #THIS IS THE COMMAND ORDERED BY THE CLIENT

print("· Testing GET...")
for i in range(5):
    cmd = f"GET {i}"
    print(f"GET {i}: {c.talk(cmd)}", end="") #not \n

print("· Testing INFO...")
s = c.talk("GET 0")
cmd = f"INFO {s}"
print(c.talk(cmd))

print("* Testing COMP...")
cmd = f"COMP {s}"
print(c.talk(cmd))

print("* Testing REV...")
cmd = f"REV {s}"
print(c.talk(cmd))

print("* Testing GENE...")
listgene = ["U5","ADA","FRAT1","FXN","RNU6_269P"]
for i in listgene:
    cmd = f"GENE {i}"
    print(f"GENE {i}")
    print(c.talk(cmd))