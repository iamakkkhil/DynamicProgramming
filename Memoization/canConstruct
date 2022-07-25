def canConstructBrute(target, wordbank):
    if target == "":
        return True

    for word in wordbank:
        if target.startswith(word):
            suffix = target[len(word) :]
            if canConstructBrute(suffix, wordbank):
                return True

    return False


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

# print(canConstructBrute("abcdef", ["abc", "ab", "cd", "def", "abcd"]))
# print(canConstructBrute("skateboard", ["bo", "rd", "ate", "ska", "sk", "boar"]))
# print(
#     canConstruct(
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


def canConstruct(target, wordbank, memo=dict()):
    if target in memo:
        return memo[target]
    if target == "":
        return True

    for word in wordbank:
        if target.startswith(word):
            suffix = target[len(word) :]
            if canConstruct(suffix, wordbank, memo):
                memo[target] = True
                return memo[target]

    memo[target] = False
    return memo[target]


"""
Slicing
Time - O(m)
Space - O(m)
 |
 |
 ↓ 
Time - O(n * m * m)   (Now we are only trying the combinations)
Space - O(m * m)
"""


print(canConstruct("abcdef", ["abc", "ab", "cd", "def", "abcd"]))
print(canConstruct("skateboard", ["bo", "rd", "ate", "ska", "sk", "boar"]))
print(
    canConstruct(
        "eeeeeeeeeeeeeeeeeeeeeeeef",
        ["e", "ee", "eee", "eeee", "eeeee", "eeeeeeee", "eeeeeeeeeeee"],
    )
)
