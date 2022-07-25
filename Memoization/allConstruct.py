def allConstructBrute(target, wordbank):
    if target == "":
        return [[]]

    result = []

    for word in wordbank:
        if target.startswith(word):
            suffix = target[len(word):]
            suffixWays = allConstructBrute(suffix, wordbank)
            targetWays = [[word]+way for way in suffixWays]
            # targetWays = list(map(lambda way: [word, *way], suffixWays))

            result.extend(targetWays)

    return result

"""
Time - O(n^m * m)
Space - O(m * m * m)
"""


def allConstruct(target, wordbank, memo={}):
    if target in memo: return memo[target]
    if target == "":
        return [[]]

    result = []

    for word in wordbank:
        if target.startswith(word):
            suffix = target[len(word):]
            suffixWays = allConstruct(suffix, wordbank, memo)
            targetWays = [[word]+way for way in suffixWays]
            # targetWays = list(map(lambda way: [word, *way], suffixWays))
            result.extend(targetWays)

    memo[target] = result
    return result


"""
Slicing
Time - O(m)
Space - O(m)
 |
 |
 ↓
Time - O(n * m * m)
Space - O(m * m * m)
"""



print(allConstruct("purple", ["purp", "p", "ur", "le", "purpl"]))
print(
    allConstruct(
        "eeeeeeeeeeeeeeeeeeeeeeeef",
        ["e",
         "ee",
         "eee",
         "eeee",
         "eeeee",
         "eeeeeeee",
         "eeeeeeeeeeee"
        ],
    )
)
