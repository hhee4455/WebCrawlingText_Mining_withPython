import os
import sys
import requests
import urllib.request
import urllib.parse

# 네이버 개발자 센터에서 발급받은 클라이언트 ID와 클라이언트 시크릿을 입력하세요.
client_id = "TgsTrQ04l8ydlXpRwzDc"
client_secret = "FCWimzWgzq"

# 검색할 단어를 URL 인코딩합니다.
encText = urllib.parse.quote("파이썬")

# API 요청 URL 설정
url = "https://openapi.naver.com/v1/search/blog?query=" + encText

# API 요청에 필요한 헤더 설정
headers = {
    "X-Naver-Client-Id": client_id,
    "X-Naver-Client-Secret": client_secret
}

# API 요청 보내기
response = requests.get(url, headers=headers, verify=False)

# 응답 코드 확인
if response.status_code == 200:
    # 응답 데이터를 UTF-8 형식으로 디코딩하여 출력
    print(response.text)
else:
    # 에러 코드 출력
    print("Error Code:", response.status_code)
