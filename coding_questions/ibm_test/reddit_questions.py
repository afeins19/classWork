"""


2 people A and B have same length of array all contains int, and with a startFlag odd and even. 
what you need to do is to calculate the sum of arrayA-arrayB of each odd item or even item (based on startFlag). 
if sum >0, A wins, output A's name, if sum<0, output B's name, if sum==0, output Tie
like:
    Tom=[2,2,3]
    Jerry=[3,1,4]
    flag=odd
    sum = (2-3)+(3-4)=-2

output "Jerry"

2. given an integer, if 2 adjecent digit are both odd or even, we can do a swap for these digit.
Like for 597683
swap 5 and 9 -> 957683
swap 5 and 7 -> 975683
swap 6 and 8 -> 975863

get largest number 975863 
"""

# Question 1 
def q1(p1:tuple[str, list[int]], p2:tuple[str, list[int]], startFlag):
    p1_name = p1[0]
    p2_name = p2[0]

    jump = 0
    if startFlag == "even":
        jump = 1 

    p1_val = 0
    for i in range(jump, len(p1[1]), 2):
        p1_val += (p1[1][i] - p2[1][i])

    if p1_val > 0: 
        return p1_name
    return p2_name

print(q1(['greg', [1,2,3]], ['perpo', [4,5,-15]], "even"))


# Question 2 
def bothEvenOrOdd(a,b):
    return (a % 2 == 0 and b % 2 == 0) or (a % 2 != 0 and b % 2 != 0)

def q2(val):
    vald = [int(i) for i in (str(val))]
    out = []

    for i in range(0, len(vald)-1, 2):
        if bothEvenOrOdd(vald[i], vald[i+1]): 
            out.extend([vald[i+1], vald[i]])
        else:
            out.extend([vald[i], vald[i+1]])
    
    # edge case - odd number
    if len(vald) % 2 != 0:
        out.append(vald[-1]) # add last val 

    return ''.join([str(i) for i in out])

print(q2(123))
     
            
            