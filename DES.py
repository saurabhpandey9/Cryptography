import numpy as np

s1="14 4 3 1 2 15 11 8 3 10 6 12 5 9 0 7 0 15 7 4 14 2 13 1 10 6 12 11 9 5 3 8 4 1 14 8 13 6 2 11 15 12 9 7 3 10 5 0 15 12 8 2 4 9 1 7 5 11 3 14 10 0 6 13"
s2="15 1 8 14 6 11 3 4 9 7 2 13 12 0 5 10 3 13 4 7 15 2 8 14 12 0 1 10 6 9 11 5 0 14 7 11 10 4 13 1 5 8 12 6 9 3 2 15 13 8 10 1 3 15 4 2 11 6 7 12 0 5 14 9"
s3="10 0 9 14 6 3 15 5 1 13 12 7 11 4 2 8 13 7 0 9 3 4 6 10 2 8 5 14 12 11 15 1 13 6 4 9 8 15 3 0 11 1 2 12 5 10 14 7 1 10 13 0 6 9 8 7 4 15 14 3 11 5 2 12"
s4="7 13 14 3 0 6 9 10 1 2 8 5 11 12 4 15 13 8 11 5 6 15 0 3 4 7 2 12 1 10 14 9 10 6 9 0 12 11 7 13 15 1 3 14 5 2 8 4 3 15 0 6 10 1 13 8 9 4 5 11 12 7 2 14"
s5="2 12 4 1 7 10 11 6 8 5 3 15 13 0 14 9 14 11 2 12 4 7 13 1 5 0 15 10 3 9 8 6 4 2 1 11 10 13 7 8 15 9 12 5 6 3 0 14 11 8 12 7 1 14 2 13 6 15 0 9 10 4 5 3"
s6="12 1 10 15 9 2 6 8 0 13 3 4 14 7 5 11 10 15 4 2 7 12 9 5 6 1 13 14 0 11 3 8 9 14 15 5 2 8 12 3 7 0 4 10 1 13 11 6 4 3 2 12 9 5 15 10 11 14 1 7 6 0 8 13"
s7="4 11 2 14 15 0 8 13 3 12 9 7 5 10 6 1 13 0 11 7 4 9 1 10 14 3 5 12 2 15 8 6 1 4 11 13 12 3 7 14 10 15 6 8 0 5 9 2 6 11 13 8 1 4 10 7 9 5 0 15 14 2 3 12"
s8="13 2 8 4 6 15 11 1 10 9 3 14 5 0 12 7 1 15 13 8 10 3 7 4 12 5 6 11 0 14 9 2 7 11 4 1 9 12 14 2 0 6 10 13 15 3 5 8 2 1 14 7 4 10 8 13 15 12 9 0 3 5 6 11"

# Parity Drop (64 bit to 56 bit)
def parity_drop(block_64):
    par_table = [57,49,41,33,25,17,9,1,58,50,42,34,26,18,10,2,59,51,43,35,27,19,11,3,60,52,44,36,63,55,47,39,31,23,15,7,62,54,46,38,30,22,14,6,61,53,45,37,29,21,13,5,28,20,12,4]
    bit_56 = ""
    for index in par_table:
        bit_56 += key_64[index - 1]
    return(bit_56)

# print(key_56)



# Dividing key into two halfes (28 bit each)
def divide_28(key_56):
    first_28 = key_56[:28]
    second_28 = key_56[28:]
    return(first_28, second_28)

# print(first_28, second_28)



# Left shift of 28 bit keys
# Check no. of shifts
def check_nof_shift(round_no):
    if(round_no in [1,2,9,16]):
        nof_shift = 1
    else:
        nof_shift = 2
    return(nof_shift)
# Left shift operation
def left_shift(key, nof_shift):
    shifted = ""
    shifted = key[nof_shift:28] + key[:nof_shift]
    return(shifted)
# a = left_shift(first_28, nof_shift)
# b = left_shift(second_28, nof_shift)
# print("after shifting\n ")
# print(a, " ",b)


#combine two 28-bits parts to one single 56-bit key
def combine(a, b):
    key_56_new = a + b
    return(key_56_new)


# Key compression
def key_compression(key_56):
    comp_table = [14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10, 23, 19, 12, 4, 26, 8, 16, 7, 27, 20, 13, 2, 41, 52, 31, 37, 47, 55, 30, 40, 51, 45, 33, 48, 44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32]
    compressed_key = ""
    for i in comp_table:
        compressed_key += key_56[i - 1]
    return(compressed_key)

# comp_key = key_compression(key_56_new)
# print("compressed key is", comp_key)
# print(len(comp_key))


# KEY GENERATOR


def key_generator_part(round_no, a, b):
    nof_shift = check_nof_shift(round_no)
    a = left_shift(a, nof_shift)
    b = left_shift(b, nof_shift)
    n = a + b
    comp = key_compression(n)
    round_keys.append(comp)
    return(a, b)

