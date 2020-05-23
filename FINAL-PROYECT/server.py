import http.server
import socketserver
import termcolor
from pathlib import Path
import json
from socket import gethostbyname, gaierror
from Seq1 import Seq

PORT = 8080
#ensembl info
server = "rest.ensembl.org"
params = "?content-type=application/json"


socketserver.TCPServer.allow_reuse_address = True

class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        termcolor.cprint(self.requestline, 'green')
        req_line = self.requestline.split(" ")
        # Get the path. It always start with the / symbol
        path = req_line[1]
        arguments = path.split('?') #we can see "?" in the examples given
        verb = arguments[0]
        status = 404
        try:
            if verb == "/":
                contents = Path("index.html").read_text()
                status = 200
            elif verb == "/listSpecies":
                endpoint = "/info/species"  # specific endpoint for this function
                conn = http.client.HTTPConnection(server)
                pair = arguments[1]
                name,values = pair.split("=")
                limit = values
                if values == "":
                    contents = Path("Error.html").read_text()
                    contents += f"""<a href="/">Main page</a>
                                        </body>
                                        </html>"""
                    status = 404
                else:
                    limit = int(values)
                    try:
                        conn.request("GET", endpoint + params)
                    except (ConnectionRefusedError, gaierror):
                        print("ERROR! Cannot connect to the Server")
                        exit()
                    resp = conn.getresponse()
                    data = resp.read().decode()
                    data = json.loads(data)
                    info = data['species']
                    lim_list = []
                    contents = f"""<!DOCTYPE html>
                    <html lang="en">
                    <head>
                        <meta charset="UTF-8">
                        <title>LIST OF SPECIES</title>
                        <p>The total number of species is:{len(info)}</p>
                    </head>
                    <body style="background-color: rgb(64,224,208);">"""
                    if values == "":
                        for i in info:
                            contents += f"""
                            <ol>
                            <li>-{i["common_name"]}</li>
                            </ol>"""
                        contents += """<a href="/">Main page</a>
                                </body>
                                </html>"""
                        status = 200
                    else:
                        if len(info) >= (limit):
                            contents += f"""<p>The limit that you have selected is: {limit}</p>
                                            <p>The species are:</p>
                                               </body>
                                               </html>"""
                            for i in info:
                                lim_list.append(i["common_name"])
                                if limit == len(lim_list):
                                    for e in lim_list:
                                        contents += f"""<il>
                                        <ol>-{e}</ol>
                                        </il>"""
                            contents += """<a href="/">Main page</a>
                                        </body>
                                        </html>"""
                            status = 200
            elif verb == "/karyotype":
                contents = f"""
                <!DOCTYPE html>
                <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <title>KARYOTYPE OF A SPECIE</title>
                    <p>The names of the chromosomes are:</p>
                </head>
                <body style="background-color: rgb(64,224,208);">"""
                pair = arguments[1]
                division = pair.split("?")
                n, namespecie = division[0].split("=")
                if namespecie != "":
                    endpoint = "info/assembly/"  # specific endpoint for this function
                    conn = http.client.HTTPConnection(server)
                    try:
                        conn.request("GET", endpoint + str(namespecie) + params) #to check if the input is in ensembl
                    except ConnectionRefusedError:
                        print("ERROR! Cannot connect to the Server")
                        exit()
                    resp = conn.getresponse()
                    data = resp.read().decode("utf-8")
                    data = json.loads(data)
                    info = data['karyotype']
                    for i in info:
                        contents += f"""<il>
                                        <ol>-{i}</ol>
                                        </il>"""
                    contents += f"""<a href="/">Main page</a>
                                        </body>
                                        </html>"""
                    status =200
                else:
                    contents = Path("Error.html").read_text()
                    contents += f"""<a href="/">Main page</a>
                                                            </body>
                                                            </html>"""
            elif verb == "/chromosomeLength":
                pair = arguments[1]
                division = pair.split("&")
                n_specie, specie = division[0].split("=")
                n_chr, chromosome = division[1].split("=")
                if specie == "":
                    contents = Path("Error.html").read_text()
                    contents += f"""<a href="/">Main page</a>
                    </body>
                    </html>"""
                    status = 404
                elif chromosome == "":
                    contents = Path("Error.html").read_text()
                    contents += f"""<a href="/">Main page</a>
                    </body>
                    </html>"""
                    status = 404
                else:
                    endpoint = "/info/assembly/"
                    conn = http.client.HTTPConnection(server)
                    try:
                        conn.request("GET", endpoint +specie + params) #to check if the input is in ensembl
                    except ConnectionRefusedError:
                        print("ERROR! Cannot connect to the Server")
                        exit()
                    resp = conn.getresponse()
                    data = resp.read().decode("utf-8")
                    data = json.loads(data)
                    chr_length = "" #this is just a value, so no []
                    for i in data["top_level_region"]:
                        if i["name"] == chromosome:
                            chr_length = i["length"]
                            if int(chr_length) == 0:
                                contents = f"""
                            <!DOCTYPE html>
                            <html lang="en">
                            <head>
                                <meta charset="UTF-8">
                                <title>ERROR</title>
                                <p> Invalid input, check it again </p>
                            </head>
                            <body style="background-color: red;">"""
                            else:
                                contents = f"""
                                <!DOCTYPE html>
                                <html lang="en">
                                <head>
                                    <meta charset="UTF-8">
                                    <title>LENGTH OF THE SELECTED CHROMOSOME</title>
                                </head>
                                <body style="background-color: rgb(64,224,208);">"""
                                contents += f"""<p>The length of the chromosome {chromosome} of the {specie} is: {chr_length}</p>"""
                            contents += f"""<a href="/">Main page</a>
                                                    </body>
                                                    </html>"""
                    status = 200

                contents = Path("Error.html").read_text()
                contents += f"""<a href="/">Main page</a>
                                    </body>
                                    </html>"""
                status = 404
            elif verb == "/geneSeq":
                try:
                    contents = f"""
                    <!DOCTYPE html>
                    <html lang="en">
                    <head>
                        <meta charset="UTF-8">
                        <title>GENE LIST</title>
                    </head>
                    <body style="background-color: rgb(64,224,208);">"""
                    pair = arguments[1]
                    division = pair.split("=")
                    specie_n = division[1]
                    values = ""
                    endpoint = f"/xrefs/symbol/homo_sapiens/{specie_n}" #id gene human
                    conn = http.client.HTTPConnection(server)
                    try:
                        conn.request("GET", endpoint + params)
                    except ConnectionRefusedError:
                        print("ERROR! Cannot connect to the Server")
                        exit()
                    resp = conn.getresponse()
                    data = resp.read().decode("utf-8")
                    data = json.loads(data)
                    ID = data[0]
                    gene = ID["id"] #obtain gene in ensembl: we can find this data on wikipedia
                    #we need another endpoint, we have the id to use sequence/id/---
                    endpoint1 = f"sequence/id/{gene}"
                    conn1 = http.client.HTTPConnection(server)
                    try:
                        conn1.request("GET", endpoint1 + params)
                    except ConnectionRefusedError:
                        print("ERROR! Cannot connect to the Server")
                        exit()
                    resp1 = conn1.getresponse()
                    data1 = resp1.read().decode("utf-8")
                    data1 = json.loads(data1)
                    sequence = data1["seq"]
                    contents += f"""<p> The sequence of this human  gene ({gene}) is: {sequence}</p>"""
                    status = 200
                except:
                    contents = Path("Error.html").read_text()
                    contents += f"""<a href="/">Main page</a>
                                        </body>
                                        </html>"""
                    status = 404


            self.send_response(status)
            self.send_header('Content-Type', 'text/html')
            self.send_header('Content-Length', len(str.encode(contents)))
            self.end_headers()
            self.wfile.write(str.encode(contents))
            return
        except (ValueError,KeyError,IndexError,TypeError,UnboundLocalError):
            contents = Path("Error.html").read_text()
            status = 404

Handler = TestHandler

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at PORT", PORT)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stopped by the user")
        httpd.server_close()




