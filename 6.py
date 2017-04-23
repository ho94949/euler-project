ans = 0
for i in range(1, 101):
    ans += (i ** 3) - (i ** 2)

print(ans)


"""
Can be solved using square(sum(1..i)) = sum(cube(1..i))
"""
