N = 600851475143

i = 2
ans = 0
while i*i<N:
    if N%i==0:
        N //= i
        ans = i
    else:
        i += 1

print (max(ans,N))
