#정규식. Regular expressions

import re
#차량 번호판은 네가지 문자. ex) abcd, book, desk
# ca?e
# care cafe case cave
# a~z까지 다 대입?

p = re.compile("ca.e")
# . (ca.e): 하나의 문자를 의미 > care, cafe, case | caffe (x)
# ^ (^de) : 문자열의 시작 > desk, destination | fade (x)
#  $ (se$) : 문자열의 끝 > case, base  | face (x)

# m = p.match("case")
# # m = p.match("caffe")
# # print(m.group()) #매치되지 않으면 에러가 발생
# if m:
#     print(m.group())
# else:
#     print("매칭되지 않음")

# 위의 식을 함수로 만들어보자
def print_match(m):
    if m:
        print("m.group(): ", m.group()) #일치하는 문자열 반환
        print("m.string: ", m.string) # 입력받은 문자열 반환
        print("m.start(): ", m.start()) # 일치하는 문자열의 시작 index
        print("m.end()", m.end()) #일치하는 문자열의 끝 index
        print("m.span()", m.span()) #일치하는 문자열의 시작 & 끝 index
        print("")
    else:
        print("매칭되지 않음")

# m = p.match("careless") #match: 주어진 문자열의 처음부터 일치하는지 확인
# print_match(m)

# m = p.search("good care") # search: 주어진 문자열 중에 일치하는 게 있는지 확인
# print_match(m)

lst = p.findall("good care cafe") # findall: 일치하는 모든 것을 리스트 형태로 변환
print(lst)

# 1. re.compile("원하는 형태")
# 2. m = p.match("비교할 문자열") : 주어진 문자열의 처음부터 일치하는지 확인
# 3. m = p.search("비교할 문자열") : 주어진 문자열 중에 일치하는 게 있는지 확인
# 4. lst = p.findall("비교할 문자열") : 일치하는 모든 것을 리스트 형태로 변환

# 원하는 형태: 정규식
# . (ca.e): 하나의 문자를 의미 > care, cafe, case | caffe (x)
# ^ (^de) : 문자열의 시작 > desk, destination | fade (x)
#  $ (se$) : 문자열의 끝 > case, base  | face (x)
