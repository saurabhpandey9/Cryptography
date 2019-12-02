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

def CRT(a,b,p,q):
    return ((a*q*modInverse(q,p)+b*p*modInverse(p,q))%(p*q))

def Keygen():
    p=int(input("Enter P: "))
    q=int(input("Enter Q: "))
    n=p*q
    return n,p,q

def Encrypt(P,n):
    C=(P**2)%n
    return C

def Decrypt(C,p,q,h):
    a1=(C**((p+1)//4))%p
    a2=-1*((C**((p+1)//4))%p)
    b1=(C**((q+1)//4))%q
    b2=-1*((C**((q+1)//4))%q)
    p1=CRT(a1,b1,p,q)
    p2=CRT(a1,b2,p,q)
    p3=CRT(a2,b1,p,q)
    p4=CRT(a2,b2,p,q)
    if hash(p1)==h:
        return p1
    elif hash(p2)==h:
        return p2
    elif hash(p3)==h:
        return p3
    else:
        return p4

msg=input("Enter plain text: ")
pub_key,pri_key1,pri_key2=Keygen()
H=[hash(ord(m)) for m in msg]
Cblos=[chr(Encrypt(ord(m),pub_key)) for m in msg]
Cipher="".join(Cblos)
print()
print("Encrypted Text: ",Cipher)
print()
Dblos=[chr(Decrypt(ord(Cipher[j]),pri_key1,pri_key2,H[j])) for j in range(len(Cipher))]
Plain="".join(Dblos)
print("Decrypted Text: ",Plain)