def fib(n):
    if n <= 2: return 1
    return fib(n-1)+fib(n-2)


# Memoized Solution
def fib(n, memo=dict()):
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]


print(fib(7))
print(fib(8))
print(fib(9))
print(fib(150))
