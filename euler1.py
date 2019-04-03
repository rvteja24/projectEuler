# Sum of multiples of 3 & 5 in natural numbers less than 1000

sumOfMultiplesOfThreeAndFiveLessThan1000 = 0
number = 0
while number < 1000:
    if(number%3 == 0) or (number%5 ==0):
        sumOfMultiplesOfThreeAndFiveLessThan1000 = sumOfMultiplesOfThreeAndFiveLessThan1000+number
    number = number+1
print(sumOfMultiplesOfThreeAndFiveLessThan1000)
