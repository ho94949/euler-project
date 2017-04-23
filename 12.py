from lib import tau 

i = 0
while True:
    i += 1
    v = i*(i+1)//2
    if tau(v) > 500:
        print(v)
        exit()
