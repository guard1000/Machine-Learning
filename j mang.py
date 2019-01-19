#로그인 위한 모듈
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

#아이디와 비밀번호 지정
USER = "guard1000"
PASS = "1q2w3e4r!"

#세션 시작
session = requests.session()

#로그인 하자
login_info = {
    "retPage": "http://www.icampus.ac.kr/back/login/loginAction.do?method=checkLoginAuth&aspcd=002&rtncd=100",
    "method": "loginHide",
    "language": "en",
    "loginId": USER, #아이디 지정
    "userPasswd": PASS #PW지정
}
url_login = "https://admin.skku.edu/co/COCOUsrLoginAction.do"
res = session.post(url_login, data=login_info)
res.raise_for_status() #오류 발생하면 예외 발생

#마이페이지에 접근
url_main = "http://www.icampus.ac.kr/back/mypage/MemoAction.do?method=detailReceive&pBbsCode=3149955&pCurrentPage=1&pURL=listReceive&_TOK=1530722810452"
res = session.get(url_main)
res.raise_for_status()

#페이지 정보 가져오기
soup = BeautifulSoup(res.text, "html.parser")
mileage = soup.select_one(".보낸사람 b").get_text() #이부분 문제있,
print("마일리지: "+ mileage)
