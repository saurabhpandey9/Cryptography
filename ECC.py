import math
import random

def isPerfectSquare(x):
    sr = math.sqrt(x)
    return ((sr - math.floor(sr)) == 0)

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

def GF(a,b,N):
    L=list()
    for x in range(N):
        w=(x**3+a*x+b)%N
        if isPerfectSquare(w):
            L.append([x,int(w**0.5)])
            L.append([x,int(-1*(w**0.5)%N)])
    return L

def ptadd(a,b,N,P,Q):
    R=list()
    if(P[0]==Q[0] and P[1]==((-1*Q[1])%N)):
        print("Exception : Points at infinity. Please Try again...:(")
        exit()
    if P==Q:
        l=((3*(P[0]**2)+a)*(modInverse(2*P[1],N)))%N
        R.append(((l**2)-(2*P[0]))%N)
        R.append((l*(P[0]-R[0])-P[1])%N)
        return R
    else:
        l=((Q[1]-P[1])*(modInverse((Q[0]-P[0]),N)))%N
        R.append(((l**2)-(P[0]+Q[0]))%N)
        R.append((l*(P[0]-R[0])-P[1])%N)
        return R

def ptsub(a,b,N,P,Q,s):
    Q1=[Q[0],(-1*Q[1])%N]
    p = ptadd(a,b,N,P,Q1)
    if p==s:
        return p
    else:
        return s

def ptmul(a,b,N,k,P):
    S=P
    for j in range(k-1):
        S=ptadd(a,b,N,S,P)
    return S

def keygen(a,b,N,L):
    e1=random.choice(L)
    d=random.randint(1,100)
    e2=ptmul(a,b,N,d,e1)
    return [e1,e2],d

def Encrypt(a,b,N,pub,PT):
    r=random.randint(1,100)
    c1=ptmul(a,b,N,r,pub[0])
    c2=ptadd(a,b,N,PT,ptmul(a,b,N,r,pub[1]))
    return c1,c2

def Decrypt(a,b,N,pri,C,s):
    PT=ptsub(a,b,N,C[1],ptmul(a,b,N,pri,C[0]),s)
    return PT

print("Let y2=x3+ax+b be an EC.")
print("For above EC:-")
a=int(input("Choose a: "))
b=int(input("Choose b: "))
N=int(input("Enter Large Prime No.: "))
if(4*(a**3)+27*(b**2)==0):
    print("Invalid Coeff's : Singular EC")
    exit()
G=GF(a,b,N)
print("Gallo's Field Points on Curve are:-")
print(G)
pubkey,prikey=keygen(a,b,N,G)
msg=G[int(input("From above list, Choose Point index[0 to "+str(len(G)-1)+"], as plain text: "))];m=msg
print("Plain text Chosen: ",msg)
C=Encrypt(a,b,N,pubkey,msg)
print("Encrypted Text:")
print(C[0]," & ",C[1])
P=Decrypt(a,b,N,prikey,C,m)
print("Decrypted Text:")
print(P)
