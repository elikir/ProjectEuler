#Find the sum of the even valued fib terms under 4 million


def isFib(n):
    checkOne = (5 * n ** 2) + 4
    checkTwo = (5 * n ** 2) - 4
    if checkOne ** .5 % 1 == 0 or checkTwo ** .5 % 1 == 0:
        return True
    return False


sum = 0
for x in range(4000000):
    if x%2==0:
        if isFib(x):
            sum += x
print sum

