a = int(input())
if a % 4 == 1 or a % 4 == 2:
    print("IMPOSSIBLE")
elif a % 4 == 3:
    print("++-" + "+--+" * (a // 4))
else:
    print("+--+" * (a // 4))
