S = input()
good = 1
for i in range(len(S)):
    if i % 2 == 0:
        if S[i] == "R" or S[i] == "U" or S[i] == "D":
            # print(1)
            good = good
        else:
            good = 0
    else:
        if S[i] == "L" or S[i] == "U" or S[i] == "D":
            # print(2)
            good = good
        else:
            good = 0

if not good:
    print("No")
else:
    print("Yes")