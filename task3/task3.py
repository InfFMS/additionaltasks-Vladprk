a = int(input())
ans = 1
d = 2
while d**2 <= a:
    if a % (d**2) == 0:
        ans = d**2
    d += 1
print(ans)
