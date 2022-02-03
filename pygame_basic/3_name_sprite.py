########### 프레임 설정
import pygame

pygame.init()   # 초기화. 반드시 필요


# 화면 크기 설정
screen_width = 480   # 가로 크기
screen_height = 640     # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))


# 화면 타이틀 설정
pygame.display.set_caption("Nado Game")     # game 이름


# 배경 이미지 불러오기
background = pygame.image.load("C:/Users/YSJ/Desktop/PythonWorkspace/pygame_basic/background.png")


# 스프라이트 불러오기 (캐릭터)
character = pygame.image.load("C:/Users/YSJ/Desktop/PythonWorkspace/pygame_basic/character.png")
character_size = character.get_rect().size  # 이미지의 크기 설정
character_width = character_size[0]     # 캐릭터 가로 크기
character_height = character_size[1]    # 캐릭터 세로 크기
character_x_pos = (screen_width - character_size[0]) / 2  # 화면 중앙에 캐릭터가 위치하도록
character_y_pos = screen_height - character_height   # 화면 가장 아래 부분에 캐릭터가 위치하도록




# 이벤트 루프 
running = True  # 게임이 진행 중인지 확인
while running :
    for event in pygame.event.get() :   # 프로그램이 계속 진행 중인지(마우스, 키보드 등 계속 움직이는지) 확인. 어떤 이벤트 발생했는지.
        if event.type == pygame.QUIT :  # 프로그램 창이 닫히는 이벤트 발생할 떄
            running = False
            

    # screen.fill((0,0,255))
    screen.blit(background, (0,0))  # 배경 그리기

    screen.blit(character, (character_x_pos, character_y_pos))

    pygame.display.update() # 게임 화면을 다시 그리기


# pygame 종료
pygame.quit()

