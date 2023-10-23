def isPrime(n):
    if n >= 2 and n < 100:
        for i in range(2,int(n/2)+1):
            if n % i == 0:
                return False
        return True
    else: 
        print("Number is not in specified parameters")
    
for i in range(2,100):
    print(i, isPrime(i) ,"\n")
        