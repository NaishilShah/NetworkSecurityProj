import random


def key_gener( noise, mod=2 ):
    key = random.getrandbits( ( noise ** 2 ) )
    "Changing the power here will cause the key size to change"

    while ( (key % 2) != 1):
        key = key + 1

    return key


def encryption( noise, key, a_bit, mod=2 ):
    mask          = random.getrandbits( noise )
    a_bit_parity = a_bit % mod

    while ( ( mask % mod ) != a_bit_parity ):
        mask = random.getrandbits( noise )

    return mask + (key * random.getrandbits(noise ** 2))
    "Changing the power to say 5, will increase the key and cipher size"


def decryption( key, a_bit, mod=2 ):
    return ( a_bit % key ) % mod



def add():
    mod = 100
    noise   = random.getrandbits(3)
    key   = key_gener( noise, mod=mod )
    print( " Addition Operation:___________________________________________________\n" )

    a_plain= input( "Enter First Integer: " )
    if a_plain is 0:
        a_plain = input( "Enter non zero integer:")
    b_plain= input( "Enter Second Integer: " )
    if b_plain is 0:
        b_plain = input( "Enter non zero integer:")
    a_cipher     = encryption( noise, key, a_plain, mod=mod )
    b_cipher     = encryption( noise, key, b_plain, mod=mod )
    c       = a_cipher + b_cipher
    d       = decryption( key, c, mod=mod )
    print( "Result\n________________________________________________")
    print( "First Integer: %d \nSecond Integer: %d \n" % ( a_plain, b_plain ) )
    print( "Encrypted First Integer: %d \nEncrypted Second Integer: %d \n" % ( a_cipher, b_cipher ) )
    print( "Encrypted Result of Addition:------- %d \nDecrpyted Result of Addition:-------- %d \n \n" % ( c, d ) )

def subtract():
    mod = 100
    noise   = random.getrandbits(3)
    key   = key_gener( noise, mod=mod )
    print( " Subtraction Operation:___________________________________________________\n" )

    a_plain= input( "Enter First Integer: " )
    if a_plain is 0:
        a_plain = input( "Enter non zero integer:")
    b_plain= input( "Enter Second Integer: " )
    if b_plain > a_plain:
        b_plain = input( "Enter non zero integer lower than first:" )
    a_cipher     = encryption( noise, key, a_plain, mod=mod )
    b_cipher     = encryption( noise, key, b_plain, mod=mod )
    c       = a_cipher - b_cipher
    d       = decryption( key, c, mod=mod )
    print( "Result\n________________________________________________")
    print( "First Integer: %d \nSecond Integer: %d \n" % ( a_plain, b_plain ) )
    print( "Encrypted First Integer: %d \nEncrypted Second Integer: %d \n" % ( a_cipher, b_cipher ) )
    print( "Encrypted Result of Subtraction:------- %d \nDecrpyted Result of Subtraction:-------- %d \n \n" % ( c, d ) )


def mult():
    mod = 100
    noise   = random.getrandbits(3)
    key   = key_gener( noise, mod=mod )
    print( " Multiplication Operation:___________________________________________________\n" )

    a_plain= input( "Enter First Integer: " )
    if a_plain is 0:
        a_plain = input( "Enter non zero integer:")
    b_plain= input( "Enter Second Integer: " )
    if b_plain is 0:
        b_plain = input( "Enter non zero integer:")
    a_cipher     = encryption( noise, key, a_plain, mod=mod )
    b_cipher     = encryption( noise, key, b_plain, mod=mod )
    c       = a_cipher * b_cipher
    d       = decryption( key, c, mod=mod )
    print( "Result\n________________________________________________")
    print( "First Integer: %d \nSecond Integer: %d \n" % ( a_plain, b_plain ) )
    print( "Encrypted First Integer: %d \nEncrypted Second Integer: %d \n" % ( a_cipher, b_cipher ) )
    print( "Encrypted Result of Multiplication:------- %d \nDecrpyted Result of Multiplication:-------- %d \n \n" % ( c, d ) )

def divide():
    mod = 100
    noise   = random.getrandbits(3)
    key   = key_gener( noise, mod=mod )
    print( "Verifying Dividing Operation:___________________________________________________\n" )

    a_plain= input( "Enter First Integer: " )
    if a_plain is 0:
        a_plain = input( "Enter non zero integer:")
    b_plain= input( "Enter Second Integer: " )
    if b_plain is 0:
        b_plain = input( "Enter non zero integer:" )
    a_cipher     = encryption( noise, key, a_plain, mod=mod )
    b_cipher     = encryption( noise, key, b_plain, mod=mod )
    c       = a_cipher / b_cipher
    d       = decryption( key, c, mod=mod )
    print( "Result\n________________________________________________")
    print( "First Integer: %d \nSecond Integer: %d \n" % ( a_plain, b_plain ) )
    print( "Encrypted First Integer: %d \nEncrypted Second Integer: %d \n" % ( a_cipher, b_cipher ) )
    print( "Encrypted Result of Division:------- %d \nDecrpyted Result of Division:-------- %d \n \n" % ( c, d ) )


add()
subtract()
mult()
"divide()"
