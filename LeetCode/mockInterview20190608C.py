while 1:
    def solve(pattern, str):
        P_list = ["" for i in range(30)]

        str = list(str.split())
        cnt = 0
        for i in pattern:
            if len(P_list[ord(i) - ord("a")]) == 0:
                P_list[ord(i) - ord("a")] = str[cnt]
            elif P_list[ord(i) - ord("a")] != str[cnt]:
                return False
            cnt += 1
        P_list.sort()
        print(P_list)
        for i in range(1, len(P_list)):
            if P_list[i] == P_list[i - 1] and len(P_list[i]) > 0:
                return False

        return True

    pattern = "abba"
    str = "dog cat cat dog"
    pattern = "abba"
    str = "dog cat cat dog"
    print(solve(pattern, str))
    break