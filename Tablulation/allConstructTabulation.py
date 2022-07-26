def allConstructTabulation(target, wordbank):
    if target == "":
        return [[]]

    table = [[] for _ in range(len(target)+1)]
    table[0] = [[]]

    for i in range(0, len(target)+1):
        if table[i] != []:
            for word in wordbank:
                # if the word matched the characters starting at position i
                if target[i:].startswith(word):
                    totalWays = [way + [word] for way in table[i]]
                    table[i+len(word)].extend(totalWays)

    return table[len(target)]


"""
Time -  O(n^m)
Space - O(n^m)
"""


print(allConstructTabulation("purple", ["purp", "p", "ur", "le", "purpl"]))
