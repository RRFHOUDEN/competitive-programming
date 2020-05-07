n = int(input())
a = [int(input()) for _ in range(n)]

left = [a[0]]
right = [a[-1]]
for i in range(1, n):
    left.append(max(left[i-1], a[i]))
    right.append(max(right[i-1], a[n-i-1]))
right = right[::-1]
print(right[1])

for i in range(1, n-1):
    print(max(left[i-1], right[i+1]))
print(left[-2])