n, k, c = map(int, input().split())
s = input()
left_to_right = [0 for _ in range(n)]
right_to_left = [0 for _ in range(n)]

now = 1
i = 0
while i < n:
    if s[i] == "x":
        i += 1
        continue
    left_to_right[i] = now
    now += 1
    i += c + 1
for i in range(1, n):
    if left_to_right[i] == 0:
        left_to_right[i] = left_to_right[i - 1]

s = s[::-1]
now = 1
i = 0
while i < n:
    if s[i] == "x":
        i += 1
        continue
    right_to_left[i] = now
    now += 1
    i += c + 1
right_to_left = right_to_left[::-1]
for i in range(n - 2, -1, -1):
    if right_to_left[i] == 0:
        right_to_left[i] = right_to_left[i + 1]

ans = 0
for i in range(n):
    tmp = 0
    if i - 1 >= 0:
        tmp += left_to_right[i - 1]
    if i + 1 < n:
        tmp += right_to_left[i + 1]
    if tmp < k:
        print(i + 1)