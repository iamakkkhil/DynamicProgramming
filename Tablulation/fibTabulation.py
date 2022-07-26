def fib(n):
    if n == 0: return 0
    if n <= 2: return 1
        
    table = [0]*(n+1)
    table[1] = 1

    for i in range(0, n-1):
        table[i+1] += table[i]
        table[i+2] += table[i]

    table[n] += table[n-1]

    return table[n]


print(fib(6))
print(fib(1000))

"""
Time  -  O(n)
Space -  O(n)
"""
