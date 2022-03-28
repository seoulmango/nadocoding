import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/list?titleId=748105&weekday=sun"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

#cartoons = soup.find_all("td", attrs={"class":"title"})
# title = cartoons[0].a.get_text()
# link = "https://comic.naver.com"+cartoons[0].a["href"]
# print(title)
# print(link)

#만화 제목과 링크 가져오기
# for cartoon in cartoons:
#     title = cartoon.a.get_text()
#     link = "https://comic.naver.com"+cartoon.a["href"]
#     print(title)
#     print(link)
#     print("")

#만화 별점 가져와서 평균 구하기

cartoons = soup.find_all("div", attrs={"class":"rating_type"})
total_rate = 0
for cartoon in cartoons:
    rate = cartoon.find("strong").get_text()
    print(rate)
    total_rate += float(rate)

print("Total score:", total_rate)
print("Average score:", total_rate/len(cartoons))