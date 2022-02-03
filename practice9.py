################## 모듈(class나 함수 등을 담고 있는 파일).

# import theater_module
# theater_module.price(3)
# theater_module.price_morning(4)


# import theater_module as mv 
# mv.price(3)


# from theater_module import *
# price(3)


# from theater_module import price, price_morning
# price(5)
# price_soldier(3)


# from theater_module import price_soldier as price
# price(5)







################### 패키지 (모듈 집합)
# import travel.thailand
# trip_to = travel.thailand.ThialandPackage()
# trip_to.detail()

# from travel import vietnam
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()


# from travel import *  # __all__ 함수 필요
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()
# trip_to = thailand.ThialandPackage()
# trip_to.detail()







################## 패키지, 모듈 위치
# import inspect
# import random
# print(inspect.getfile(random))
# print(inspect.getfile(thailand))






################## pip로 패키지 설치
# from bs4 import BeautifulSoup
# soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
# print(soup.prettify())






########## 내장 함수
# input : 사용자 입력을 받는 함수
# dir : 어떤 객체를 넘겨줬을 때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시
# print(dir())
# import random
# print(dir())
# import pickle
# print(dir())

# print(dir(random))

# name = "Jim"
# print(dir(name))





############ 외장 함수
# glob : 경로 내의 폴더 / 파일 목록 조회 (윈도우 dir)
# import glob
# print(glob.glob("*.py")) # 확장자가 py인 모든 파일

# os : 운영체제에서 제공하는 기본 기능.
# import os
# print(os.getcwd())

# folder = "sample_dir"

# if os.path.exists(folder) :
#     print("이미 존재하는 폴더입니다.")
#     os.rmdir(folder)
#     print(folder, "폴더를 삭제하였습니다.")
# else :
#     os.makedirs(folder)
#     print(folder, "폴더를 생성하였습니다.")

# time : 시간 관련 함수
# import time
# print(time.localtime())
# print(time.strftime("%Y-%m-%d %H:%M:%S"))

# import datetime
# print("오늘 날짜는", datetime.date.today()) 

# today = datetime.date.today()
# td = datetime.timedelta(days=100)
# print("우리가 만난지 100일은", today + td)





########### Quiz
# import byme

# byme.sign()