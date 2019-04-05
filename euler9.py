#product of pythagorean triplet for the condition a+b+c = 1000

a = 1
b = 1
c = 1

for i in range(1,500):
    a = i
    for j in range(1,500):
        b = j
        for k in range(1,500):
            c = k
            if(a+b+c == 1000) and (a*a + b*b == c*c):
                print(a*b*c)
                
                
            
        
    


