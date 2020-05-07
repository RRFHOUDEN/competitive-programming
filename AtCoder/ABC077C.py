import bisect

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
a.sort()
b.sort()
c.sort()

cnt = 0
cnt_b = []
for i_b in range(n):
    # if max(c) < b[i_b]:
    #     cnt_b.append(0)
    #     continue
    i_a = bisect.bisect_left(a, b[i_b]) - 1
    i_c = bisect.bisect_right(c, b[i_b])
    if i_a < 0 or n <= i_c:
        continue
    cnt += (i_a + 1) * (n - i_c)
    # print(i_a, i_b, i_c)

print(cnt)