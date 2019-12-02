import numpy as np
import random
Msg=input("Enter message: ")
X=np.array([(ord(x)-65) for x in Msg])
H=[x for x in Msg]
print("Plain text:",X)
N=len(Msg)
#Key=np.array([[random.randint(0,26) for y in range(N)] for x in range(N)])
Key=np.array([[6,24,1],[13,16,10],[20,17,15]])
print()
print("Key:",Key)
Ikey=(np.linalg.inv(Key))%26
print()
print("Inverse Key:",Ikey)
Temp=np.matmul(Key,X)
C=Temp%26
print()
print("Cipher Text:",C)

T=Ikey%26
P=np.matmul(C,T)
Y=(P%26).astype(int)
print()
print("Recieved:",X)
Plain="".join(H)
print(Plain)