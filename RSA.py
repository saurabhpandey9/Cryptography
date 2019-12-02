import math
import random

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

def phi(p,q):
    return (p-1)*(q-1)

def genkey(p,q):
    phv=phi(p,q)
    n=p*q
    choice=list()
    for j in range(1,phv):
        if math.gcd(j,phv)==1:
            choice.append(j)
    e=random.choice(choice)
    d=modInverse(e,phv)
    return e,d,n


def Encrypt(msg,e,n):
    C=(msg**e)%n
    return C

def Decrypt(cip,d,n):
    P=(cip**d)%n
    return P

p=int(input("Chose P:"))
q=int(input("Chose Q:"))
M=input("Enter message:")
pubkey,prikey,n=genkey(p,q)
Cblos=[chr(Encrypt(ord(m),pubkey,n)) for m in M]
Cipher="".join(Cblos)
print()
print("Encrypted Text:")
print(Cipher)
print()
Dblos=[chr(Decrypt(ord(m),prikey,n)) for m in Cipher]
Plain="".join(Dblos)
print("Decrypted Text:")
print(Plain)