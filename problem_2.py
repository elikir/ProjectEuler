#Find the sum of the even valued fib terms under 4 million
# 5z^2 + 4 or 5z^2 − 4
sum = 0
for x in range(4000000):
    if x%2==0:
        if isFib(x):


def isFib(n):
    checkOne = 5 * n**2 + 4
    checkTwo = 5 * n**2 − 4
    if isinstance(sqrt(checkOne)n int)