
#takes a list of numbers and sums them
def listsum(numList):
    if len(numList)==1:
        return numList[0]
    else:
        #returns the first item and the remaining tuple (reducing list until the base case)
        return numList[0] + listsum(numList[1:])

print(listsum([1,2,3,4,5]))





