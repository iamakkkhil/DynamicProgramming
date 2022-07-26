def gridTabulation(m,n):
    if m==0 or n==0:
        return 0
    if m==1 and n==1:
        return 1

    table = [[0]*(n+1) for _ in range(m+1)]

    table[1][1] = 1

    for i in range(0, m+1):
        for j in range(0, n+1):
            current = table[i][j]
            # right neighbour
            if j+1 <= n:
                table[i][j+1] += current
            # down neighbour
            if i+1 <= m:
                table[i+1][j] += current

    return table[m][n]


print(gridTabulation(1,1))
print(gridTabulation(0,0))
print(gridTabulation(2,3))
print(gridTabulation(3,3))
print(gridTabulation(18,18))
