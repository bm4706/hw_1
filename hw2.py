import random

RPS = "바위", "가위", "보"
a = random.choice(RPS)  # 가위바위보 무작위로 섞어서 하나 뽑기
print(a)

j = 0  # 시행횟수
q = 0  # 이긴횟수
w = 0  # 진횟수
e = 0  # 비긴횟수
continue_game = "y"
while continue_game == "y":
    i = input("가위 바위 보 중 하나를 선택하세요.\n 입력한 답:")  # 일단 시작 문구 넣어줘야함
    i = str(i)
    if i in ["가위", "바위", "보"]:
        if i == "가위":  # 경우의 수 따져야해서 3개로 나눔
            j += 1
            if a == "가위":
                print("비겼습니다. 다시 시작하세요")
                e += 1
                continue
            elif a == "바위":
                print("졌습니다.")
                w += 1
            elif a == "보":
                print("이겼습니다.")
                q += 1

        elif i == "바위":
            j += 1
            if a == "바위":
                print("비겼습니다. 다시 시작하세요")
                e += 1
                continue
            elif a == "보":
                print("졌습니다.")
                w += 1
            elif a == "가위":
                print("이겼습니다.")
                q += 1
        elif i == "보":
            j += 1
            if a == "보":
                print("비겼습니다.")
                e += 1
                continue
            elif a == "가위":
                print("졌습니다.")
                w += 1

            elif a == "바위":
                print("이겼습니다.")
                q += 1

    elif i not in ["가위", "바위", "보"]:
        print("잘못 입력하였습니다. 다시 입력해주세요.\n")
        continue
    continue_game = input("게임을 다시 하시겠습니까? [y or n]").lower()
    a = random.choice(RPS)  # 다시 게임을 시작할때 새로운 변수를 추가해야 하므로
else:
    print("게임을 종료합니다.")

print(str(j)+"회 진행하였습니다.")
print("승리수"+str(q) + "번\n" + "비긴횟수" + str(e)+"번\n"+"진횟수"+str(w)+"번")
