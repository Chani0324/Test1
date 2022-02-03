# class unit :
#     def __init__(self) :
#         print("unit 생성자")

# class flyable:
#     def __init__(self):
#         print("flyable 생성자")

# class flyableunit(unit, flyable):   
#     def __init__(self):
#         super().__init__()

# dropship = flyableunit()    # class에 상속 받는 순서에 따라 super 상속이 다름.






# ############# text로 스타크 만들어보기
# class unit :
#     def __init__(self, name, hp, speed) :
#         self.name = name
#         self.hp = hp
#         self.speed = speed
#         print("{0} 유닛이 생성되었습니다.".format(name))

#     def move(self, location) :
#         print("[지상 유닛 이동]")
#         print("{0} : {1} 방향으로 이동합니다. [속도 {2}]".format(self.name, location, self.speed))

#     def dmged(self, dmg) :
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name, dmg))
#         self.hp -= dmg
#         print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
#         if self.hp <= 0 :
#             print("{0} : 파괴되었습니다.".format(self.name))


# class attackunit(unit) :
#     def __init__(self, name, hp, speed, dmg) :
#         unit.__init__(self, name, hp, speed)
#         self.dmg = dmg

#     def attack(self, location) :
#         print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(self.name, location, self.dmg))


# class flyunit : 
#     def __init__(self, flying_speed) :
#         self.flying_speed = flying_speed

#     def fly(self, name, location) :
#         print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.flying_speed))

# class flyattackunit(attackunit, flyunit) :
#     def __init__(self, name, hp, dmg, flying_speed) :
#         attackunit.__init__(self, name, hp, 0, dmg)    # 멤버 변수 초기화
#         flyunit.__init__(self, flying_speed)   # 멤버 변수 초기화

#     def move(self, location) :
#         print("[공중 유닛 이동]")
#         self.fly(self.name, location)


# class building(unit) :
#     def __init__(self, name, hp, location) :
#         super().__init__(name, hp, 0)  # self는 쓰지 않음.
#         self.location = location
        

# # 마린 만들기
# class marine(attackunit) :
#     def __init__(self) :
#         attackunit.__init__(self, "마린", 40, 1, 5)
    
#     # 스팀팩
#     def stimpack(self) :
#         if self.hp > 10 :
#             self.hp -= 10
#             print("{0} : 스팀팩을 사용합니다. (HP 10 감소)".format(self.name))
#         else :
#             print("{0} : 체력이 부족하여 스팀팩을 사용하지 않습니다.".format(self.name))


# # 탱크
# class tank(attackunit) :
#     # 시즈모드
#     seize_developed = False # 시즈모드 개발여부
    
#     def __init__(self) :
#         attackunit.__init__(self, "탱크", 150, 1, 35)
#         self.seize_mode = False

#     def set_seize_mode(self) :
#         if tank.seize_developed == False :
#             return

#         # 현재 시즈모드가 아닐 때 -> 시즈 모드
#         if self.seize_mode == False :
#             print("{0} : 시즈모드로 전환합니다.".format(self.name))
#             self.dmg *= 2
#             self.seize_mode = True
#         # 시즈모드 -> 해제
#         else : 
#             print("{0} : 시즈모드로 전환합니다.".format(self.name))
#             self.dmg /= 2
#             self.seize_mode == False


# # 레이스
# class wraith(flyattackunit) :
#     def __init__(self) :
#         flyattackunit.__init__(self, "레이스", 80, 20, 5)
#         self.clocked = False

#     def clocking(self) :
#         if self.clocked == True :
#             print("{0} : 클로킹 모드를 해제합니다.".format(self.name))
#             self.clocked = False
#         else :
#             print("{0} : 클로킹 모드를 설정합니다.".format(self.name))
#             self.clocked = True


# def game_start():
#     print("새로운 게임을 시작합니다.")

# def game_over():
#     print("Player : gg")
#     print("[Player] 님이 퇴장하셨습니다.")


# ##### 게임 진행
# from random import *

# game_start()

# m1 = marine()
# m2 = marine()
# m3 = marine()

# t1 = tank()
# t2 = tank()

# w1 = wraith()


# attack_units = []
# attack_units.append(m1)
# attack_units.append(m2)
# attack_units.append(m3)
# attack_units.append(t1)
# attack_units.append(t2)
# attack_units.append(w1)

# # 유닛 이동
# for unit in attack_units :
#     unit.move("1시")

# # 탱크 시즈모드 개발
# tank.seize_developed = True
# print("시즈모드 개발이 완료되었습니다.")

# # 공격 준비
# for unit in attack_units :
#     if isinstance(unit, marine) : # 만들어진 객체가 어떤 class의 instance인지 확인
#         unit.stimpack()
#     elif isinstance(unit, tank) :
#         unit.set_seize_mode()
#     elif isinstance(unit, wraith) :
#         unit.clocking()

# # 공격
# for unit in attack_units :
#     unit.attack("1시")

# # 피해
# for unit in attack_units :
#     unit.dmged(randint(5,21))


# # 게임 종료
# game_over()







############ Quiz
# class House : 
#     def __init__(self, location, house_type, deal_type, price, completion_year) :
#         self.location = location
#         self.house_type = house_type
#         self.deal_type = deal_type
#         self.price = price
#         self.completion_year = completion_year

#     def show_detail(self) :
#         print(self.location, self.house_type, self.deal_type, self.price, self.completion_year)


# House1 = House("강남", "아파트", "매매", "10억", "2010년")
# House2 = House("마포", "오피스텔", "전세", "5억", "2007년")
# House3 = House("송파", "빌라", "월세", "500/50", "2000년")


# total = []

# total.append(House1)
# total.append(House2)
# total.append(House3)


# print("총 {0} 대의 매물이 있습니다.".format(len(total)))
# for sell in total :
#     sell.show_detail()   
    

