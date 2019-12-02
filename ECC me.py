
import random
import math

p=0
a=0



#To calculate the possible point on Curve
def points(a, b, p):
	x = 0
	lis = [] #list containing all possible point
	while(x < p):
		temp = ((x ** 3) + (a * x) + b) % p
		if(math.sqrt(temp) % 1 == 0):
			lis.append([x, int(math.sqrt(temp))])
			lis.append([x, (p - int(math.sqrt(temp)))%p])
		x += 1
	return lis

#Finding modinverse
def Inverse(a):
    m=p
    a = a % m; 
    for x in range(1, m) : 
        if ((a * x) % m == 1) : 
            return x 
    return 1

def add(x1,y1,x2,y2):
    if(x2 == "none"):
        return [ x1,y1]
    if(x1== "none"):
        return [x2,y2]
    if(x1==x2 and y2 ==(p-y1)%p):
        return ["none", "none"]
    if(x1==x2 and y1==y2):
        lamda = (((3*x1**2+a)%p)*Inverse((2*y1)%p))%p
    else:
        lamda = (((y2-y1)%p)* Inverse((x2-x1)%p))%p
    x3 = (lamda**2 - x1 - x2)%p
    y3 = ((lamda*(x1 - x3))%p - y1)%p
    return [x3,y3]

def mult(d: int, point):
    ans = point[:]
    for i in range(d-1):
        ans = add(ans[0], ans[1], point[0], point[1])
    return ans

def inversOf(x, y):
    #non represent point at infinity
    if(x=="none"):
        return ["none","none"]
    return [x, (-y)%p]

def encrypt(plain,e1,e2,r):
    c1 = mult(r, e1)
    c2 = add(*plain, *mult(r,e2))
    return [c1,c2]


#decryption
# PT=c2-d*c1
def decrypt(c1,c2, d):
    ans = add(*c2, *inversOf(*mult(d,c1)))
    return ans




print("---------------------------ECC Algorithm-----------------------------------\n")

a, b = list(map(int, input("Enter values of a and b for the elliptical curve:").split()))
p = int(input("Enter prime for the gallois field:"))

print("\nPossible points on curve are: \n", points(a, b, p))

#Bob will choose e1 a point on curve
print("\nChoose point e1 on curve from above list like:3 6 >> ")
e1=list(map(int,input().split()))

d = int(input("Enter any random number as private key:"))


print("Enter a point as plain-text on curve from above list : ")
plain=list(map(int,input().split()))

print("\nKey e1 : ", e1)
e2x, e2y = mult(d, e1) #here e2 will be calculated by BOB
e2 = [e2x, e2y]

print("Key e2 : ", e2)
print("\nPlain text: ", plain)

#Alice select a pair of point as plain text and calculate a pair of points as cipher text
#c1=r*e1 here r is random number calculated below while decryptiong
#c2=PT*e2 
c1, c2 = encrypt(plain, e1,e2, random.randint(1, 10))

print("cipher text :", c1,c2)
print("Decrypt:", decrypt(c1,c2, d))

