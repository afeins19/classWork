#using the map function
import sys

def square(n):
    return n*n

nums=[i for i in range(10)]

nums_processed = list(map(square, nums))
meta=list(map(square,nums_processed))
print(nums_processed, meta)
