import math
def modInverse(a, m) : 
    m0 = m 
    y = 0
    x = 1
  
    if (m == 1) : 
        return 0
  
    while (a > 1) :
        q = a // m
        t = m
        m = a % m 
        a = t 
        t = y
        y = x - q * y 
        x = t
    if (x < 0) : 
        x = x + m0
    return x

def Encrypt(msg,key):
    Cip=[chr(((ord(x)-65)*key)%26+65) for x in msg]
    return "".join(Cip)

def Decrypt(msg,key):
    Plain=[chr(((ord(x)-65)*modInverse(key,26))%26+65) for x in msg]
    return "".join(Plain)

msg=input("Enter message: ").upper()
key=int(input("Enter the Key: "))
if math.gcd(key,26)!=1:
    print("Invalid Key.")
    exit()
CT=Encrypt(msg,key)
print("Encrypted Text:",CT)
PT=Decrypt(CT,key)
print("Decrypted Text:",PT)