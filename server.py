# server.py

import socket                   # Import socket module

from Crypto.Cipher import AES

def decrypt(ciphertext):
    obj2 = AES.new('69ibgr2jn463ygvx', AES.MODE_CFB, '0njoc6838ncvosin')
    message = obj2.decrypt(ciphertext)
    print 'The message is: ', (message)
    #return message


port = input('Enter the port number to connect to: ')  # Reserve a port for your service.
s = socket.socket()             # Create a socket object
host = socket.gethostname()     # Get local machine name
s.bind((host, port))            # Bind to the port
s.listen(5)                     # Now wait for client connection.

print 'Waiting for Clients...'

while True:
    conn, addr = s.accept()     # Establish connection with client.
    print 'Got connection request from', addr
    data = conn.recv(1024)
    decrypt(data)
    #print('Server received', repr(data))
    print 'Connection Established'

    filename='mytext.txt'
    f = open(filename,'rb')
    l = f.read(1024)
    while (l):
       conn.send(l)
       #print('Sent ',repr(l))
       l = f.read(1024)
    f.close()

    print('File Sent')
    #conn.send('Thank you for connecting')
    conn.close()
