n, m = map(int, input().split())
ans = n * (n - 1) // 2
ans += m * (m - 1) // 2
print(ans)