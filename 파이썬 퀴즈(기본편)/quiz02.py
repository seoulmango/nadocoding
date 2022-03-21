from random import *

wordlist = ["macbook", "likelion", "wifi"]

word = choice(wordlist)

question = "ㅁ" * len(word)

while True:
    print(question)
    guess = input("input >>")
    if guess in word:
        print('정답!\n')
        idx=-1
        for alphabet in word:
            idx += 1
            if alphabet == guess:
                question = question[:idx]+alphabet+question[idx+1:]
    else:
        print("땡!\n")
    if question == word:
        print(word)
        print("You Win!")
        break