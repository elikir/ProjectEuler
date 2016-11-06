#By listing the first six prime numbers:
#  2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?


#is_prime
# consumes a number n and returns true if prime
# else false
# input: 1,4,6
# output: False
# input: 2,3,5,7,11
# output: True
#-------
# The limitation to this problem is my lack of mathematics regarding primes,
# though I know more advanced ways of finding primes, Java would be more suitable
# due to ArrayLists, allowing me to create a seive and find the 10001st prime
def is_prime(n):
    for x in range(2,n):
        if n%x==0:
            return False
    return True

#nth_prime
# consumes a number n and finds the nth prime
# input: 6
# output: 13
def nth_prime(n):
    count = 0
    start = 1
    while count < n:
        start+=1
        if is_prime(start):
            count+=1
    return start


# final thoughts
# this problem took near 60 seconds to solve
# much more optimization is needed
if __name__ == '__main__':
    solution = nth_prime(10001)
    print solution