def solved(n):
    nowans = []
    ansList = []
    def solved2(n, endcnt, nowans, ansList):
        if n >= 1:
            solved2(n - 1, endcnt + 1, nowans + ["("], ansList)
        if endcnt >= 1:
            solved2(n, endcnt - 1, nowans + [")"], ansList)
        if n == 0 and endcnt == 0:
            ansList.append("".join(nowans))
        return ansList

    ans = (solved2(n, 0, nowans, ansList))
    return ans

print(solved(3))