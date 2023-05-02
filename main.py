import datetime
import string
import re

def create_membership():
		
    now = datetime.datetime.now()
    stnr_date = now.strftime('%Y%m%d')
    users = []
    
    while True:
        user = {}

        # id 제한
        while True:
            id=input("id:")
            if id.encode().isalpha():
                print("한글로 입력하세요.")
            else:
                if 2<=len(id)<=4:
                    user['id']=id
                    break
                else:
                    print("2~4글자만 입력하세요.")

        # 비밀번호 제한
        while True:
            pw=input("password:")
            if len(pw)<8:
                print("비밀번호는 8글자 이상으로 하세요.")
            else:
                count=0
                count+=pw.count('!')
                count+=pw.count('@')
                count+=pw.count('#')
                count+=pw.count('$')
                if count==0:
                    print("!,@,#,$ 중 최소한 하나는 사용하세요.")
                else:
                    if pw[0].isupper():
                        user['pw']=pw
                        break
                    else:
                        print("비밀번호의 시작은 영문 대문자로 시작하세요.")

        # email 제한
        while True:
            email=input("email:")
            f=re.compile('\w+[@]\w+.com')
            if f.match(email):
                user['email']=email
                break
            else:
                print("email형식을 지켜주세요. @앞에는 영문과 숫자만 가능합니다.")
        user['stnr_date']=stnr_date
        users.append(user)
        a=input("더 등록하시겠습니까?(Y or N) ")
        if a.upper()=="Y":
            continue
        elif a.upper()=="N":
            break
        else:
            print("Y,N으로만 답해주세요")
    
    return users



def load_to_txt(user_list):
    f = open('memberdb.txt', 'w', encoding='UTF-8')
    s_final=""
    for i in user_list:
        user_info=[]
        for k in i.values():
            user_info.append(k)
        s="{"+f"{user_info[0]},{user_info[1]},{user_info[2]},{user_info[3]}"+"}"+"\n"
        s_final=s_final+s
    f.write(s_final)
    f.close()
    
def run():
    user_list = create_membership()
    load_to_txt(user_list)


run()