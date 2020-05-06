import socket
import termcolor
from Seq1 import Seq

seq = ["ACTGAACTTGACCTACGGTCA","TTCGACCGGAAGTCCAATTTG","CCTAGGAACTTTGACGTAACT","ACGTCAGCTAGTGCTAACGTA","ATTGCTAAGGTTCTGAGTACT"]
# -- Step 1: create the socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# -- Optional: This is for avoiding the problem of Port already in use
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Configure the Server's IP and PORT
PORT = 8080
IP = "127.0.0.1"

# -- Step 1: create the socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Optional: This is for avoiding the problem of Port already in use
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# -- Step 2: Bind the socket to server's IP and PORT
ls.bind((IP, PORT))

# -- Step 3: Configure the socket for listening
ls.listen()

def get_func(n):
    return seq[n]
def info_func(s):
    s=Seq(s)
    l = s.length()
    ac = s.count_base("A")
    tc = s.count_base("T")
    cc = s.count_base("C")
    gc = s.count_base("G")
    resp = f"""Sequence: {s}
    Total length: {l}
    A: {ac} ({round((ac/l)*100)})%  
    C: {cc} ({round((cc/l)*100)})%     
    T: {tc} ({round((tc/l)*100)})%     
    G: {gc} ({round((gc/l)*100)})%"""
    return resp

def comp_func(s):
    s = Seq(s)
    compl = s.seq_complement()
    return compl

def rev_func(s):
    s = Seq(s)
    rev = s.seq_reverse()
    return rev

def gene_func(GENE):
    FOLDER = "../Session-04/"
    txt = ".txt"
    s = Seq().read_fasta(FOLDER + GENE + txt)
    return s

print("SEQ server configured!")

listn=["1","2","3","4"]
while True:
    # -- Waits for a client to connect
    print("Waiting for clients to connect")
    try:
        (cs, client_ip_port) = ls.accept()

    # -- Server stopped manually
    except KeyboardInterrupt:
        print("Server stopped by the user")

        # -- Close the listenning socket
        ls.close()

        # -- Exit!
        exit()

    # -- Execute this part if there are no errors
    else:
        msg_raw = cs.recv(2048)
        # -- We decode it for converting it
        # -- into a human-redeable string
        msg = msg_raw.decode()
        lines = msg.split("\n")
        line0 = lines[0].strip()
        lcmds = line0.split(' ')
        comm = lcmds[0]
        try:
            arg = lcmds[1]
        except IndexError:
            # -- No arguments
            arg = ""
        # -- Print the received message
        print(f"Message received: ", end="")
        response=""
        if comm == "PING":
            termcolor.cprint("PING command", 'green')
            response = "OK!\n"

        elif comm == "GET":
            termcolor.cprint("GET command", 'green')
            response = get_func(int(arg))+"\n"
        elif comm == "INFO":
            termcolor.cprint("INFO command", 'green')
            response = info_func(arg) + "\n"
        elif comm == "COMP":
            termcolor.cprint("COMP command", 'green')
            response = comp_func(arg) + "\n"
        elif comm == "REV":
            termcolor.cprint("REV command", 'green')
            response = rev_func(arg) + "\n"
        elif comm == "GENE":
            termcolor.cprint("GENE command", 'green')
            response = gene_func(arg) + "\n"

        print(response)
        cs.send(response.encode())
        cs.close()