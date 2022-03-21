names = ["김모씨", "박모씨", "이모씨", "나모씨"]


for name in names:
    fhandle = open("%s.txt" %name, "w", encoding="utf8")
    fhandle.write(f"""
    안녕하세요 {name}님!

    저희는 {name}님과 같은 사업
    아이템에 관심이 있는 사람들입니다.
    혹시 관심이 생기시면 010-1234-5678로 연락 부탁드립니다.

    감사합니다!
    """)
    fhandle.close()

