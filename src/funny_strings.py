def funny_strings(s):
    rInt = []
    sInt = []
    r = s[::-1]
    for i in range(len(s) - 1):
        rInt.append(abs(ord(r[i]) - ord(r[i + 1])))
        sInt.append(abs(ord(s[i]) - ord(s[i + 1])))
    if rInt == sInt:
        return "Funny"
    else:
        return "Not Funny"
