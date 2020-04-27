import socket
import termcolor

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

print("SEQ server configured!")

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
        # -- Print the received message
        print(f"Message received: ", end="")
        if msg == "PING":
            termcolor.cprint("PING command", 'green')
            response = "OK!\n"
            print(response)
            cs.send(response.encode())
            cs.close()