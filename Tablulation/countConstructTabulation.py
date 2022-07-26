def countConstructTabulation(target, wordbank):
    if target == "":
        return 1

    table = [0] * (len(target)+1)
    table[0] = 1

    for i in range(len(target)+1):
        if table[i] > 0:
            for word in wordbank:
                if target[i:].startswith(word):
                    table[len(word)+i] += table[i]

    return table[len(target)]


"""
Time  - O(m^2 * n)
Space - O(m^2)
"""


print(countConstructTabulation("purple", ["purp", "p", "ur", "le", "purpl"]))
print(countConstructTabulation("abcdef", ["ab", "abcd", "cd", "abc", "def", "f"]))
print(countConstructTabulation("skateboard", ["bo", "rd", "ate", "ska", "sk", "boar"]))
print(
    countConstructTabulation(
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
                
