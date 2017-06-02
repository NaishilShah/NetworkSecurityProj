# client.py

import socket                   # Import socket module
from Crypto.Cipher import AES

def encrypt(message):
    obj = AES.new('69ibgr2jn463ygvx', AES.MODE_CFB, '0njoc6838ncvosin') #first is the key and then is the IV used
    ciphertext = obj.encrypt(message)
    #print 'Encrypted Text is ' + (ciphertext)
    s.send(ciphertext)


s = socket.socket()             # Create a socket object
host = socket.gethostname()     # Get local machine name
port = input('Enter the port number to connect to: ')  # Reserve a port for your service.

s.connect((host, port))
encrypt('Connection Request')
print 'Connection Established'

with open('received_file', 'wb') as f:
    print 'file opened'
    while True:
        #print('receiving data...')
        data = s.recv(1024)
        #print 'data=',(data)
        if not data:
            break
        # write data to a file
        f.write(data)

f.close()
print('Received the file')
s.close()
print('Connection Closed')
