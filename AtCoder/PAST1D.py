n = int(input())
a = [int(input()) for _ in range(n)]
a.sort()
a_set = set(a)
correct = 1
for i in range(1, n):
    if a[i] == a[i - 1]:
        correct = 0
        print(a[i], end=" ")
        break
for i in range(1, n+1):
    if not i in a_set:
        print(i, end = "")
        break


if correct:
    print("Correct")
else:
    print()