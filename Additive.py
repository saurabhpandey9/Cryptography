
def Encrypt(msg,key):
    C=[(ord(x)-65+key)%26+65 for x in msg]
    Cip=[chr(x) for x in C]
    return "".join(Cip)

def Decrypt(msg,key):
    C=[(ord(x)-65-key)%26+65 for x in msg]
    Plain=[chr(x) for x in C]
    return "".join(Plain)

msg=input("Enter message: ").upper()
key=int(input("Enter the Key: "))
CT=Encrypt(msg,key)
print("Encrypted Cipher: "+CT)
PT=Decrypt(CT,key)
print("Decrypted Cipher: "+PT)