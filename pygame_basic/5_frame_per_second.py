import pygame

pygame.init()   # 초기화. 반드시 필요


# 화면 크기 설정
screen_width = 480   # 가로 크기
screen_height = 640     # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))


# 화면 타이틀 설정
pygame.display.set_caption("Nado Game")     # game 이름


# FPS
clock = pygame.time.Clock()


# 배경 이미지 불러오기
background = pygame.image.load("C:/Users/YSJ/Desktop/PythonWorkspace/pygame_basic/background.png")


# 스프라이트 불러오기 (캐릭터)
character = pygame.image.load("C:/Users/YSJ/Desktop/PythonWorkspace/pygame_basic/character.png")
character_size = character.get_rect().size  # 이미지의 크기 설정
character_width = character_size[0]     # 캐릭터 가로 크기
character_height = character_size[1]    # 캐릭터 세로 크기
character_x_pos = (screen_width - character_size[0]) / 2  # 화면 중앙에 캐릭터가 위치하도록
character_y_pos = screen_height - character_height   # 화면 가장 아래 부분에 캐릭터가 위치하도록


# 이동할 좌표
to_x = 0
to_y = 0


# 이동 속도
character_speed = 0.3



# 이벤트 루프 
running = True  # 게임이 진행 중인지 확인
while running :
    dt = clock.tick(10)     # 게임 화면의 초당 프레임수를 설정
    print("fps :" + str(clock.get_fps()))

    for event in pygame.event.get() :   # 프로그램이 계속 진행 중인지(마우스, 키보드 등 계속 움직이는지) 확인. 어떤 이벤트 발생했는지.
        if event.type == pygame.QUIT :  # 프로그램 창이 닫히는 이벤트 발생할 떄
            running = False

        if event.type == pygame.KEYDOWN : # 키보드가 눌러졌는지 확인
            if event.key == pygame.K_LEFT :
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT :
                to_x += character_speed
            elif event.key == pygame.K_UP :
                to_y -= character_speed
            elif event.key == pygame.K_DOWN :
                to_y += character_speed

        if event.type == pygame.KEYUP :     # 방향키를 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT :
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN :
                to_y = 0
            
    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

    # 가로 경계값
    if character_x_pos < 0 :
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width :
        character_x_pos = screen_width - character_width

    # 세로 경계값
    if character_y_pos < 0 :
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height :
        character_y_pos = screen_height - character_height

    # screen.fill((0,0,255))
    screen.blit(background, (0,0))  # 배경 그리기

    screen.blit(character, (character_x_pos, character_y_pos))

    pygame.display.update() # 게임 화면을 다시 그리기


# pygame 종료
pygame.quit()

