####### print 함수
# print(5)
# print(-5)
# print(5*3)
# print('풍선')
# print("풍선"*9)



########## 참 / 거짓
# print(5>10)
# print(True)
# print(not True)
# print(not False)
# print(not (5>10))



########## 변수 사용. , 와 ++ 이용
# animal = "고양이"
# name = "연탄이"
# age = 4  
# hobby = "산책"
# is_adult = age >= 3

# print("우리집 " + animal + "의 이름은 " + name + "에요")
# print(name,"는 ",age, "살이고 " ,hobby, "을 좋아하죠")
# print(name,"는 어른일까요?" , is_adult)



########### 주석
# Ctrl + / 



########### Quiz
# station1 = "사당"
# station2 = "신도림"
# station3 = "인천공항"

# print(station1, "행 열차가 들어오고 있습니다.")
# print(station2, "행 열차가 들어오고 있습니다.")
# print(station3, "행 열차가 들어오고 있습니다.")



############ 연산자
# print(1+1)
# print(2**3) # 2^3
# print(5%3) # 5를 3으로 나눈 나머지
# print(5//3) # 5를 3으로 나눈 몫
# print(3 > 10//3)
# print(3 == 10//3)
# print(1 != 3)
# print(not(1 != 3))
# print((3>0) and (3<5)) # &
# print((3>0) or (3>5)) # |



############ 간단한 수식
# number = 2 + 3*4
# number = number + 2
# print(number)
# number += 2
# print(number)
# print(abs(-5)) # 절대값
# print(pow(4, 2)) # 4^2
# print(max(5, 12)) # 제일 큰값
# print(min(5, 12)) # 제일 작은값
# print(round(3.14)) # 반올림(0.5 초과)
# print(round(max(5, 10.51)))
# from math import *
# print(floor(4.99)) # 내림
# print(ceil(3.14)) # 올림
# print(sqrt(16)) # 제곱근



############ 랜덤 함수 - random, randrange, randint
from random import *
# print(random()) # 0.0 ~1.0 미만의 임의의 값 생성
# print(int(random()*10))
# print(int(random()*10))
# print(int(random()*10)+1)
# print(int(random()*10)+1)
# print(int(random()*10)+1)
# print(int(random()*10)+1)
# print(int(random()*10)+1)
# print(int(random()*10)+1)
# print(randrange(1, 46)) # 1~46 미만의 임의의 정수 값 생성
# print(randint(1,45)) # 1~45 이하의 임의의 정수 값 생성



############# Quiz. 스터디 모임 임의 날짜 정하기
# from random import *
# date = randint(4, 28)
# print("오프라인 스터디 모임 날짜는 매월", date,"일로 선정되었습니다.")



################ 문자열 출력
# sentence = '나는 소년입니다.'
# print(sentence)
# sentence3 = """
# 나는 소년이고,
# 학생입니다.
# """
# print(sentence3)



############### 슬라이싱
# jumin = "920122-1234567"
# print("성별 : ", jumin[7]) # 맨앞자리는 0번쨰로 취급
# print("태어난 년도 : ", jumin[0:2]) # 0번째부터 2번째 직전까지의 값 출력
# print("태어난 월 : ", jumin[2:4])
# print("태어난 일 : ", jumin[4:6])
# print("생년월일 : ", jumin[:6])
# print("뒤 7자리 : ", jumin[7:])
# print("뒤 7자리 : ", jumin[-7:]) # 맨 뒤는 -1번째로 취급



############### 문자열 처리 함수
# python = "Python is Amazing"
# print(python.lower()) # 소문자 출력
# print(python.upper()) # 대문자출력
# print(python[0].isupper()) # 첫글자 대문자인지
# print(len(python)) # 변수의 총 길이 출력
# print(python.replace("Python", "Java")) # 변수에서 전자를 찾아 후자로 바꿈

# index = python.index("n") # 변수에서 어느 위치에 있는지
# print(index)
# index = python.index("n", index+1) # 그 다음번째 n을 찾음
# print(index)

# print(python.find("n"))
# print(python.find("Java")) # 없으면 -1로 뜸
# # print(python.index("Java")) # 없으면 오류 뜸
# print(python.count("n")) # 변수에서 n이 몇번 나오는지



################## 문자열 포맷
# 방법 1
# print("나는 %d살입니다." % 20) # %d위치에 20을 넣음. 정수만 가능
# print("나는 %s을 좋아해요." %"파이썬") # %s위치에 문자열을 넣음. 숫자도 가능.
# print("나는 %c로 시작해요." % "A") # %c위치에 문자를 넣음.

# print("나는 %s색과 %s색을 좋아해요." %("파란", "빨간")) # 순서에 맞춰서 문자 넣기 가능
# print("나는 {}색과 {}색을 좋아해요.".format("파란", "빨간"))
# print("나는 {0}색과 {1}색을 좋아해요.".format("파란", "빨간"))
# print("나는 {1}색과 {0}색을 좋아해요.".format("파란", "빨간")) # {}숫자에 맞춘 순서에 따라 입력 가능
# print("나는 {age}살이며, {color}색을 좋아해요".format(age=20, color="빨간")) # format에서 들어간 변수에 따라 입력 가능. 순서 상관 없음.

# age = 20
# color = "빨간"
# print(f"나는 {age}살이며, {color}색을 좋아해요") # f 함수 : 변수로 지정된 값을 바로 입력함...?



################# 탈출문자
# print("백문이 불여일견 \n백견이 불여일타") # 줄을 바꿔서 진행
# print("저는 '신'입니다.")
# print("저는 \"신\"입니다") # \ 를 사용해 문장 내에서 "", '' 사용 가능
# print("C:\\Users\\YSJ\\Desktop\\PythonWorkspace") # \+\



# ################## Quiz 직접 풀어본것
# ads = "https://tales.nexon.com/Home/Main"
# A = ads.find(".")
# A = A+1     # . 다음부터 시작

# B = ads.find(".")
# B = ads.find(".", B+1)

# C = ads[A:B]    # 첫번쨰 . 다음부터 . 직전까지
# D = C[:3]   # 중간 글자 중 첫 세글자.
# E = len(C)  # 중간 글자 길이
# F = C.count("e") # 중간 글자에서 e 가 몇번 나오는지

# print(f"{ads}의 생성된 비밀번호 : {D}{E}{F}!")

# #########

# ## Quiz 영상에서의 풀이
# url = "http://naver.com"
# my_str = url.replace("http://", "")
# my_str = my_str[:my_str.find(".")]
# passward = my_str[:3]+str(len(my_str))+str(my_str.count("e"))+"!"
# print("{0}의 생성된 비밀번호는 {1}입니다.".format(url, passward))



######################## 리스트 []
# A = 10
# B = 20
# C = 30
# K = [A, B, C]
# print(K)

# print(K.index(20))
# K.append(40)    # 리스트 끝에 추가
# print(K)

# K.insert(1, 81)     # 리스트 어디에 81이라는 숫자를 넣을건지
# print(K)

# K.pop()     # 리스트 끝에서 하나씩 뺌
# print(K)

# K.append(20)
# print(K.count(20))

# K.sort()    # 작은 순서대로 재배열
# print(K)

# K.reverse() # 큰 순서대로 배열
# print(K)

# K.clear()   # 리스트를 비움
# print(K)

# H = [5,2,1]
# K.extend(H)     # 하나의 리스트로 합침
# print(K)


