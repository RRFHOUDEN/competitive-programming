# import queue
# a = queue.LifoQueue()
# b = queue.LifoQueue()
# c = queue.LifoQueue()
#
# for i in [a, b, c]:
#     i.put(1)
#     i.put(2)
#     i.put(3)
#
# def f():
#     if a.empty():
#         return
#     num = a.get()
#     c.put(num)
#     f()
#     num = c.get()
#     b.put(num)
#
# f()
# while not b.empty():
#     num = b.get()
#     print(num)

#
# L = 876
# S = 204
# cnt = 0
# while L != S:
#     cnt += 1
#     if L < S:
#         S -= L
#     else:
#         L -= S
# print(L, S, cnt)

def f(x, y):
    if y == 0:
        return x
    return f(y, x % y)
print(f(231, 15))