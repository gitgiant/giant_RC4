class mysocket:
    '''demonstration class only
      - coded for clarity, not efficiency
    '''

    def __init__(self, sock=None):
        if sock is None:
            self.sock = socket.socket(
                socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sock = sock

    def connect(self, host, port):
        self.sock.connect((host, port))

    def mysend(self, msg):
        totalsent = 0
        while totalsent < len(msg):
            sent = self.sock.send(msg[totalsent:])
            if sent == 0:
                raise RuntimeError("socket connection broken")
            totalsent = totalsent + sent

    # def myreceive(self):
    #     chunks = []
    #     bytes_recd = 0
    #     while bytes_recd < MSGLEN:
    #         chunk = self.sock.recv(min(MSGLEN - bytes_recd, 2048))
    #         if chunk == '':
    #             raise RuntimeError("socket connection broken")
    #         chunks.append(chunk)
    #         bytes_recd = bytes_recd + len(chunk)
    #     return ''.join(chunks)

    # s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # print(socket.gethostname())
    # s.bind((socket.gethostname(), 80))
    # # listen to up to 5 connections
    # s.listen(5)

    # while 1:
    #     # accept connections from outside
    #     (clientsocket, address) = s.accept()
    #     # now do something with the clientsocket
    #     # in this case, we'll pretend this is a threaded server
    #     # ct = client_thread(clientsocket)
    #     # ct.run()