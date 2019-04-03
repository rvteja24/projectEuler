#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#Find the largest palindrome made from the product of two 3-digit numbers.

a=100
b=[]
c=[]
palin=[]
pal=True
temp=0

for i in range (900):
    b.append(a)
    a += 1

for i in range(900):
    for j in range(900):
        l = b[i] * b[j]
        c.append(l)
        
        

for i in range(900*900):
    m = list(str(c[i]))
    for j in range(len(m)):
        if(m[j] == m[len(m)-1-j]):
            pal=True
        else:
            pal=False
            break
    if(pal == True) and (c[i]>temp):
        temp = c[i]
        
        

print(temp)

