a, b = input().split()
a = int(a)
b_list = list(b.split("."))
b = int(b_list[0])*100
b += int(b_list[1])
print(a*b//100)