import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", 1234))

server.listen(5)

print("Server waiting...")

client_socket, addr = server.accept()
print("Connected from:", addr)

client_socket.send("Hello from server".encode())
client_socket.close()
