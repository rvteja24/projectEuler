#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


smallestDivisible=True
smallestDivisibleNumber=0

for i in range(10000000,1000000000,10):
    for j in range(2,21):
        if(i % j == 0):
            smallestDivisible=True
        else:
            smallestDivisible=False
            break
    if(smallestDivisible == True):
        smallestDivisibleNumber = i
        break
    

print(smallestDivisibleNumber)
