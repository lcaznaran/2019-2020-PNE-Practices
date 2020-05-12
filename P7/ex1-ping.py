import http.server
import json

server = "rest.ensembl.org"
endpoint = "/info/ping"
params = "?content-type=application/json"
url = server + endpoint + params

print()
print(f"Server: {server}")
print(f"URL: {url}")

conn = http.client.HTTPConnection(server)
try:
    conn.request("GET", endpoint + params)
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()

r1 = conn.getresponse()
print(f"Response received!: {r1.status} {r1.reason}\n")
data1 = r1.read().decode()

resp = json.loads(data1)

ping = resp["ping"]
if ping ==1:
    print("Ping ok")
