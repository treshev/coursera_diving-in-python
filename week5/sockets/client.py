import socket

with socket.create_connection(('127.0.0.1', 10000)) as sock:
    sock.sendall(b"ping from client")
