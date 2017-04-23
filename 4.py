ans = 0
for i in range(100, 1000):
    for j in range(100, 1000):
        v = i*j
        if str(v)==str(v)[::-1]: ans = max(ans, v)

print (ans)
