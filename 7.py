def isPrime(x):
    i = 2
    while i*i <= x:
        if x%i==0: return False
        i += 1
    return True

i = 2
cnt = 0
while True:
    if isPrime(i): cnt += 1
    if cnt == 10001:
        print(i)
        break
    i += 1
