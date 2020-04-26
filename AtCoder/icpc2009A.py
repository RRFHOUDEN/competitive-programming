bolock = []
for i in range(1, 300):
    bolock.append(i * (i + 1) * (i + 2) // 6)

i = len(bolock) - 1
n = int(input())
cnt = 0
while i >= 0:
    if n >= bolock[i]:
        cnt += 1
        n -= bolock[i]
        print(i)
    i-= 1

print(bolock[:40])
print(cnt)