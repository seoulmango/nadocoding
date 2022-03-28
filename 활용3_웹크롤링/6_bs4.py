import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
# print(soup.title) #<title> tag와 같이 가져옴
# print(soup.title.get_text()) # <title> tag 없이 가져옴
# # print(soup.a) #soup 객체에서 첫번째로 발견되는 a element 출력
# print(soup.a.attrs) #a element의 속성 정보를 출력
# print(soup.a["href"]) #a element의 href 속성 값 정보 출력

print(soup.find("a", attrs={"class":"Nbtn_upload"}).get_text())
# a element 중에서 웹툰 올리기 클래스 버튼을 찾아줘
# a element 없이 찾을 수도 있음. div class를 찾아도 되고.

# print(soup.find("li", attrs={"class":"rank01"}))
# rank1 = soup.find("li", attrs={"class":"rank01"})

# print(rank1.a.get_text())
# print(rank1.next_sibling.next_sibling.get_text())

# rank2 = rank1.next_sibling.next_sibling
# rank3 = rank2.next_sibling.next_sibling
# rank2 = rank3.previous_sibling.previous_sibling
# print(rank1.parent)

# rank2 = rank1.find_next_sibling("li") #조건에 해당하는 next sibling만 찾는다.
# print(rank2.a.get_text())
# rank3 = rank2.find_next_sibling("li")
# print(rank3.a.get_text())
# rank2 = rank3.find_previous_sibling("li")
# print(rank2.a.get_text())

# print(rank1.find_next_siblings("li"))


webtoon = soup.find("a",text="외모지상주의-384화 일해회 (2계열사) [13]")
print(webtoon)