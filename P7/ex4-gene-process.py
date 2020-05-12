import http.server
import json
import termcolor
from Seq1 import Seq

BASES = ["A","C","T","G"]
genes = {
    'FRAT1': 'ENSG00000165879',
    'ADA': 'ENSG00000196839',
    'FXN': 'ENSG00000165060',
    'RNU6_269P': 'ENSG00000212379',
    'MIR633': 'ENSG00000207552',
    'TTTY4C': 'ENSG00000228296',
    'RBMY2YP': 'ENSG00000227633',
    'FGFR3': 'ENSG00000068078',
    'KDR': 'ENSG00000128052',
    'ANK2': 'ENSG00000145362',
}
namegene = input("Write the gene name:")
server = "rest.ensembl.org"
endpoint = "/sequence/id/"
params = "?content-type=application/json"
url = server + endpoint + genes[namegene] + params
if namegene in genes:
    print()
    print(f"Server: {server}")
    print(f"URL: {url}")

    conn = http.client.HTTPConnection(server)
    try:
        conn.request("GET", endpoint+ genes[namegene] + params)
    except ConnectionRefusedError:
        print("ERROR! Cannot connect to the Server")
        exit()

    r1 = conn.getresponse()
    print(f"Response received!: {r1.status} {r1.reason}\n")
    data1 = r1.read().decode()

    gene = json.loads(data1)

    termcolor.cprint(f"Gene: ","yellow",end="")
    print(f"{namegene}")
    termcolor.cprint("Description: ","yellow",end="")
    print(f"{gene['desc']}") #see esembl page for desc and seq (especial functions)

    sequence = gene['seq']
    s = Seq(sequence)
    l = s.length()
    ac = s.count_base("A")
    tc = s.count_base("T")
    cc = s.count_base("C")
    gc = s.count_base("G")
    termcolor.cprint("Total length: ","yellow",end="")
    print(l)
    resp=f"""
    A: {ac} ({round((ac / l) * 100)})%
    C: {cc} ({round((cc / l) * 100)})%
    T: {tc} ({round((tc / l) * 100)})% 
    G: {gc} ({round((gc / l) * 100)})%"""
    print(resp)

    dictionary = s.count()
    listvalues = list(dictionary.values())
    maxvalue = max(listvalues)
    termcolor.cprint("The most frequent base is: ","yellow",end="")
    print(f"{BASES[listvalues.index(maxvalue)]}") #look for the max base