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
    return seq.count(base)

def seq_count(seq):
    res = {'A': seq_count_base(seq, 'A'), 'T': seq_count_base(seq, 'T'),
           'C': seq_count_base(seq, 'C'), 'G': seq_count_base(seq, 'G')}
    return res

def seq_reverse(seq):
    return seq[::-1]

def seq_complement(seq):
    # -- Dictionary of complement bases
    basec = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    comp = ""
    for b in seq:
        comp += basec[b]
    return comp
