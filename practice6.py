# name = "마린"
# hp = 40
# dmg = 5

# print("{0} 유닛이 생성되었습니다.".format(name))
# print("체력 {0}, 공격력 {1}".format(hp,dmg))


# tank = "탱크"
# tank_hp = 150
# tank_dmg = 35

# print("{0} 유닛이 생성되었습니다.".format(tank))
# print("체력 {0}, 공격력 {1}".format(tank_hp, tank_dmg))


# def attack(name, location, dmg) :
#     print("{0} : {1} 방향으로 적군을 공격합니다. [공격력{2}]".format(name, location, dmg))


# attack(name, "1시", dmg)
# attack(tank, "1시", tank_dmg)




############ class
# class unit :
#     def __init__(self, name, hp, dmg) :
#         self.name = name
#         self.hp = hp
#         self.dmg = dmg
#         print("{0} 유닛이 생성되었습니다.".format(self.name))
#         print("체력 {0}, 공격력 {1}".format(self.hp, self.dmg))


# marine1 = unit("마린", 40, 5)
# marine2 = unit("마린", 40, 5)
# tank = unit("탱크", 150, 35)

############ 멤버 변수
# wraith1 = unit("레이스", 80, 5)
# print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.dmg))

# wraith2 = unit("레이스", 80, 5) 
# wraith2.clocking = True # 멤버 변수로 지정해서 해당 객체만 가짐

# if wraith2.clocking == True :
#     print("{0}는 현재 클로킹 상태입니다.".format(wraith2.name))





########### 메소드 
# class attackunit :
#     def __init__(self, name, hp, dmg) :
#        self.name = name
#        self.hp = hp
#        self.dmg = dmg

#     def attack(self, location) :
#         print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(self.name, location, self.dmg))

#     def dmged(self, dmg) :
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name, dmg))
#         self.hp -= dmg
#         print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
#         if self.hp <= 0 :
#             print("{0} : 파괴되었습니다.".format(self.name))


# firebat1 = attackunit("파이어뱃", 50, 16)
# firebat1.attack("5시")

# firebat1.dmged(25)
# firebat1.dmged(25)




############ 상속. class에 같은 변수가 설정되어 있으면 다음 함수를 만들 때 이어받아서 할 수 있음.
# class unit :
#     def __init__(self, name, hp) :
#         self.name = name
#         self.hp = hp


# class attackunit(unit) :
#     def __init__(self, name, hp, dmg) :
#         unit.__init__(self, name, hp)
#         self.dmg = dmg

#     def attack(self, location) :
#         print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(self.name, location, self.dmg))

#     def dmged(self, dmg) :
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name, dmg))
#         self.hp -= dmg
#         print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
#         if self.hp <= 0 :
#             print("{0} : 파괴되었습니다.".format(self.name))


# firebat1 = attackunit("파이어뱃", 50, 16)
# firebat1.attack("5시")

# firebat1.dmged(25)
# firebat1.dmged(25)





############# 다중 상속.
# class unit :
#     def __init__(self, name, hp) :
#         self.name = name
#         self.hp = hp


# class attackunit(unit) :
#     def __init__(self, name, hp, dmg) :
#         unit.__init__(self, name, hp)
#         self.dmg = dmg

#     def attack(self, location) :
#         print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(self.name, location, self.dmg))

#     def dmged(self, dmg) :
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name, dmg))
#         self.hp -= dmg
#         print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
#         if self.hp <= 0 :
#             print("{0} : 파괴되었습니다.".format(self.name))

# class flyunit : 
#     def __init__(self, flying_speed) :
#         self.flying_speed = flying_speed

#     def fly(self, name, location) :
#         print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.flying_speed))

# class flyattackunit(attackunit, flyunit) :
#     def __init__(self, name, hp, dmg, flying_speed) :
#         attackunit.__init__(self, name, hp, dmg)    # 멤버 변수 초기화
#         flyunit.__init__(self, flying_speed)    # 멤버 변수 초기화


# valkyrie1 = flyattackunit("발키리", 200, 6, 5)
# valkyrie1.fly(valkyrie1.name, "3시")





############ 메소드 오버라이딩
# class unit :
#     def __init__(self, name, hp, speed) :
#         self.name = name
#         self.hp = hp
#         self.speed = speed

