n = int(input())
a = list(map(int, input().split()))

set_a = set()
for i in a:
    while i % 2 == 0:
        i //= 2
    set_a.add(i)
print(len(set_a))