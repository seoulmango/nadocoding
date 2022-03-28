import requests

res = requests.get("http://google.com")
# res = requests.get("http://nadocoing.tistory.com")

# 올바르게 가져오면 문제 없고, 아니면 에러를 낸다
res.raise_for_status()

# print("응답코드 :",res.status_code) #200이면 정상

# if res.status_code == requests.codes.ok: #후에 있는게 200이랑 똑같은 것
#     print("정상입니다")
# else:
#     print("문제가 생겼습니다. [에러코드 ", res.status_code, "]")

print(len(res.text))
print(res.text)

with open("mygoogle.html", "w", encoding="utf8") as f:
    f.write(res.text)