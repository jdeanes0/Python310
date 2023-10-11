def getsum(n):
    if n == 1:
        return 1
    return getsum(n-1) + n

globaln = 10

print(getsum(globaln))

sum = [0]*(globaln+1) # I unironically dislike arrays that start at 0 now.
for i in range(1, globaln+1):
    sum[i] = sum[i-1] + i # plus i, dumbass

print(sum[globaln])

"""
Remember, the entire point of dynamic programming is to think about the sub-functions and
sub-problems of each problem instead of tackling it linearly.
"""
