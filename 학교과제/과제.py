import requests
from bs4 import BeautifulSoup

url = 'https://section.blog.naver.com/BlogHome.naver?directoryNo=0&currentPage=1&groupId=0'

response = requests.get(url)

if response.status_code == 200: # 정상 연결시
    soup = BeautifulSoup(response.text, 'html.parser') # 수프 text 형태로 만들기
    post_view_area = soup.find(id='postViewArea') # 본문 내용만 담긴 css 코드 뽑아내기
    if post_view_area:  # postViewArea가 있는지 확인
        print(post_view_area.get_text().split('점심')[3].split('F3')[0]) # 점심메뉴 부분만 잘라내기
    else:
        print("본문 내용을 찾을 수 없습니다.")
else:
    print(response.status_code)
