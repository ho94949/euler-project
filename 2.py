x = 1
y = 1
ans = 0
while x < 4000000:
    x, y = x+y, x
    if y%2==0: ans += y
    
print (ans) 
