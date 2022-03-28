import requests
import re
from bs4 import BeautifulSoup

headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.83 Safari/537.36"}


search_until = int(int(input("몇 페이지까지 검색하시겠습니까?: "))+1)

for i in range(1, search_until):
    url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={}&rocketAll=false&searchIndexingToken=1=4&backgroundColor=".format(i)
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    items = soup.find_all("li", attrs={"class":re.compile("^search-product")})

    # print(items[0].find("div", attrs={"class":"name"}).get_text())

    for item in items:
        #광고 제품은 제외
        ad = item.find("span", attrs={"class":"ad-badge-text"})
        if ad:
            print("""
            -------광고 상품은 제외하겠습니다-------
            
            """)
            continue

        name = item.find("div", attrs={"class":"name"}).get_text()
        price = item.find("strong", attrs={"class":"price-value"}).get_text()
        rating = item.find("em", attrs={"class":"rating"})
        if rating:
            rating = rating.get_text()
        else:
            print("""

            -----평점 없는 상품 제외합니다-----

            """)
            continue
        print("상품: " + name)
        print("가격: " + price)
        print("평점: " + rating)
        print("")

