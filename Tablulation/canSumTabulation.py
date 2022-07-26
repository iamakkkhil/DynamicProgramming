def canSum(target, numbers):
    if target == 0:
        return True
        
    table = [False] * (target+1)
    table[0] = True

    for i in range(0, target+1):
        if table[i]:
            for num in numbers:
                if i+num <= target:
                    table[i+num] = True

                if table[target]:
                    return table[target]

    return table[target]
            

"""
m = numbers.length
n = target

Time  - O(m*n)
Space - O(n)
"""


print(canSum(7, [6,0,1]))
