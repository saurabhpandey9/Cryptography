# Keyless Transaposition Cipher
def encrypt(plain):
	i = 0
	j = 1
	cipher = ""
	cipher1 = ""
	cipher2 = ""
	while(i < len(plain)):
		cipher1 += plain[i]
		i += 2
	while(j < len(plain)):
		cipher2 += plain[j]
		j += 2
	pos = len(cipher1)
	cipher = cipher1 + cipher2
	return(cipher, pos)

def decrypt(cipher, pos):
        i = 0
        j = pos
        k = j
        plain = ""
        while(i < k and j < len(cipher)):
                plain += cipher[i] + cipher[j]
                i += 1
                j += 1
        if(i < k):
                plain += cipher[i]
        return plain

plain = input("Enter the plain text: ")
cipher, pos = encrypt(plain)
print("After encryption: ", cipher)
plain = decrypt(cipher, pos)
print("After decryption: ", plain)