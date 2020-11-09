## Variables & Dictionaries
# article_list = []
# user1 = {"아이디": "hong123", "비밀번호": "1234", "이름": "홍길동"}
# user2 = {"아이디": "sony7", "비밀번호": "7777", "이름": "손흥민"}
# user3 = {"아이디": "ryu99", "비밀번호": "9999", "이름": "류현진"}
# user_list = []
# no = 4
## =========================================================

## 게시물
from openpyxl import Workbook, load_workbook

# wb = Workbook()
# ws = wb.active
# ws.title = "Articles"
#
# ws["A1"] = "rowCount"
# ws["B1"] = 2
#
# ws["A2"] = "번호"
# ws["B2"] = "제목"
# ws["C2"] = "내용"
# ws["D2"] = "작성자"
#
# wb.save("ArticleWB.xlsx")

## Save posts to Xlsx
def writeArticleToXl(article):
    wb = load_workbook("ArticleWB.xlsx")
    ws = wb.active
    rowCnt = ws["B1"].value

    ws["A" + str(rowCnt + 1)] = article["번호"]
    ws["B" + str(rowCnt + 1)] = article["제목"]
    ws["C" + str(rowCnt + 1)] = article["내용"]
    ws["D" + str(rowCnt + 1)] = article["작성자"]

    ws["B1"] = rowCnt + 1
    wb.save("ArticleWB.xlsx")


## Read posts from Xlsx
def readArticleFrXl(num):
    wb = load_workbook("ArticleWB.xlsx")
    ws = wb.active

    for r in ws.rows:
        row_index = r[0].value
        if row_index == num:
            title = r[1].value
            body = r[2].value
            user = r[3].value

            article = {"번호": num, "제목": title, "내용": body, "작성자": user}
            return article


    return None


## Update posts in Xlsx
def updateArticleToXL(num, title, body):
    wb = load_workbook("ArticleWB.xlsx")
    ws = wb.active


    for r in ws.rows:
        row_index = r[0].value
        if row_index == num:
            r[1].value = title
            r[2].value = body
            wb.save("ArticleWB.xlsx")

    return None



## Delete posts from Xlsx
def deleteArticleFrXL(num):
    wb = load_workbook("ArticleWB.xlsx")
    ws = wb.active


    for r in ws.rows:
        row_index = r[0].value
        if row_index == num:
            ws.delete_rows(r)
            wb.save("ArticleWB.xlsx")


    return None



##==========================================================

## 작성자
# wb = load_workbook("ArticleWB.xlsx")
# ws2 = wb.create_sheet("Users")
# ws2.title = "Users"
#
# ws2["A1"] = "rowCount"
# ws2["B1"] = 2
#
# ws2["A2"] = "아이디"
# ws2["B2"] = "비밀번호"
# ws2["C2"] = "이름"
#
#
# wb.save("ArticleWB.xlsx")

## New user information
def newUserInfoToXl():
    id_info = input("등록할 아이디를 입력해 주세요 : ")
    pw_info = input("등록할 비밀번호를 입력해 주세요 : ")
    name_info = input("이름을 입력해 주세요 : ")

    new_user = {"아이디" : id_info, "비밀번호" : pw_info, "이름" : name_info}
    return new_user


## Save new user to Xlsx
def addUserToXL(new_user):
    wb = load_workbook("ArticleWB.xlsx")
    ws2 = wb.active
    rowCnt = ws2["B1"].value

    ws2["A" + str(rowCnt + 1)] = new_user["아이디"]
    ws2["B" + str(rowCnt + 1)] = new_user["비밀번호"]
    ws2["C" + str(rowCnt + 1)] = new_user["이름"]

    ws2["B1"] = rowCnt + 1
    wb.save("ArticleWB.xlsx")


## Read user from Xlsx
def readUserFrXlsx(id, pw):
    wb = load_workbook("ArticleWB.xlsx")
    ws2 = wb.active


    for r in ws2.rows:
        row_id = r[0].value
        if row_id == id:
            row_pw = r[1].value
            row_name = r[2].value
            user = {"아이디": row_id, "비밀번호": row_pw, "이름": row_name}
            return user

    return None


## Update user to Xlsx
def updateUserToXlsx(nm):
    wb = load_workbook("ArticleWB.xlsx")
    ws2 = wb.active


## Delete user from Xlsx
def deleteUserFrXlsx(nm):
    wb = load_workbook("ArticleWB.xlsx")
    ws2 = wb.active


# ==========================================================


def loginCheck(id, pw):
    user = readUserFrXlsx(id, pw)
    if user["아이디"] == id:
        if user["비밀번호"] == pw:
            print("{}님 반갑습니다!".format(user["이름"]))
            return True

        else:
            print("비밀번호를 틀렸습니다")
            return False

    else:
        print("없는 아이디입니다")
        return False


def printArticle():
    article = readArticleFrXl()
    print("=========== 게시물 목록 ==============")
    print("번호 : {} \n제목 : {}".format(article["번호"], article["제목"]))
    print("=====================================")


def addArticle():
    global no
    title = input("제목을 입력해주세요")
    body = input("내용을 입력해주세요")
    article = {"번호": no, "제목": title, "내용": body, "작성자": login_id}
    writeArticleToXl(article)
    no += 1


# Find the specified article from the list
def getArticleNum():
    num = int(input("게시물 번호를 입력해주세요 : "))
    target = readArticleFrXl(num)
    return target


def updateArticle():
    num = int(input("게시물 번호를 입력해주세요 : "))
    title = input("수정 제목 : ")
    body = input("수정 내용 : ")
    target = updateArticleToXL(num, title, body)

    if target is None:
        print("없는 게시물입니다.")

    else:
        print("수정이 완료되었습니다.")


def deleteArticle():
    num = int(input("게시물 번호를 입력해주세요 : "))
    target = deleteArticleFrXL(num)

    if target is None:
        print("없는 게시물입니다.")

    else:
        print("삭제가 완료되었습니다.")


def detailArticle():
    target = getArticleNum()

    if target is None:
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

        elif cmd == "add_user":
            user_info = newUserInfo()
            addUserToXL(user_info)

        elif cmd == "print_user":
            readUserFrXlsx()

        elif cmd == "update_user":
            nm = input("수정할 작성자의 이름을 입력해 주세요 : ")
            updateUserToXlsx(nm)

        elif cmd == "delete_user":
            nm = input("삭제할 작성자의 이름을 입력해 주세요 : ")
            deleteUserFrXlsx(nm)


# ===========================================================