import socket

# SERVER IP, PORT
PORT = 8080
IP = "212.128.253.150"

while True:
  # -- Ask the user for the message
  m = input("Message to send: ")
  # -- Create the socket
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  # -- Establish the connection to the Server
  s.connect((IP, PORT))
  # -- Send the user message
  s.send(str.encode(m))
  # -- Close the socket
  s.close()
