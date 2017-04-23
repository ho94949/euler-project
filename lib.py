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
