import queue
def solved(n):
    if n <= 9:
        return n
    nums = queue.Queue()
    for i in range(1, 10):
        nums.put(i)
    cnt = 9
    for i in range(cnt, n):
        i_num = nums.get()
        ini_num = i_num % 10
        for j in range(max(0, ini_num - 1), min(10, ini_num + 2)):
            nums.put(i_num * 10 + j)
            cnt += 1
            if cnt == n:
                return i_num * 10 + j
k = int(input())
num = queue.Queue()
print(solved(k))