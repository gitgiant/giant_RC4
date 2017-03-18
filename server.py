from mysocket import *


class Server(object):

    def __init__(self):

        self.serverSocket = socket(AF_INET, SOCK_STREAM)

    def connect(self, addr):

        self.serverSocket.connect(addr)

    def _sendFile(self, path):

        sendfile = open(path, 'rb')
        data = sendfile.read()

        self._con.sendall(len(data)) # Send the length as a fixed size message
        self._con.sendall(data)


        # Get Acknowledgement
        self._con.recv(1) # Just 1 byte