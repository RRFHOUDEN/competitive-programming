n = int(input())
a = list(map(int, input().split()))
ans = 0
max_takahashi = -10 ** 10
for i in range(n):
    j_aoki = -10 ** 10
    j_takahashi = -10 ** 10
    for j in range(n):
        if i == j:
            continue

        if i < j:
            now_aoki = 0
            now_takahashi = 0
            for k in range(i, j+1):
                if (k-i) % 2 == 0:
                    now_takahashi += a[k]
                else:
                    now_aoki += a[k]
            if j_aoki < now_aoki:
                j_aoki = now_aoki
                j_takahashi = now_takahashi

        if j < i:
            now_aoki = 0
            now_takahashi = 0
            for k in range(j, i+1):
                if (k-j) % 2 == 0:
                    now_takahashi += a[k]
                else:
                    now_aoki += a[k]
            if j_aoki < now_aoki:
                j_aoki = now_aoki
                j_takahashi = now_takahashi

    if max_takahashi < j_takahashi:
        max_takahashi = j_takahashi

print(max_takahashi)