#     def move(self, location) :
#         print("[지상 유닛 이동]")
#         print("{0} : {1} 방향으로 이동합니다. [속도 {2}]".format(self.name, location, self.speed))

# class attackunit(unit) :
#     def __init__(self, name, hp, speed, dmg) :
#         unit.__init__(self, name, hp, speed)
#         self.dmg = dmg

#     def attack(self, location) :
#         print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(self.name, location, self.dmg))

#     def dmged(self, dmg) :
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name, dmg))
#         self.hp -= dmg
#         print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
#         if self.hp <= 0 :
#             print("{0} : 파괴되었습니다.".format(self.name))

# class flyunit : 
#     def __init__(self, flying_speed) :
#         self.flying_speed = flying_speed

#     def fly(self, name, location) :
#         print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.flying_speed))

# class flyattackunit(attackunit, flyunit) :
#     def __init__(self, name, hp, dmg, flying_speed) :
#         attackunit.__init__(self, name, hp, 0, dmg)    # 멤버 변수 초기화. 0 : unit에 speed 값
#         flyunit.__init__(self, flying_speed)    # 멤버 변수 초기화

#     def move(self, location) :
#         print("[공중 유닛 이동]")
#         self.fly(self.name, location)


# valture = attackunit("벌쳐", 80, 10, 20)
# battlecruiser = flyattackunit("배틀크루져", 500, 25, 3)

# valture.move("11시")
# # battlecruiser.fly(battlecruiser.name, "9시")
# battlecruiser.move("9시")




############# pass
# class unit :
#     def __init__(self, name, hp, speed) :
#         self.name = name
#         self.hp = hp
#         self.speed = speed

#     def move(self, location) :
#         print("[지상 유닛 이동]")
#         print("{0} : {1} 방향으로 이동합니다. [속도 {2}]".format(self.name, location, self.speed))

# class attackunit(unit) :
#     def __init__(self, name, hp, speed, dmg) :
#         unit.__init__(self, name, hp, speed)
#         self.dmg = dmg

#     def attack(self, location) :
#         print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(self.name, location, self.dmg))

#     def dmged(self, dmg) :
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name, dmg))
#         self.hp -= dmg
#         print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
#         if self.hp <= 0 :
#             print("{0} : 파괴되었습니다.".format(self.name))

# class flyunit : 
#     def __init__(self, flying_speed) :
#         self.flying_speed = flying_speed

#     def fly(self, name, location) :
#         print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.flying_speed))

# class flyattackunit(attackunit, flyunit) :
#     def __init__(self, name, hp, dmg, flying_speed) :
#         attackunit.__init__(self, name, hp, 0, dmg)    # 멤버 변수 초기화. 0 : unit에 speed 값
#         flyunit.__init__(self, flying_speed)    # 멤버 변수 초기화

#     def move(self, location) :
#         print("[공중 유닛 이동]")
#         self.fly(self.name, location)


# class building(unit) :
#     def __init__(self, name, hp, location) :
#         pass    # 아무것도 안하고 일단 넘어감.


# supply_depot = building("서플라이 디폿", 500, "7시")


# def game_start():
#     print("새로운 게임을 시작합니다.") 

# def game_over():
#     pass

# game_start()
# game_over()







############### super
# class unit :
#     def __init__(self, name, hp, speed) :
#         self.name = name
#         self.hp = hp
#         self.speed = speed

#     def move(self, location) :
#         print("[지상 유닛 이동]")
#         print("{0} : {1} 방향으로 이동합니다. [속도 {2}]".format(self.name, location, self.speed))

# class attackunit(unit) :
#     def __init__(self, name, hp, speed, dmg) :
#         unit.__init__(self, name, hp, speed)
#         self.dmg = dmg

#     def attack(self, location) :
#         print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(self.name, location, self.dmg))

#     def dmged(self, dmg) :
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name, dmg))
#         self.hp -= dmg
#         print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
#         if self.hp <= 0 :
#             print("{0} : 파괴되었습니다.".format(self.name))

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
        

# import numpy as np

# A = np.array([[1, 2, 3], [4, 5, 6]])


# print(2*A)