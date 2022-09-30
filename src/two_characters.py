from itertools import combinations


def two_characters(s):
    results = []
    st = list(set(s))
    if len(st) < 2:
        return 0
    else:
        combos = list(combinations(st, len(st) - 2))
        # print(combos)
        for i in combos:
            skip = False
            temp = s
            for x in i:
                temp = temp.replace(x, "")
            # print(temp)
            for y in range(len(temp) - 1):
                if temp[y] == temp[y + 1]:
                    skip = True
                    break
            if not skip:
                results.append(len(temp))
            else:
                results.append(0)

    return max(results)
