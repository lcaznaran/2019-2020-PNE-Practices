from pathlib import Path

def seq_ping():
    print("OK")

def seq_read_fasta(f):
    file_contents = Path(f).read_text()
    lines = file_contents.split("\n")
    body = "\n".join(lines[1:])
    return body

def seq_len(FILENAME):
    contents = Path(FILENAME).read_text()
    lines = contents.split("\n")
    body = "".join(lines[1:])
    return len(body)

def seq_count_base(seq,base):
    a = 0
    t = 0
    c = 0
    g = 0
    base = [a, t, c, g]
    for b in seq:
        if b == "A":
            a += 1
        if b == "C":
            c += 1
        if b == "G":
            g += 1
        if b == "T":
            t += 1

    return base