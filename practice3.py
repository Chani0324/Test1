################## if
# weather = input("오늘 날씨는 어때요? ")
# if weather == "비" or weather == "눈":
#     print("우산을 챙기세요")
# elif weather == "미세먼지" :
#     print("마스크를 챙기세요")
# else : 
#     print("준비물 필요 없어요")

# temp = int(input("기온은 어때요?"))
# if 30 <= temp:
#     print("너무 더워요. 나가지 마세요")
# elif 10 <= temp and temp < 30 :
#     print("괜챃은 날씨에요")
# elif 0 <= temp < 10:
#     print("외투를 챙기세요")
# else :
#     print("너무 추워요. 나가지 마세요")




############### for 몇번 시행하는지 지정된 상태에서 반복 실행
# print("대기번호 : 1")
# print("대기번호 : 2")
# print("대기번호 : 3")

# for waiting_no in range(1, 5):
#     print("대기번호 : {0}".format(waiting_no))

# starbucks = ["아이언맨", "토르", "아이엠 그루트"]
# for customer in starbucks :
#     print("{0}, 커피가 준비되었습니다. ".format(customer) )




#################### while 보통 지속적 반복으로 특정한 값이 나올 떄까지 진행할 때 쓰임.
# customer = "토르"
# index = 5
# while index >= 1:
#     print("{0}, 커피가 준비되었습니다. {1} 번 남았어요.".format(customer, index))
#     index -= 1
#     if index == 0:
#         print("커피는 폐기처분되었습니다.")

# customer = "아이언맨"
# index = 1
# while True:
#     print("{0}, 커피가 준비되었습니다. 호출 {1} 회".format(customer, index))
#     index += 1

# customer = "토르"
# person = "Unknown"
# while person != customer :
#     person = input("이름이 어떻게 되세요?")
#     print("{0}, 커피가 준비되었습니다.".format(customer))




################### continue와 break
# absent = [2, 5] # 결석
# no_book = [7]
# for student in range(1, 11) :
#     if student in absent:
#         continue  # 해당 조건이면 건너뛰고 다음 조건 실행
#     elif student in no_book :
#         print("오늘 수업 여기까지. {0}는 교무실로 따라와".format(student))
#         break # 해당 조건 만족 시 탈출
#     print("{0}, 책을 읽어봐".format(student))


# customer = "토르"
# while True :
#     person = input("이름이 어떻게 되세요?")
#     if person != customer :
#         continue
#     elif person == customer :
#         print("{0}, 커피가 준비되었습니다.".format(customer))
#         break




################# 한줄 for
# 출석 번호 1 2 3 4, 앞에 100을 붙이기로 함. ex)101, 102, ...
# students = [1,2,3,4,5]
# students = [i+100 for i in students]
# print(students)

# 학생 이름을 길이로 변환
# students = ["Iron man", "Thor", "I am groot"]
# students = [len(u) for u in students]
# print(students)




########################### Quiz
# from random import *
# # 승객 수 50   
# reqtime = list(range(5,16)) # 지정 시간 5~15분
# realcus = 0 # 실제 탑승 승객

# for customer in range(1,51) :
#     time = randint(5,50) # 시간 5~50분 랜덤
#     if time in reqtime :
#         print("[O] {0}번째 손님 (소요시간 : {1}분)".format(customer,time))
#         realcus += 1
#     else :
#         print("[X] {0}번째 손님 (소요시간 : {1}분)".format(customer,time))

# print("총 탑승 승객 :", realcus,"명")



