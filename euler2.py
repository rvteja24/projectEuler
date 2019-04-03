#Sum of even fibonacci number whose value is less than 4 million

a = 1
b = 2
temp = 0
sumOfEvenFibonacci = 2
while temp < 4000000:
    temp = a + b
    if ( temp%2 == 0):
       sumOfEvenFibonacci   = sumOfEvenFibonacci + temp
    a = b
    b = temp
print(sumOfEvenFibonacci)
