import socket

server = socket.socket()
server.bind(('localhost', 1234))
server.listen(1)

print("Server waiting for connection...")
conn, addr = server.accept()

msg = conn.recv(1024).decode()
print("Received from client:", msg)

conn.send(b"Acknowledgement from server")
conn.close()
