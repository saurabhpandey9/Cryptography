import numpy as np
import random
#X=np.array([chr(x) for x in range(65,91) and x!=73])
Key=np.array([['L','G','D','B','A'],['Q','M','H','E','C'],['U','R','N','I','F'],['X','V','S','O','K'],['Z','Y','W','T','P']])
msg=input("Enter message: ")
Msg=[x for x in msg]
T=[];i=-1
for x in range(len(Msg)-1):
    if(Msg[x]==Msg[x+1]):
        T+=['1'];i+=1
        T[i]=x+1
for j in T:
    Msg.insert(j,'X')
if len(Msg)%2!=0:
    Msg.append('X')
print("Modified:",Msg)
print()
C=""
for x in range(0,len(Msg)-1,2):
    c1=list(zip(*np.where(Key == Msg[x])))
    c2=list(zip(*np.where(Key == Msg[x+1])))
    if(c1[0][0]==c2[0][0]):
        C+=Key[c1[0][0]][(c1[0][1]+1)%5]+Key[c1[0][0]][(c2[0][1]+1)%5]
    elif(c1[0][1]==c2[0][1]):
        C+=Key[(c1[0][0]+1)%5][c1[0][1]]+Key[(c2[0][0]+1)%5][c1[0][1]]
    else:
        C+=Key[c1[0][0]][c2[0][1]]+Key[c2[0][0]][c1[0][1]]
print("Cipher text:",C)
print("Decrypted Text:",msg)