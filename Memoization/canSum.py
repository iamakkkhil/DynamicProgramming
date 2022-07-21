def canSumBrute(targetSum, numbers):
    if targetSum == 0:
        return True
    if targetSum < 0:
        return False

    for num in numbers:
        remainder = targetSum - num
        if canSumBrute(remainder, numbers):
            return True

    return False

    
# Memoized Solution
def canSum(targetSum, numbers, memo={}):
    if targetSum in memo:
        return memo[targetSum]

    if targetSum == 0: return True
    if targetSum < 0: return False

    for n in numbers:
        remainder = targetSum - n
        if canSum(remainder, numbers, memo):
            memo[targetSum] = True
            return True

    memo[targetSum] = False
    return False


print(canSum(7, [5, 3, 4, 7]))
print(canSum(7, [2, 4]))
print(canSum(300, [7, 14]))
