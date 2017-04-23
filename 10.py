from lib import isPrime

ans = 0
for i in range(2000001):
    if isPrime(i):
        ans += i 

print(ans)
