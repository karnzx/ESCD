# 0 < n < 30
def stair_case(n, pattern="#"):
    result = ""
    for i in range(n):
        result += f"{pattern*(i+1):>{n}}\n"
    # print(result)
    return result
