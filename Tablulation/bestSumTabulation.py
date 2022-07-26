def bestSum(target, numbers):
    if target == 0:
        return []

    table = [None for _ in range(target + 1)]
    table[0] = []

    for i in range(0, target + 1):
        if table[i] != None:
            for num in numbers:
                if i + num <= target:
                    temp = table[i] + [num]
                    if (table[i + num] is None) or (len(table[i + num]) > len(temp)):
                        table[i + num] = temp

    return table[target]


"""
Time  - O(m^2 * n)
Space - O(m^2)
"""

print(bestSum(7, [5, 3, 4]))
print(bestSum(7, [5, 3, 4, 7]))
print(bestSum(7, [2, 3]))
print(bestSum(8, [2, 3, 5, 8]))
print(bestSum(300, [7, 14]))
print(bestSum(100, [10, 25, 4, 90, 14]))
print(bestSum(100, [10, 25, 14]))
print(bestSum(8, [1, 4, 14]))
