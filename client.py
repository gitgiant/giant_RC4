from mysocket import *


class Client(object):

    def __init__(self):

        self.clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self, addr):

        self.clientSocket.connect(addr)

    def _sendFile(self, path):

        sendfile = open(path, 'rb')
        data = sendfile.read()

        self._con.sendall(len(data)) # Send the length as a fixed size message
        self._con.sendall(data)


        # Get Acknowledgement
        self._con.recv(1) # Just 1 byte
