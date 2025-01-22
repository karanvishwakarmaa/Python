def mergeAlternately(word1: str, word2: str) -> str:
    merged = []
    i, j = 0, 0

    # Merge characters alternately from both strings
    while i < len(word1) and j < len(word2):
        merged.append(word1[i])
        merged.append(word2[j])
        i += 1
        j += 1

    # Append the remaining characters from word1 or word2
    if i < len(word1):
        merged.append(word1[i:])
    if j < len(word2):
        merged.append(word2[j:])

    return ''.join(merged)


# Example usage
word1 = "abc"
word2 = "pqr"
result = mergeAlternately(word1, word2)
print(result)  # Output: "apbqcr"
