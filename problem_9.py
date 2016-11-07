#A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#a2 + b2 = c2
#For example, 32 + 42 = 9 + 16 = 25 = 52.
#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.




#pythag
# consumes a number and finds the special pythagorean triplet
# under said number that equals the number
# input: 3 4 5
# output: 60
def pythag(n):
    for a in range(1, n):
        for b in range(1, n):
            for c in range(1, n):
                if a + b + c == n and a ** 2 + b ** 2 == c ** 2:
                    return a * b * c


if __name__ == '__main__':
    print pythag(1000)

