import pygame
SCREEN_WIDTH = 800 #가로
SCREEN_HEIGHT = 600 #세로

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

pygame.init()

pygame.display.set_caption("pygame")

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

clock = pygame.time.Clock()

done = False

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    # 게임 로직 구간
    # 화면 삭제 구간
    # 스크린 채우기
    screen.fill(WHITE)
    # 화면 그리기
    # 화면 업데이트
    pygame.display.flip()
    # 초당 60프레임으로 업데이트
    clock.tick(60)
pygame.quit()