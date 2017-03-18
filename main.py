import random
import socket
import sys
from config import *
import client
import server
import threading

key = 'B4B545326FF13'
LOCALHOST = '127.0.0.1'
BUFFER_SIZE = 1024

def is_valid_ipv4_address(address):
    if address == "localhost":
        return True
    try:
        mysocket.inet_pton(mysocket.AF_INET, address)
    except AttributeError:
        try:
            mysocket.inet_aton(address)
        except mysocket.error:
            return False
        return address.count('.') == 3
    except mysocket.error:  # not a valid address
        return False

    return True

def is_valid_ipv6_address(address):
    try:
        mysocket.inet_pton(mysocket.AF_INET6, address)
    except mysocket.error:  # not a valid address
        return False
    return True

class ChatListener(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.port = None

    def run(self):
        listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        listen_socket.bind((LOCALHOST, self.port))
        listen_socket.listen(1)

        while True:
            connection, address = listen_socket.accept()
            print("listening")
            print("Established connection with: ", address)

            message = connection.recv(BUFFER_SIZE)
            print("Them: ", message)


class ChatSender(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.address = None
        self.port = None

    def run(self):
        send_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        send_socket.connect((self.address, self.port))

        while True:

            message = input("You: ")

            if message.lower() == "quit":
                break
            else:
                try:
                    send_socket.sendall(message)
                except:
                    print(str(Exception))

def main():
    print(header)
    #while True:
    print("Please select from the following options: ")
    print("[E]stablish a connnection")
    print("[L]isten for a connection")
    print("[Q]uit")

    choice = input().lower()
    if choice == 'e':
        # address = input("Please enter an address: ")
        # See if target address is valid
        address = 'localhost'
        if is_valid_ipv4_address(address):

            port = int(input("Please select port to use: "))
            if port > 65535 | port < 0:
                print("Error port outside range.")
            #port = 80
            #     break

        else:
            print("Address is not valid")
            #break
        # opens the file and reads contents as binary
        bin_data = open('send_message', 'rb').read()
        chat_sender = ChatSender()
        chat_sender.address = address
        chat_sender.port = port
        chat_sender.start()

    elif choice == 'l':
        port = int(input("Please select port to use: "))
        if port > 65535 | port < 0:
            print("Error port outside range.")
            #break
        chat_listener = ChatListener()
        chat_listener.port = port
        chat_listener.start()

    elif choice == 'q':
        print("Exiting")
        exit(1)

if __name__ == '__main__':
    main()