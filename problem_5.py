#Find the smallest number that is evenly divisble by all of the numbers from 1 to 20

#smallest_divis
# consumes a starting number baseline
# and increments from baseline to a massive number at baseline increments
# until it finds one that satisfies all divisors from 2-20 (1 is implied)
# ----
# future edits would be find a list of numbers that have multiples and only check those
# such as 18 accounts for 2 3 6 & 9
def smallest_divis(baseline):
    for i in xrange(baseline, 999999999, baseline):
        if all(i % x == 0 for x in range(2,20)):
            return i
    return None

if __name__ == '__main__':
    solution = smallest_divis(20)
    if solution is None:
        print "No success"
    else:
        print solution

