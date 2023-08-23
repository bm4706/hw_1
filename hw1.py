# up & down 만들기

# 일단 랜덤한 숫자를 생성해야함

import random

# 1~100까지 무작위 수이므로
a = random.randint(1, 100)
print(a)  # 답을 나타내므로 임시로 주석처리

# a는 문자열 처리되므로 정수로 변환
numbers = int(a)


# 플레이어는 숫자를 입력해야함 거기서 큰지 작은지 정해야함

# i = int(input("1에서 100까지 수를 입력하세요:")) # 여기서 넣은값이 문자열 처리되나봄 그래서 int를 써서 정수값으로 변환
# if i > numbers:
#     print("up!")
# elif i < numbers:
#     print("down!!")
# else:
#     print("정답입니다.")
#     break

score = []
# 이제 반복문을 넣어보자
j = 0  # 시행 횟수
continue_game = "y"

while continue_game == "y":  # 값이 항상 참이어야하므로 true
    # 입력값을 넣어야하므로, while문밖에다가 넣으니 에러가뜨므로 안에 넣어줘야한다

    # j += 1  # 시행 횟수를 알기 위해
    try:
        i = input("1에서 100까지 수를 입력하세요:")
        i = int(i)
    except ValueError:
        print("문자를 집어넣으셨습니다. 다시 시도해주세요.")
        continue
    if i > 100 or i <= 0:  # 혹시나 100초과 0미만인 값을 넣은 경우
        print("잘못된 값을 입력하였습니다. 1부터 100까지의 값을 다시 입력해주세요")
        continue  # 처음으로 되돌리기 위한 설정
    else:
        j += 1  # 위에다 넣으면 100초과하거나 음수의값을 집어넣어도 시행한걸로 취급하므로
        if i > numbers:  # 조건문을 걸어서 up인지 down 인지 알려줘야함
            print("up!")
            continue
        elif i < numbers:
            print("down!!")
            continue
        elif i == numbers:
            print("정답입니다.")

    continue_game = input("게임을 다시 하시겠습니까? [y or n]").lower()
    a = random.randint(1, 100)
    numbers = int(a)
    score.append(int(j))  # 최고 시행횟수를 찾기위해 리스트 값을 append 해줌

else:
    print("총" + str(j) + "회 반복하였습니다.")  # int로 넣으면 왜 안되는지 궁금하기는 함


best_score = max(score)
print(score)
print(str(best_score) + "회가 최고 점수입니다.")

##
