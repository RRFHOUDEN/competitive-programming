sosu = [1 for i in range(10 ** 5 + 1)]

for i in range(2, len(sosu)):
    if sosu[i] == 1:
        j = i * 2
        #print(i, j)
        while j <= 10 ** 5:
            sosu[j] = 0
            j += i

print(sum(sosu))
u = 0
import time
now = time.time()
for i in range(200 * 10 ** 5):
    u += 3
print(time.time() - now)