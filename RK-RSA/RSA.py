"""MAJAI ROIDU"""

import random
#import Crypto as c
from Crypto.Util import number


'''
Euclid's algorithm for determining the greatest common divisor
Use iteration to make it faster for larger integers
'''
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

'''
Euclid's extended algorithm for finding the multiplicative inverse of two numbers
'''
def multiplicative_inverse(e, phi):
    d = 0
    x1 = 0
    x2 = 1
    y1 = 1
    temp_phi = phi
    
    while e > 0:
        temp1 = temp_phi/e
        temp2 = temp_phi - temp1 * e
        temp_phi = e
        e = temp2
        
        x = x2- temp1* x1
        y = d - temp1 * y1
        
        x2 = x1
        x1 = x
        d = y1
        y1 = y
    
    if temp_phi == 1:
        print("c",d+phi)
        return d + phi

'''
Tests to see if a number is prime.
'''
def is_prime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for n in range(3, int(num**0.5)+2, 2):
        if num % n == 0:
            return False
    return True

def generate_keypair(p, q):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError('Both numbers must be prime.')
    elif p == q:
        raise ValueError('p and q cannot be equal')
    #n = pq
    n = p * q

    #Phi is the totient of n
    phi = (p-1) * (q-1)
    print("ph",phi)
    #Choose an integer e such that e and phi(n) are coprime
    e = random.randrange(1, phi)
    print("e",e)
    #Use Euclid's Algorithm to verify that e and phi(n) are comprime
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)

    #Use Extended Euclid's Algorithm to generate the private key
    d = multiplicative_inverse(e, phi)
    
    #Return public and private keypair
    #Public key is (e, n) and private key is (d, n)
    return ((e, n), (d, n))

def encrypt(pk, plaintext):
    #Unpack the key into it's components
    key, n = pk
    #Convert each letter in the plaintext to numbers based on the character using a^b mod m
    cipher = [(ord(char) ** key) % n for char in plaintext]
    #Return the array of bytes
    return cipher

def decrypt(pk, ciphertext):
    #Unpack the key into its components
    key, n = pk
    #Generate the plaintext based on the ciphertext and key using a^b mod m
    plain = [chr((char ** key) % n) for char in ciphertext]
    #Return the array of bytes as a string
    return ''.join(plain)

def read_from_file(file_name="efg.txt"):
    msg = []
    ret_msg = []
    try:
        file = open(file_name,'r')
        msg = file.readlines()
        
    except:
        print("Error : File not Found or List not created")

    for item in msg:
        ret_msg.append(item.replace("\n",""))
    print(ret_msg)
    return ret_msg

def write_to_file(enc_msg,file_name="encrypted.txt"):
    file = open(file_name,"a")
    file.write(enc_msg+"\n")

def gen_prime(n_length):
    prim_num = number.getPrime(n_length)
    return prim_num

#file = raw_input("Enter the file name?")
#print(file)
#read_from_file()
#write_to_file("checking")

 

if __name__ == '__main__':
    '''
    Detect if the script is being run directly by the user
    '''
    plain_msg = []
    encrypted = []
    decrypted = []
    print ("RSA Encrypter/ Decrypter")
    n_len = int(input("Enter length of primu number"))
    p = gen_prime(n_len)
    q = gen_prime(n_len)
    print("\nPrime Number 1 :",p)
    print("\nPrime Number 2 :",q)
    print ("Generating your public/private keypairs now . . .")
    public, private = generate_keypair(p, q)
    print ("Your public key is ", public ," and your private key is ", private)
    #message = raw_input("Enter a message to encrypt with your private key: ")
    file = raw_input("Enter the file name?")
    plain_msg = read_from_file(file)
    file = open("encrypted.txt","w")
    
    for item in plain_msg:
        #n =123456789
        encrypted_msg = encrypt(private, item)
        encrypted.append(encrypted_msg)
        encrypted_msg = ''.join(map(lambda x: str(x), encrypted_msg))
        
        write_to_file(encrypted_msg)

    
    #encrypted_msg = encrypt(private, message)
    #print "Your encrypted message is: "
    #print ''.join(map(lambda x: str(x), encrypted_msg))
    print ("Decrypting message with public key ", public ," . . .")
    print ("Your message is:")
    
    
    for item in encrypted:
        #print item
        decrypted.append(decrypt(public, item))
    
    print(decrypted)
    #print(decrypt(public,encrypted_msg))
    


    