############# 표준 출력
# import sys
# print("Python", "Java", sep=",", end="?")
# print("뭐가 더 재밌을까?")

# print("Python", "Java", file=sys.stdout)    # 표준 출력으로 문장이 찍힘.
# print("Python", "Java", file=sys.stderr)    # 표준 err로 문장이 찍힘.

# score = {"수학":0, "영어":50, "코딩":100}
# for subject, score in score.items() :
#     print(subject.ljust(8), str(score).rjust(4), sep=":")    # 오른쪽 정렬(칸), 왼쪽 정렬(칸).

# # 은행 대기 순번표
# for num in range(1,21) :
#     print("대기번호 : " + str(num).zfill(3))

# answer = input("아무 값이나 입력하세요 : ")
# print(type(answer))
# print("입력하신 값은 " + str(answer) + "입니다.")





############# 다양한 출력 포멧
# # 빈 자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
# print("{0: >10}".format(500))
# # 양수일 떈 +로 표시, 음수일 땐 -로 표시
# print("{0: >+10}".format(500))
# print("{0: >+10}".format(-500))
# # 왼쪽 정렬하고, 빈칸으로 _로 채움
# print("{0:_<+10}".format(500))
# # 3자리 마다 콤마를 찍어주기
# print("{0:,}".format(100000000000))
# # 3자리마다 콤마를 찍어주기, +-부포를 붙이기
# print("{0:+,}".format(100000000000))
# # 3자리마다 콤마를 찍어주기, 부호도 붙이고, 자리수 확보하기
# # 빈자리는 ^로 채우기
# print("{0:^<+30,}".format(100000000000))
# # 소수점 출력
# print("{0:f}".format(5/3))
# # 소수점 특정 자리수까지 표시
# print("{0:.2f}".format(5/3))






############ 파일 입출력
# score_file = open("score.txt", "w", encoding="utf8")  # "w"는 write의 의미
# print("수학 : 0", file=score_file)
# print("영어 : 50", file=score_file)
# score_file.close()

# score_file = open("score.txt", "a", encoding="utf8")     # "a"는 append의 의미
# score_file.write("과학 : 80")
# score_file.write("\n코딩 : 100")
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.read())
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.readline()) # 줄별로 읽기. 한줄 읽고 커서는 다음 줄로 이동
# print(score_file.readline())
# print(score_file.readline())
# print(score_file.readline())
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# while True :
#     line = score_file.readline()
#     if not line : 
#         break
#     print(line)

# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# lines = score_file.readlines()
# for line in lines :
#     print(line, end="")

# score_file.close()






############# pickle : 텍스트 이외의 자료형을 파일로 저장하기 위해 사용. ex)리스트형이나 클래스 등등.
# import pickle
# profile_file = open("profile.pickle", "wb") # "wb" 바이너리 타입을 write
# profile = {"이름":"박명수", "나이":30, "취미":["축구", "골프", "코딩"]}
# print(profile)
# pickle.dump(profile, profile_file)  # profile에 있는 정보를 file에 저장
# profile_file.close()


# profile_file = open("profile.pickle", "rb")
# profile = pickle.load(profile_file) # file에 있는 정보를 profile에 불러오기
# print(profile)
# profile_file.close()






######### with
# import pickle

# with open("profile.pickle", "rb") as profile_file :     # profile.pickle을 열어서 profile_file이라는 변수로 저장해둠.
#     print(pickle.load(profile_file))


# with open("study.txt", "w", encoding="utf8") as study_file :
#     study_file.write("파이썬 공부중")

# with open("study.txt", "r", encoding="utf8") as study_file :
#     print(study_file.read())





######## Quiz
# import pickle

# for workreport in range(1,51) : 
#     with open("{0}주차.txt".format(workreport), "w", encoding="utf8") as report_file :
#         report_file.write("-{0} 주차 주간 보고- \n부서 : \n이름 : \n업무 요약 : ".format(workreport))

