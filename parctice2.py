############ 사전정의 "{}"
# cabinet = {3:"유재석", 100: "김태호"} # 변수 내의 Key에 지정된 사전 의미를 부여
# print(cabinet[3])
# print(cabinet)
# print(cabinet[4]) # 변수 안에 값이 없으면 오류
# print(cabinet.get(3))
# print(cabinet.get(5)) # 변수 안에 값이 없어 none으로 표시 후 다음 계산 진행
# print(cabinet.get(5, "사용 가능")) # 값이 없으면 none으로 표시 후 "사용 가능" 출력
# print("hi")
# print(3 in cabinet) # True 출력
# cabinet = {"A-3" : "유재석", "B-100" : "김태호"}
# print(cabinet["A-3"])
# print(cabinet["B-100"])

# # 새 손님
# print(cabinet)
# cabinet["A-3"] = "김종국"
# cabinet["C-20"] = "조세호" # 값 추가
# print(cabinet)

# # 간 손님
# del cabinet["A-3"]
# print(cabinet)

# # Key 들만 출력
# print(cabinet.keys())

# # value 들만 출력
# print(cabinet.values())

# # Key, value 쌍으로 출력
# print(cabinet.items())

# 값 clear
# cabinet.clear





################ 튜플(내용 변경이나 추가 불가능) 대신 리스트 [] 보다 속도가 빠름
# menu = ("돈까스", "치즈까스")
# print(menu[0])
# print(menu[1])

# name = "김종국"
# age = 20
# hobby = "코딩"
# print(name, age, hobby)

# name, age, hobby = ("김종국", 20, "코딩")
# print(name, age, hobby)





################ 집합 (중복 안됨, 순서 없음)
# my_set = {1,2,3,3,3}
# print(my_set)

# java = {"유재석", "김태호", "양세형"}
# python = set(["유재석", "박명수"])

# # 교집합
# print(java & python)
# print(java.intersection(python))

# # 합집함
# print(java | python)
# print(java.union(python))

# # 차집합
# print(java - python)
# print(java.difference(python))

# # 값 추가 빼기
# python.add("홍만")
# print(python)
# python.remove("유재석")
# print(python)





################자료 구조 변경
# menu = {"커피", "우유", "주스"}
# print(menu)
# print(menu, type(menu))

# menu = list(menu)
# print(menu, type(menu))

# menu = tuple(menu)
# print(menu, type(menu))




# ############## Quiz
# from random import *
# List = list(range(1,21))
# shuffle(List)
# A = sample(List,1)
# List.remove(A[0])
# B = sample(List,3)

# print("-- 당첨자 발표 -- \n치킨 당첨자 : ", A[0], "\n커피 당첨자 : ", B, "\n-- 축하합니다. --")


# ## Quiz 영상 풀이
# List = list(range(1,21))

# winners = sample(List,4)
# print(" -- 당첨자 발표 -- ")
# print("치킨 당첨자 : {0}".format(winners[0]))
# print("커피 당첨자 : {0}".format(winners[1:]))
# print(" -- 축하합니다 -- ")





