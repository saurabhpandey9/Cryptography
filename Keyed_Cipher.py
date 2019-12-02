import random

def Encrypt(msg,key):
    lm=len(msg)
    lk=len(key)
    for j in range(lk*(lm//lk+1)-lm):
        msg+='X'
    M=[[msg[y*len(key)+x] for x in range(len(key))] for y in range(lm//lk+1)]
    for e in range(len(M)):
        Temp=[M[e][x] for x in key]
        M[e]=Temp
    return "".join(["".join(x) for x in M])

def Decrypt(msg,key):
    M=[[msg[y*len(key)+x] for x in range(len(key))] for y in range(len(msg)//len(key))]
    for e in range(len(M)):
        Temp=[M[e][key.index(x)] for x in range(len(key))]
        M[e]=Temp
    return "".join(["".join(x) for x in M])

msg=input("Enter message: ").upper()
l=int(input("Enter Key length: "))
key=list(range(l))
random.shuffle(key)
print("Key: ",key)
CT=Encrypt(msg,key)
print("Encrypted Text: ",CT)
PT=Decrypt(CT,key)
print("Decrypted Text: ",PT[:len(msg)])