def countConstructBrute(target, wordbank):
    if target == "":
        return 1

    totalCount: int = 0
    for word in wordbank:
        if target.startswith(word):
            suffix = target[len(word):]
            n_ways = countConstructBrute(suffix, wordbank)
            totalCount += n_ways

    return totalCount


"""
Slicing
Time - O(m)
Space - O(m)
 |
 |
 ↓
Time - O(n^m * m)
Space - O(m * m)
"""


# print(countConstructBrute("abcdef", ["abc", "ab", "cd", "def", "abcd"]))
# print(countConstructBrute("skateboard", ["bo", "rd", "ate", "ska", "sk", "boar"]))
# print(countConstructBrute("purple", ["purp", "p", "ur", "le", "purpl"]))
# print(
#     countConstructBrute(
#         "eeeeeeeeeeeeeeeeeeeeeeeef",
#         ["e",
#          "ee",
#          "eee",
#          "eeee",
#          "eeeee",
#          "eeeeeeee",
#          "eeeeeeeeeeee"
#         ],
#     )
# )


def countConstruct(target, wordbank, memo=dict()):
    if target in memo: return memo[target]
    if target == "":
        return 1

    totalCount: int = 0
    for word in wordbank:
        if target.startswith(word):
            suffix = target[len(word):]
            n_ways = countConstruct(suffix, wordbank, memo)
            totalCount += n_ways

    memo[target] = totalCount
    return memo[target]


"""
Slicing
Time - O(m)
Space - O(m)
 |
 |
 ↓
Time - O(n * m * m)
Space - O(m * m)
"""


print(countConstruct("abcdef", ["abc", "ab", "cd", "def", "abcd"]))
print(countConstruct("skateboard", ["bo", "rd", "ate", "ska", "sk", "boar"]))
print(countConstruct("purple", ["purp", "p", "ur", "le", "purpl"]))
print(
    countConstruct(
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
