import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.bind(('127.0.0.1', 10000))
    sock.listen()
    print("Socket is ready address: ", sock.getsockname())
    conn, adress = sock.accept()
    while True:
        data = conn.recv(1024)
        if not data:
            break
        print(data.decode('utf-8'))
