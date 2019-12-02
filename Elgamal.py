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

#primitive root
def PR(p):
    L=list()
    h=dict()
    for x in range(1,p):
        for t in range(1,p):
            h[t]=0
        for j in range(1,p):
            h[(x**j)%p]=1
        #print(h)
        L.append(x)
        for x in h.values():
            if x==0:
                L.pop()
                break
    return L


def keygen(p):
    d=random.choice(list(range(1,p-1)))
    print(PR(p))
    e1=random.choice(PR(p))
    e2=(e1**d)%p
    return d,e1,e2

def encrypt(e1,e2,p,M):
    r=random.choice(list(range(1,p-1)))
    c1=(e1**r)%p
    c2=(M*(e2**r))%p
    return c1,c2

def decrypt(c1,c2,d,p):
    m = ((c2%p)*modInverse((c1**d),p))%p
    return m

p=int(input("Enter Prime: "))
d,e1,e2=keygen(p)
msg=int(input("Enter msg: "))
c1,c2=encrypt(e1,e2,p,msg)
print("Encrypted Text: ",c1," & ",c2)
m=decrypt(c1,c2,d,p)
print("Decrypted Text: ",m)
