#sum_squares
# consumes a number n and produces a sum of EACH square
# from 1 to n
# input: 10
# output: 385
def sum_squares(n):
    sum = 1
    for x in range(2,n+1):
        sum += x**2

    return sum


#square_sum
# consumes a number n and produces a square of the sum
# of all numbers from 1 to n
# input: 10
# output: 3025
def square_sum(n):
    sum = 1
    for x in range (2,n+1):
        sum += x
    return sum**2


if __name__ == '__main__':
    solution = square_sum(100) - sum_squares(100)
    print solution
