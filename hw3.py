

class Member:  # 일단 클래스를 명명

    def __init__(self, name, username, password):
        # print(f"회원이름은 {name}입니다.\n 회원 아이디는 {username}입니다.")
        self.name = name  # self.속성 = 변수?
        self.username = username
        self.password = password

    def __str__(self):  # 회원정보를 알려주는 함수를 설정
        return (f"회원이름은 {self.name}입니다.\n회원 아이디는 {self.username}입니다.")
    # display 는 print를 해야하지만 __str은 return으로 해야 입력한 리스트들 다나옴


class Post():
    def __init__(self, title, content, author):
        # super().__init__() # 상속으로author 과 name을 같게할려했으나 오류가 발생해서 상속안시키는걸로...
        self.title = title
        self.content = content
        self.author = author
        # self.author = self.username

    def __str__(self):
        return (f"제목 : {self.title}\n내용 : {self.content}\n작성자 : {self.author}")


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

for a in members:
    for b in range(3):
        title = input(f"{a.name}의 제목:")
        content = input(f"{a.name}의 내용:")
        author = a.name
        posts.append(Post(title, content, author))
        # print(title)

for post in posts:
    print(post)
