from Client0 import Client

# -- Parameters of the server to talk to
PORT = 8080
IP = "127.0.0.1"

for i in range(1):

    # -- Create a client object
    c = Client(IP, PORT)

    # -- Send a message to the server
    c.debug_talk(f"Message {i}")