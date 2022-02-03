################# 함수
# def open_account():
#     print("새로운 계좌가 생성되었습니다.")

# open_account()




#################### 전달값과 반환값
# def deposit(balance, money) :
#     print("입금이 완료되었습니다. 잔액은 {0}원입니다.".format(balance + money))
#     return balance + money

# def withdraw(balance, money) :
#     if balance < money :
#         print("잔액이 부족합니다. 잔액은 {0}원입니다.".format(balance))
#         return balance
#     elif balance >= money :
#         print("출금이 완료되었습니다. 잔액은 {0}원입니다.".format(balance - money))
#         return balance - money

# def withdraw_night(balance, money) : 
#     commission = 100 # 수수료
#     return commission, balance-money-commission

# balance = 0 # 잔액
# balance = deposit(balance, 1000) 
# # balance = withdraw(balance, 500)
# commission, balance = withdraw_night(balance, 500)  # return값에 반환 값으로 2개가 온다면 변수도 순서에 맞춰 2개로.
# print("수수료 {0}원이며, 잔액은 {1}원입니다.".format(commission, balance))






######################## 기본값
# def profile(name, age, main_lang) :
#     print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}".format(name, age, main_lang))

# profile("유재석", 20, "파이썬")
# profile("김태호", 25, "자바")

# def profile(name, age=17, main_lang="파이썬") :
#     print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}".format(name, age, main_lang))

# profile("유재석")
# profile("김태호")





################# 키워드값
# def profile(name, age, main_lang) :
#     print(name, age, main_lang)

# profile(age=22, name="유재석", main_lang="파")





###############가변 인자
# def profile(name, age, *language) :   #  * 으로 매개변수 이용.
#     print("이름 :{0}\t나이 : {1}\t".format(name,age), end=" ")
#     for lang in language :
#         print(lang, end=" ")
#     print()

# profile("유재석", 20, "파이선", "자바", "C", "C++")




#############지역변수, 전역변수 
# gun = 10  

# def checkpoint(soldiers) :  # 경계근무 
#     gun = 20    # 지역 변수
#     gun = gun-soldiers  
#     print("[함수 내] 남은 총 : {0}".format(gun))

# print("전체 총 : {0}".format(gun))
# checkpoint(2)
# print("남은 총 : {0}".format(gun))


# def checkpoint(soldiers) :  # 경계근무 
#     global gun   # 전역변수 
#     gun = gun-soldiers  
#     print("[함수 내] 남은 총 : {0}".format(gun))

# print("전체 총 : {0}".format(gun))
# checkpoint(2)
# print("남은 총 : {0}".format(gun))


# def checkpoint_ret(gun, soldiers) :
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))
#     return gun

# print("전체 총 : {0}".format(gun))
# gun = checkpoint_ret(gun, 2)
# print("남은 총 : {0}".format(gun))






######### Quiz
## 표준 체중
## 남자 : 키 x 키 x 22
## 여자 : 키 x 키 x 21

## 조건 1 : 표준 체중은 별도의 함수 내에서 계산
##     * 함수명 : std_weight
##     * 전달값 : 키(height), 성별(gender)
## 조건 2 : 표준 체중은 소수점 둘째자리까지 표시


# def std_weight(height, gender) :
#     if gender == "남자" :
#         std_weight = round(height/100*height/100*22, 2)
#         print("키 {0}cm {1}의 표준 체중은 {2}kg입니다.".format(height, gender, std_weight))
#     elif gender == "여자" :
#         std_weight = round(height/100*height/100*21, 2)
#         print("키 {0}cm {1}의 표준 체중은 {2}kg입니다.".format(height, gender, std_weight))


# gender = input("성별을 입력하세요")
# height = int(input("키를 입력하세요"))

# std_weight(height, gender)