#largest prime factor of 600851475143

def isPrime(n):
    if n==2 or n==3: return True
    if n%2==0 or n<2: return False
    for i in range(3,int(n**0.5)+1,2):   # only odd numbers
        if n%i==0:
            return False

    return True
original = 600851475143
w = int(original**.5)+1
divisors = []
while w > int(w**.5+1):
    if original%w==0:
        divisors.append(w)
    w-=1
#divisors starts from the largest numbers so i can break at the first prime one
for div in divisors:
    if isPrime(div):
        print div
        break