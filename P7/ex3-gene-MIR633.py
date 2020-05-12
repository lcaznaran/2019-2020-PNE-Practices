import http.server
import json
import termcolor

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
namegene = "MIR633"
server = "rest.ensembl.org"
endpoint = "/sequence/id/"
params = "?content-type=application/json"
url = server + endpoint + genes[namegene] + params

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
termcolor.cprint("Bases: ","yellow",end="")
print(f"{gene['seq']}")



