import subprocess
# rakutenURL = ""
# for i in range(20):
#     subprocess.Popen([r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe', rakutenURL])

import webbrowser
url = "https://rt.tstar.jp/cart/performances/agreement/141900?_ga=2.131337871.1269239286.1580610601-1376554282.1525063549"
browser = webbrowser.get('"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" %s')
for i in range(100):
    browser.open(url)
# url = "https://rt.tstar.jp/cart/performances/agreement/141901?_ga=2.155264443.1269239286.1580610601-1376554282.1525063549"
# for i in range(50):
#     browser.open(url)
# https://ticket.rakuten.co.jp/music/jpop/RTZPAHC/