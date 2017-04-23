ansv = 0
ansi = 0
for i in range(1, 1000000):
    
    cnt = 0
    v = i
    while v != 1:
        if v%2==0: v //= 2
        else: v = 3*v+1
        cnt += 1
    if ansv < cnt:
        ansv = cnt
        ansi = i

print(ansi)
