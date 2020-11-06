## Variables & Dictionaries

article_list = []

user1 = {"아이디": "hong123", "비밀번호": "1234", "이름": "홍길동"}
user2 = {"아이디": "sony7", "비밀번호": "7777", "이름": "손흥민"}
user3 = {"아이디": "ryu99", "비밀번호": "9999", "이름": "류현진"}

user_list = [user1, user2, user3]

no = 4

## =========================================================

## Make a Function to convert the inputs into files

def inputToFile(fileName):
    with open(fileName, 'w') as f:
        for key, value in fileName.items():
            f.writelines('{} : {}\n'.format(key, value))

##==========================================================

## Make a Function to convert the files into Dictionary

def articleFileToDic(fileName):
    with open(fileName, 'r') as f:
        article = {}
        for line in f.readlines():
            line = line.replace(' ','')
            items = line.split(':')
            key = items[0]
            value = items[1].replace('\n', '')

            if key == '번호':
                value = int(value)

            article[key] = value
        return article

a1 = articleFileToDic('article1.txt')
a2 = articleFileToDic('article2.txt')
a3 = articleFileToDic('article3.txt')

article_list.append(a1)
article_list.append(a2)
article_list.append(a3)

# ==========================================================


def loginCheck(id, pw):
    a = 0
    for user in user_list:
        if user["아이디"] == id:
            if user["비밀번호"] == pw:
                print("{}님 반갑습니다!".format(user["이름"]))
                return True

            else:
                print("비밀번호를 틀렸습니다")
                return False

    if a == 0:
        print("없는 아이디입니다")
        return False


def printArticle():
    print("=========== 게시물 목록 ==============")
    for article in article_list:
        print("번호 : {}   제목 : {}".format(article["번호"], article["제목"]))
    print("=====================================")


def addArticle():
    global no
    title = input("제목을 입력해주세요")
    body = input("내용을 입력해주세요")
    article = {"번호": no, "제목": title, "내용": body, "작성자": login_id}
    article_list.append(article)
    no += 1


# Find the specified article from the list
def getArticleNum():
    num = int(input("게시물 번호를 입력해주세요 : "))
    target = None
    for article in article_list:
        if article["번호"] == num:
            target = article
            break

    return target


def updateArticle():
    target = getArticleNum()

    if target == None:
        print("없는 게시물입니다.")

    else:
        tle = input("수정 제목 : ")
        bdy = input("수정 내용 : ")
        target["제목"] = tle
        target["내용"] = bdy
        print("수정이 완료되었습니다.")


def deleteArticle():
    target = getArticleNum()

    if target == None:
        print("없는 게시물입니다.")

    else:
        article_list.remove(target)
        print("삭제가 완료되었습니다.")


def detailArticle():
    target = getArticleNum()

    if target == None:
        print("없는 게시물입니다.")

    else:
        print("=========  게시물 목록  ==========")
        print("번호 : {}".format(target["번호"]))
        print("제목 : {}".format(target["제목"]))
        print("내용 : {}".format(target["내용"]))
        print("작성자 : {}".format(target["작성자"]))
        print("----- 댓글 -----")
        print("=================================")


def printHelp():
    print("add : 게시물 추가")
    print("list : 게시물 조회")
    print("add : 게시물 추가")
    print("update : 게시물 수정")
    print("delete : 게시물 삭제")
    print("detail : 게시물 상세조회")


# ===========================================================

login_id = input("아이디를 입력해주세요 : ")
login_pw = input("비밀번호를 입력해주세요 : ")

loginResult = loginCheck(login_id, login_pw)

if loginResult:
    while True:
        cmd = input("명령어를 입력해 주세요.")
        if cmd == "exit":
            print("프로그램을 종료합니다.")
            break

        elif cmd == "help":
            printHelp()

        elif cmd == "list":
            printArticle()

        elif cmd == "add":
            addArticle()

        elif cmd == "update":
            updateArticle()

        elif cmd == "delete":
            deleteArticle()

        elif cmd == "detail":
            detailArticle()

# ===========================================================