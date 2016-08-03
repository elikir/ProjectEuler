#find the largest palindrome made out of the product of 2 3-digit numbers

def isPal(n):
    n = str(n)
    length = len(n)
    for x in range(0,int(length/2)):
        if n[x] != n[length-1-x]:
            return False
    return True
max = 0
for x in range(100,999):
    for y in range(100, 999):
        check = x*y
        if isPal(check) and check>max:
            max = check
print max