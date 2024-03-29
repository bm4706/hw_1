

class Member:  # 1번 Member class 정의

    def __init__(self, name, username, password):  # 2번 이름 아이디 비밀번호 속성 지정
        # print(f"회원이름은 {name}입니다.\n 회원 아이디는 {username}입니다.")
        self.name = name  # self.속성 = 변수?
        self.username = username
        self.password = password

    def __str__(self):  # 3번 회원정보를 알려주는 함수를 설정
        return (f"회원이름은 {self.name}입니다.\n회원 아이디는 {self.username}입니다.")
    # display 는 print를 해야하지만 __str은 return으로 해야 입력한 리스트들 다나옴


class Post():  # 1번 Post class 정의
    def __init__(self, title, content, author):  # 4번 제목 내용 작성자 속성 지정
        # super().__init__() # 상속으로author 과 name을 같게할려했으나 오류가 발생해서 상속안시키는걸로...
        self.title = title
        self.content = content
        self.author = author
        # self.author = self.username

    def __str__(self):
        return (f"제목 : {self.title}\n내용 : {self.content}\n작성자 : {self.author}")


# 5번 회원 인스턴스 생성
members = []
members.append(Member("철수", "cjftn", "tncjf"))
members.append(Member("짱구", "Wkdrn", "rnWKd"))
members.append(Member("맹구", "aodrn", "rnaod"))

# print(members)  # 실행시 object at 0x 어쩌구 나옴

# a = Member
for a in members:
    print(a.name)  # 인스턴스 작성한 회원 이름을 보여주는 식
    # a.display()  # display 실행시키는 식 # 근데display보다 __str__이 권장되는거같기도?
    print(a)


posts = []
# posts.append(Post("첫번쨰제목", "첫번째내용", "철수")) # input없으면 이런식으로 넣어야


# 6번 각각의 회원이 작성하는 코드

# 각각의 회원이 게시글 작성하는 코드
for a in members:
    for b in range(3):  # 3개이상을 해야하나 3개만 가능하도록 밖에 하지못함
        title = input(f"{a.name}의 제목:")
        content = input(f"{a.name}의 내용:")
        author = a.name
        posts.append(Post(title, content, author))
        # print(title)

for post in posts:  # 입력한 제목과 내용 그리고 회원 이름을 보여주는 코드
    print(post)


# 원하는 단어를 찾고싶을때 쓰는
find_post = input("검색하고 싶은 단어를 입력하세요.\n")

for d in posts:
    if find_post in d.content:
        print(d.title)
###
