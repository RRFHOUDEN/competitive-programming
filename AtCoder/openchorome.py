import webbrowser
import time
print(time.time())
cnt = 0
C = 0
while True:
    if 1560560400 - time.time() < 0.5:
        webbrowser.open("https://entrance.shiki.jp/ticket/top.do")
    cnt += 1
    C += 1
    thistime = time.time()
    if cnt > 20:
        while True:
            cnt = 0
            if time.time() - thistime < 10:
                break
    if C > 200:
        break

print(time.time())