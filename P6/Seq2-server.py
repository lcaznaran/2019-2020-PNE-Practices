import http.server
import socketserver
import termcolor
from pathlib import Path
from Seq1 import Seq

# Define the Server's port
PORT = 8080


# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True
sequences = ["ATCGTAGTTCTGCAACAT", "TTGGACTGACTGCAAGTT","CTACGATGCTAATGTAAA","ACATGCTGATGCCTTAAT","CTGTCAAACTGGAACTGG"]
folder = "../Session-04/"
txt = ".txt"

# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inheritates all his methods and properties
class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        # Print the request line
        termcolor.cprint(self.requestline, 'green')

        # Analize the request line
        req_line = self.requestline.split(' ')

        # Get the path. It always start with the / symbol
        path = req_line[1]

        # Read the arguments
        arguments = path.split('?')

        # Get the verb. It is the first argument
        verb = arguments[0]

        # -- Content type header
        # -- Both, the error and the main page are in HTML
        contents = Path('Error.html').read_text()
        error_code = 404

        if verb == "/":
            # Open the form1.html file
            # Read the index from the file
            contents = Path('form-4.html').read_text()
            error_code = 200
        elif verb == "/ping":
            contents ="""
            <!DOCTYPE html>
            <html lang="en">
            <head>
            <meta charset="utf-8">
                <title>PING</title>
            </head>
            <body style="background-color: lightblue;">
            <h1> PING OK! </h1>
            <p> The SEQ 2 server is running </p>
            <hr>
            <a href="/">MAIN PAGE</a>
            </body>
            </html>
            """
            error_code = 200
        elif verb == "/get":
            # -- Get the argument to the right of the ? symbol
            pair = arguments[1]
            # -- Get all the pairs name = value
            pairs = pair.split('&')
            # -- Get the two elements: name and value
            name, value = pairs[0].split("=")
            n_v = int(value)
            seq = sequences[n_v]
            # -- Generate the html code
            contents = f"""
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="utf-8">
                <title>GET</title>
            </head>
            <body style="background-color: lightyellow;">
            <h2>Sequence number {n_v}</h2>
            <p> {seq} </p>
            <a href="/">Main page</a>
            </body>
            </html>
            """
            error_code = 200
        elif verb == "/gene":
            # -- Get the argument to the right of the ? symbol
            pair = arguments[1]
            # -- Get all the pairs name = value
            pairs = pair.split('&')
            # -- Get the two elements: name and value
            name, gene = pairs[0].split("=")
            s = Seq()
            s1 = Seq(s.read_fasta(folder + gene + txt))
            gene_info = str(s1)
            # -- Generate the html code
            contents = f"""
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="utf-8">
                <title>GENE</title>
            </head>
            <body style="background-color: magenta;">
            <h2>Gene: {gene}</h2>
            <textarea readdonly rows = "20" cols = "60"> {gene_info}</textarea>
            <br>
            <a href="/">Main page</a>
            </body>
            </html>
            """
            error_code = 200
        elif verb == "/operate":
            # -- Get the argument to the right of the ? symbol
            pair = arguments[1]
            # -- Get all the pairs name = value
            pairs = pair.split('&')
            # -- Get the two elements: name and value
            name, sequence = pairs[0].split("=")
            name, operation = pairs[1].split("=")
            s = Seq(sequence)
            if operation == "info":
                l = s.length()
                ac = s.count_base("A")
                tc = s.count_base("T")
                cc = s.count_base("C")
                gc = s.count_base("G")
                resp = f"""
                    <p>Total length: {l}</p>
                    <p>A: {ac} ({round((ac / l) * 100)})%</p>  
                    <p>C: {cc} ({round((cc / l) * 100)})%</p>    
                    <p>T: {tc} ({round((tc / l) * 100)})%</p>     
                    <p>G: {gc} ({round((gc / l) * 100)})%</p>"""
            elif operation == "rev":
                resp = s.seq_reverse()
            else:
                resp = s.seq_complement()
            contents = f"""
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="utf-8">
                <title>OPERATION</title>
            </head>
            <body style="background-color: lightgreen;">
            <h2>Sequence:</h2>
            <p> {sequence} </p>
            <h2> Operation: </h2>
            <p> {operation}</p>
            <h2> Result: </h2>
            <p> {resp} </p>
            <br>
            <a href="/">Main page</a>
            </body>
            </html>
            """
            error_code = 200

        # Generating the response message
        self.send_response(error_code)  # -- Status line: OK!

        # Define the content-type header:
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(contents)))

        # The header is finished
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

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stopped by the user")
        httpd.server_close()