s_string = ["abcef", "bcdef", "acf", "adef"]
s_list = []
cnt = 0
for i in s_string:
    s_list.append([])
    for j in range(len(i)):
        s_list[cnt].append(i[j])
    cnt += 1

print(s_list)

while True:
    for i in range(len(s_list)):
        