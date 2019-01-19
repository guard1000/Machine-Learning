from bs4 import BeautifulSoup
import urllib.request as req

url ="http://info.finance.naver.com/marketindex/"
res = req.urlopen(url)

soup = BeautifulSoup(res, "html.parser")

#데이터 추출
price = soup.select_one("div.head_info > span.value").string
print("usd/krw =", price)
