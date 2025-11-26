import pygame
import random

pygame.init()

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("pygame 3일차")

clock = pygame.time.Clock()

# 플레이어 설정
player = pygame.Rect(300, 400, 50, 50)
speed = 5

# 적 설정
enemy = pygame.Rect(random.randint(0, 600), -40, 40, 40)
enemy_speed = 4

running = True
while running:
    dt = clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 이동
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= speed
    if keys[pygame.K_RIGHT]:
        player.x += speed
    if keys[pygame.K_UP]:
        player.y -= speed
    if keys[pygame.K_DOWN]:
        player.y += speed

    # 경계 처리
    if player.x < 0:
        player.x = 0
    if player.x > 640 - player.width:
        player.x = 640 - player.width
    if player.y < 0:
        player.y = 0
    if player.y > 480 - player.height:
        player.y = 480 - player.height

    # 적 이동
    enemy.y += enemy_speed
    if enemy.y > 480:
        enemy.y = -40
        enemy.x = random.randint(0, 600)

    # 충돌 판정
    if player.colliderect(enemy):
        print("게임 오버!")
        running = False

    # 화면 그리기
    screen.fill((30, 30, 30))
    pygame.draw.rect(screen, (0, 255, 0), player)
    pygame.draw.rect(screen, (255, 0, 0), enemy)

    pygame.display.update()

pygame.quit()
