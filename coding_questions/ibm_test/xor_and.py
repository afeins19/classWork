# for an array arr of n-positive integers, count the unordered paris (i,h)
# (0<=i<=j) where arr[i] XOR arr[j] > arr[i] AND arr[j]

# EXAMPLE:
# given n=4, arr = [4,3,5,2]
# IDX  | XOR | AND | IS XOR > AND?
# (0,1)   7     0       TRUE
import math

arr = [4,3,5,2] 
n = len(arr)

count = 0

for i in range(n-1):
    for j in range(i+1,n): 
        xor_op = arr[i] ^ arr[j]
        and_op = arr[i] & arr[j]

        if xor_op > and_op:
            count+=1 

print(count)


def decToBin(val):
    bin_positions = []

    while val != 0:
        cur_bit = val % 2
        bin_positions.append(cur_bit)
        val = val // 2

    return [i for i in reversed(bin_positions)]

def binToDec(val):
    converted_val = 0
    n = len(val)

    for i in range(n):
        cur = val[i] * (2 ** (n-i-1))
        converted_val += cur

    return converted_val


def convertWithPadding(a,b):
    a_bin = decToBin(a)
    b_bin = decToBin(b)

    diff = abs(len(a_bin) - len(b_bin))
    
    # padding with 0's 
    if len(a_bin) != len(b_bin): 
        prepend_count = [0 for i in range(0,diff)]
        print(prepend_count)

        if len(a_bin) > len(b_bin):
            b_bin = prepend_count + b_bin
        
        elif len(a_bin) < len(b_bin):
            a_bin = prepend_count + a_bin
        
    return (a_bin, b_bin)

def xor(a,b): 
    a_bin, b_bin= convertWithPadding(a,b)

    arr = []
    for i in range(len(a_bin)-1): 
        if a_bin[i] == b_bin[i]:
            arr.append(0)
        else:
            arr.append(1)

    return binToDec(arr)