def key_generator():
    
    round_no = 1
    nof_shift = check_nof_shift(round_no)
    a = left_shift(first_28, nof_shift)
    b = left_shift(second_28, nof_shift)
    c = a + b
    d = key_compression(c)
    round_keys.append(d)  #1st round key is appended
    for round_no in range(2, 17):
        a, b = key_generator_part(round_no, a, b)

def expansion_pbox(r_bit32):
    ex_pbox_table = [32, 1, 2, 3, 4, 5, 4, 5, 6, 7, 8, 9, 8, 9, 10, 11, 12, 13, 12, 13, 14, 15, 16, 17, 16, 17, 18, 19, 20, 21, 20, 21, 22, 23, 24, 25, 24, 25, 26, 27, 28, 29, 28, 29, 30, 31, 32, 1]
    r_bit48 = ''
    for index in ex_pbox_table:
        r_bit48 += r_bit32[index - 1]
    return(r_bit48)

def xor_operation(a, b):
    result = ''
    for i in range(len(a)):
        if a[i] == b[i]:
            result += '0'
        else:
            result += '1'
    return(result)


def Sbox(OutP):
    sb=[['1' for x in range(64)] for y in range(8)]
    sb[0]=list(map(int,s1.split(' ')))
    sb[1]=list(map(int,s2.split(' ')))
    sb[2]=list(map(int,s3.split(' ')))
    sb[3]=list(map(int,s4.split(' ')))
    sb[4]=list(map(int,s5.split(' ')))
    sb[5]=list(map(int,s6.split(' ')))
    sb[6]=list(map(int,s7.split(' ')))
    sb[7]=list(map(int,s8.split(' ')))
    FO=""
    sray=np.array(sb)
    for j in range(8):
        unit=OutP[j*6:j*6+6]
        row=unit[0]+unit[5]
        ri=int(row,2)
        col=unit[1:5]
        ci=int(col,2)
        Op=str(bin(sray[j][ri*16+ci]).replace("0b",""))
        while(len(Op)<4):
            Op="0"+Op
        FO+=Op
    return FO

def Spbox(V):
    Tp="16 7 20 21 29 12 28 17 1 15 23 26 5 18 31 10 2 8 24 14 32 27 3 9 19 13 30 6 22 11 4 25"
    Spo=[V[x-1] for x in list(map(int,Tp.split(' ')))]
    return "".join(Spo)

def desfunc(R,k):
    R48=expansion_pbox(R)
    Rx=xor_operation(R48,k)
    R32=Sbox(Rx)
    Rout=Spbox(R32)
    return Rout

def Round(X,i,key):
    if i==17:
        return X
    L=X[:32]
    R=X[32:]
    op=desfunc(R,key[i-1])
    O=xor_operation(op,L)
    if i==16:
        F=O+R
    else:
        F=R+O
    return Round(F,i+1,key)

def DRound(X,i,key):
    if i==17:
        return X
    L=X[:32]
    R=X[32:]
    op=desfunc(R,key[i-1])
    O=xor_operation(op,L)
    if i==16:
        F=O+R
    else:
        F=R+O
    return DRound(F,i+1,key)

def Initial(IP):
    InP=[58,50,42,34,26,18,10,2,60,52,44,36,28,20,12,4,62,54,46,38,30,22,14,6,64,56,48,40,32,24,16,8,57,49,41,33,25,17,9,1,59,51,43,35,37,19,11,3,61,53,45,37,29,21,13,5,63,55,47,39,31,23,15,7]
    Mip=[IP[x-1] for x in InP]
    return "".join(Mip)

def Final(FP):
    Fnp=[40,8,48,16,56,24,64,32,39,7,47,15,55,23,63,31,38,6,46,14,54,22,62,30,37,5,45,13,53,21,61,29,36,4,44,12,52,20,60,28,35,3,43,11,51,19,59,27,34,2,42,10,50,18,58,26,33,1,41,9,49,17,57,25]
    Mfp=[FP[x-1] for x in Fnp]
    return "".join(Mfp)


key_64 = "0001001100110100010101110111100110011011101111001101111111110001"
key_56 = parity_drop(key_64)
first_28, second_28 = divide_28(key_56)
round_keys = []
key_generator()
#print(round_keys)
X=input("Enter 64 bit message:")
print("Encrypted cipher:")
Xi=Initial(X)
Xout=Round(Xi,1,round_keys)
Xf=Final(Xout)
print(Xf)
print("Decrypted message:")
DX=Initial(Xf)
# print(round_keys)
# print(round_keys[::-1])
DXout=DRound(DX, 1, round_keys[::-1])
DXf=Final(DXout)
print(X)

#Input  0000000100100011010001010110011110001001101010111100110111101111
#Output 1000010111101000000100110101010000001111000010101011010000000101