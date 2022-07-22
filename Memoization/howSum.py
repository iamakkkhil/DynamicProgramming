def howSumBrute(targetSum, numbers):
    if targetSum == 0:
        return []
    if targetSum < 0:
        return None

    for num in numbers:
        rem = targetSum - num
        response = howSumBrute(rem, numbers)
        if response is not None:
            response.append(num)
            return response

    return None


# Time Complexity = O(n^m * m)
# Space Complexity = O(m)


# Memoization
def howSum(targetSum, numbers, memo=dict()):
    if targetSum in memo:
        return memo[targetSum]

    if targetSum == 0:
        return []
    if targetSum < 0:
        return None

    for num in numbers:
        rem = targetSum - num
        response = howSum(rem, numbers, memo)
        if response is not None:
            response.append(num)
            memo[targetSum] = response
            return memo[targetSum]

    memo[targetSum] = None
    return memo[targetSum]


# Time Complexity = O(n*m^2)
# Space Complexity = O(m^2)


print(howSum(7, [5, 4, 3, 7], memo=dict()))
print(howSum(7, [2, 3], memo=dict()))
print(howSum(7, [2, 4], memo=dict()))
print(howSum(8, [2, 3, 5], memo=dict()))
print(howSum(0, [2, 3, 5], memo=dict()))
print(howSum(300, [7, 14], memo=dict()))
