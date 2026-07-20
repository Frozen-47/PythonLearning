import socket

client = socket.socket()
client.connect(('localhost', 1234))

client.send(b"Hello from Client")
print("Received from server:", client.recv(1024).decode())

client.close()
