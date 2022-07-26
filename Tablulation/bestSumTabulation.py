def howSum(target, numbers):
    if target == 0:
        return []

    table = [None for _ in range(target + 1)]
    table[0] = []

    for i in range(0, target + 1):
        if table[i] != None:
            for num in numbers:
                if i + num <= target:
                    temp = table[i].copy()
                    temp.append(num)
                    table[i + num] = temp

    return table[target]


"""
Time  - O(m^2 * n)
Space - O(m^2)
"""

print(howSum(7, [5, 3, 4]))
print(howSum(7, [5, 3, 4, 7]))
print(howSum(7, [2, 3]))
print(howSum(8, [2, 3, 5]))
print(howSum(300, [7, 14]))
