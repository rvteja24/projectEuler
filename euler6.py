#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

sumOfSquares = 0
Sum = 0

for i in range(1,101):
    sumOfSquares = sumOfSquares + (i*i)
    Sum = Sum + i
print(sumOfSquares)
print(Sum*Sum)
print((Sum * Sum)-sumOfSquares )
    
