def gridTravellerBruteForce(m, n):
    if m == 1 and n == 1:
        return 1
    if m == 0 or n == 0:
        return 0

    return gridTravellerBruteForce(m-1, n) + gridTravellerBruteForce(m, n-1)


# Memoized Solution
def gridTraveller(m, n, memo=dict()):
    if m > n:
        key = str(m)+","+str(n)
    else:
        key = str(n)+","+str(m)
    
    if key in memo:
        return memo[key]
        
    if n==1 and m==1:
        return 1
    if n==0 or m==0:
        return 0

    memo[key] = gridTraveller(m-1, n, memo) + gridTraveller(m, n-1, memo)
    return memo[key]


print(gridTraveller(3,3))
print(gridTraveller(5,5))
print(gridTraveller(15,15))
