n = int(input())
st = []
for i in range(n):
    x, l = map(int, input().split())
    st.append([x + l, x - l])

st.sort()
cnt = 1
right = st[0][0]
for i in range(1, n):
    if right <= st[i][1]:
        right = st[i][0]
        cnt += 1

print(cnt)