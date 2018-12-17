import socket
import time


class ClientError(Exception):
    pass


class Client:
    def __init__(self, ip, port, timeout=None):
        self.ip = ip
        self.port = port
        self.timeout = timeout

    @staticmethod
    def parse(data):
        key, value, timestamp = 0, 1, 2
        result = {}
        for par in data.split('\n'):
            if 'ok' not in par and len(par.strip()) > 0:
                params = par.split(" ")
                if params[key] in result.keys():
                    result[params[key]].append((int(params[timestamp]), float(params[value])))
                    result[params[key]].sort(key=lambda tup: tup[0])
                else:
                    result[params[key]] = [(int(params[timestamp]), float(params[value]))]
        return result

    def put(self, key, value, timestamp=None):
        timestamp = timestamp or str(int(time.time()))
        req_string = "put {key} {value} {timestamp}\n".format(key=key, value=value, timestamp=timestamp)
        with socket.create_connection((self.ip, self.port)) as sock:
            sock.sendall(req_string.encode(encoding="utf-8"))
            while True:
                data = sock.recv(1024)
                if b"ok" in data:
                    return None
                elif b"error" in data:
                    raise ClientError

    def get(self, key):
        req_string = "get {}\n".format(key)
        with socket.create_connection((self.ip, self.port), self.timeout) as sock:
            sock.sendall(req_string.encode(encoding="utf-8"))
            while True:
                data = sock.recv(1024)
                if b"ok" in data:
                    return Client.parse(data.decode())
                elif b"error" in data:
                    raise ClientError


if __name__ == "__main__":
    client = Client("127.0.0.1", 8888, timeout=15)

    client.put("palm.cpu", 0.5, timestamp=1150864247)
    client.put("palm.cpu", 2.0, timestamp=1150864248)
    client.put("palm.cpu", 0.5, timestamp=1150864248)

    client.put("eardrum.cpu", 3, timestamp=1150864250)
    client.put("eardrum.cpu", 4, timestamp=1150864251)
    client.put("eardrum.memory", 4200000)

    print(client.get("*"))
