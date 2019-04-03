#10001st prime

primes = [2]
prime = True

for i in range(3,200000,2):
    for j in range(2,i):
        if( i%j != 0):
            prime = True
        else:
            prime = False
            break
    if(prime == True):
        primes.append(i)
    if(len(primes) == 10002):
        break
print(primes[10000])
        


            

