import http.server
import socketserver
import termcolor
from pathlib import Path
import json

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
        if verb == "/":
            contents = Path("index.html").read_text()
            status = 200
        elif verb == "/listSpecies":
            endpoint = "/info/species"  # specific endpoint for this function
            conn = http.client.HTTPConnection(server)
            pair = arguments[1]
            name,value = pair.split("=")
            limit = int(value)
            try:
                conn.request("GET", endpoint + params)
            except ConnectionRefusedError:
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
            <body style="background-color: lightblue;">"""
            if value == "":
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
                if len(info) >= limit:
                    contents += f"""<p>The limit that you have selected is: {limit}</p>
                                    <p>The species are:</p>
                                       </body>
                                       </html>"""
                    for i in info:
                        lim_list.append(i["display_name"])
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
            endpoint = "/info/species"  # specific endpoint for this function
            conn = http.client.HTTPConnection(server)
            pair = arguments[1]
            name,value = pair.split("=")
            limit = int(value)
            try:
                conn.request("GET", endpoint + params)
            except ConnectionRefusedError:
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
            <body style="background-color: lightblue;">"""
            if value == "":
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
                if len(info) >= limit:
                    contents += f"""<p>The limit that you have selected is: {limit}</p>
                                    <p>The species are:</p>
                                       </body>
                                       </html>"""
                    for i in info:
                        lim_list.append(i["display_name"])
                        if limit == len(lim_list):
                            for e in lim_list:
                                contents += f"""<il>
                                <ol>-{e}</ol>
                                </il>"""
                    contents += """<a href="/">Main page</a>
                                </body>
                                </html>"""
                    status = 200
        self.send_response(status)
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(contents)))

        self.end_headers()

        # Send the response message
        self.wfile.write(str.encode(contents))
        return

# ------------------------
# - Server MAIN program
# ------------------------
# -- Set the new handler
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




