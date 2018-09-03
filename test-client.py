#!/usr/bin/env python2

import socket

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect(('localhost', 12345))
clientsocket.sendall(
    '0123456789\n'
    '0123456789\n'
    '0123456789\n'
    '0123456789\n'
    '0123456789\n'
    '0123456789\n'
    '0123456789\n'
    '0123456789\n'
    '0123456789\n'
    '0123456789\n'
    '0123456789\n'
    '0123456789\n'
    '0123456789\n'
    '0123456789\n'
    '01234589\n'
   )

result = clientsocket.recv(1024)
print result
clientsocket.close()