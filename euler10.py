# Sum of all primes below 2 million

# create a set excluding even numbers
numbers = set(range(3, 2000001, 2)) 

for number in range(3, int(2000000 ** 0.5) + 1):
    if number not in numbers:
        #number must have been removed because it has a prime factor
        continue

    nums = number
    while nums < 2000000:
        nums += number
        if nums in numbers:
            # Remove multiples of prime found
            numbers.remove(nums)

print(2 + sum(numbers))
