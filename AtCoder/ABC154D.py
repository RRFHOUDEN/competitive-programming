def solve(k, m, i, s):
    if i >= len(dp):
        if k == 0:
            return 1
        if k > 0:
            return 0

    if len(str(n)) - i < k:
        return 0

    ans = 0
    if s:
        if k > 0:
            ans += dp[i][2] * solve(k - 1, 0, i + 1, 0)
            ans += solve(k - 1, m, i + 1, 0)
        else:
            return 1
        return ans

    if k > 0:
        if len(str(n)) - i == k:
            if m:
                if str(n)[i] == "0":
                    return 0
                #小さい値を取る
                ans += dp[i][2] * solve(k - 1, 0, i + 1, 0)
                #ちょうどの値を取る
                ans += solve(k - 1, 1, i + 1, 0)
            else:
                ans += dp[i][1] * solve(k - 1, 0, i + 1, 0)

        if m:
            if str(n)[i] == "0":
                #そもそもn[i]が0
                ans += solve(k, 1, i + 1, 0)
            else:
                #小さい値を取る
                ans += dp[i][2] * solve(k - 1, 0, i + 1, 0)
                #ちょうどの値を取る
                ans += solve(k - 1, 1, i + 1, 0)
                #0を取る
                ans += solve(k, 0, i + 1, 0)

        else:
            ans += dp[i][1] * solve(k - 1, 0, i + 1, 0)
            ans += dp[i][0] * solve(k, 0, i + 1, 0)
    else:
        ans += 1


    return ans