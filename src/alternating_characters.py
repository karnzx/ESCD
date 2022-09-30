def alternating_characters(s):
    count = 0
    for i in range(len(s)):
        if i != 0 and s[i] == s[i - 1]:
            count += 1
    return count
