while 1:
    def solved(A, B, C, D):
        condicate = {}
        for i in A:
            for j in B:
                tmp = i + j
                if tmp in condicate:
                    condicate[tmp] += 1
                else:
                    condicate[tmp] = 1

        ans = 0
        for i in C:
            for j in D:
                tmp = -1 * (i + j)
                if tmp in condicate:
                    ans += condicate[tmp]
                    print(i, j, tmp)

        return ans


    A = [1, 2]
    B = [-2, -1]
    C = [-1, 2]
    D = [0, 2]
    print(solved(A, B, C, D))
    break