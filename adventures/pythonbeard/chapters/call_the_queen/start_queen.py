import socket

from definitions import IP, PORT    

class QueenHub(object):
    def __init__(self, ip, port, message_callback):
        self.ip = ip
        self.port = port
        self.socket = socket.socket()
        self.message_callback = message_callback
    
    def start(self):
        # Connect to the port
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind((self.ip, self.port))
        self.socket.listen(5)

        # Except one message and shutdown
        clientsocket, _ = self.socket.accept()
        with clientsocket:
            data = clientsocket.recv(1024)
            self.message_callback(data)
        self.socket.close()


if __name__ == "__main__":
    queen_hub = QueenHub(IP, PORT, lambda message: print("result : {} {}".format(message.hex()[:10], message)))
    
    queen_hub.start()