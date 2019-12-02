import random
def Sender(g,n):
    x=random.randint(10**4,10**6)
    global A
    A=(g**x)%n
    return x

def Reciever(g,n):
    y=random.randint(10**4,10**6)
    global B
    B=(g**y)%n
    return y

A=0
B=0
g=15485863
n=179424673
x=Sender(g,n)
y=Reciever(g,n)
KS=(B**x)%n
KR=(A**y)%n
print("Sender: ",KS)
print("Reciever: ",KR)