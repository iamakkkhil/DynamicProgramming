def bestSumBrute(targetSum, numbers):
    if targetSum == 0:
        return []
    if targetSum < 0:
        return None

    shortestCombination = None

    for num in numbers:
        remainder = targetSum - num
        resp = bestSumBrute(remainder, numbers)

        if resp is not None:
            resp.append(num)
            if shortestCombination is None or len(shortestCombination) > len(resp):
                shortestCombination = resp

    return shortestCombination


print(bestSumBrute(7, [5,3,4,7]))
print(bestSumBrute(8, [1,4,5]))

# m = target sum
# n = numbers length

# Time Complexity = O(n^m * m)
# Space Complexity = O(m*m)

            
def bestSum(targetSum, numbers, memo = {}):
    if targetSum in memo: return memo[targetSum]
    if targetSum == 0: return []
    if targetSum < 0: return None
    
    shortestCombination = None
    for num in numbers:
        remainder = targetSum - num
        remainderCombination = bestSum(remainder, numbers, memo)
        
        if remainderCombination is not None:
            resp = remainderCombination.copy()
            resp.append(num)
            # remainderCombination.append(num) 
            if shortestCombination is None or len(resp) < len(shortestCombination):            
                shortestCombination = resp
            
    memo[targetSum] = shortestCombination
    return shortestCombination
    
if __name__ == '__main__':
    print(bestSum(4, [2, 1], memo=dict()))    #Output  [2, 2] 
    print(bestSum(100, [1, 2, 5, 25], memo=dict()))

