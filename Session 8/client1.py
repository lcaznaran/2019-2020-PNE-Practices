import socket

IP = "212.128.253.128"
PORT = 8080

# --- Creamos el socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Establishing the connection with the server
s.connect((IP, PORT))

# -- Send data to the server
s.send(str.encode("hello"))

# -- Receive dara from the server
msg = s.recv(2000)

print("Message from the server", msg.decode("utf-8"))

# -- Closing the connection
s.close()