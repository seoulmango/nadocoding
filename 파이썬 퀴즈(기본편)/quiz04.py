class word:
    def __init__(self, 신조어, 보기1, 보기2, 정답):
        self.신조어 = 신조어
        self.보기1 = 보기1
        self.보기2 = 보기2
        self.정답 = 정답
    
    def show_question(self):
        print("{}의 뜻은 무엇일까요?".format(self.신조어))
        print("1. {}\n 2. {}".format(self.보기1, self.보기2))
    
    def check_answer(self):
        guess = int(input(">>"))
        if guess == self.정답:
            print("정답!")
        else:
            print("땡!")

ice = word("얼죽아", "얼어죽어도아이스","얼면죽는다아앗", 1)
ice.show_question()
ice.check_answer()
