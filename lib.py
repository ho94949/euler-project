"""
function         isPrime
Version          1
Time Complexity  O(sqrt(x))
Description
Naively divide numbers less than or equal to sqrt(x)
"""
def isPrime(x):
    if x<3: return x==2
    if x%2==0: return False  
    i = 3
    while i*i <= x:
        if x%i==0: return False
        i += 2
    return True

"""
function         tau
Version          1
Time Complexity  O(sqrt(x))
Description
factorize and product of (ki+i)s 
"""
def tau(x):
    if x<1: return 0 
    i = 2 
    ans = 1
    while i*i <= x:
        k = 1
        while x%i == 0:
            x //= i 
            k += 1 
        ans *= k 
        i += 1
    if x != 1: ans *= 2
    return ans