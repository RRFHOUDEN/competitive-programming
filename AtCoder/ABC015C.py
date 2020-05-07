def solve(i, now):
    if i >= len(t):
        # print(now)
        tmp = now[0]
        for j in range(1, len(now)):
            tmp = tmp ^ now[j]
        if tmp == 0:
            return True
        return False

    for j in range(len(t[i])):
        if solve(i+1, now+[t[i][j]]):
            return True
    return False

def main(n, k):
    for i in range(len(t[0])):
        if solve(1, [t[0][i]]):
            print("Found")
            return
    print("Nothing")
n, k = map(int, input().split())
t = [list(map(int, input().split())) for _ in range(n)]
main(n, k)