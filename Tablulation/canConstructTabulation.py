def canConstructTabulation(target, wordbank):
    if target == "":
        return True

    table = [False]*(len(target)+1)
    table[0] = True

    for i in range(0, len(target)+1):
        if table[i]:
            for word in wordbank:
                # if the word matched the characters starting at position i
                if target[i:].startswith(word):
                    table[i+len(word)] = True

                if table[len(target)]:
                    return table[len(target)]

    return table[len(target)]


"""
Time  - O(m^2 * n)
Space - O(m^2)
"""
    
print(canConstructTabulation("abcdef", ["ab", "abcd", "cd", "abc", "def", "f"]))
print(canConstructTabulation("skateboard", ["bo", "rd", "ate", "ska", "sk", "boar"]))
print(
    canConstructTabulation(
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
