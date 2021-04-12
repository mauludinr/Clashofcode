n = int(input())
for i in range(n):
    b, t = [int(j) for j in input().split()]
    t=t*9/5+32
    if (b==t):print("Same")
    elif (b>t):print("Higher")
    else:print("Lower")
