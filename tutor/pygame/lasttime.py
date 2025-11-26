import pygame
import random

pygame.init()

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("pygame 테스트")

clock = pygame.time.Clock()
a = pygame.Rect(320, 220, 120, 120)

player_img = pygame.image.load("c.png")
player_img = pygame.transform.scale(player_img, (40, 40))
player = player_img.get_rect()
player.center = (320, 240)

speed = 5
player_color = (0, 255, 0)
touching_wall = False

enemy = pygame.Rect(random.randint(0, 600), -40, 40, 40)
enemy_speed = 4

running = True
while running:
    fps = clock.tick(60)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= speed
    if keys[pygame.K_RIGHT]:
        player.x += speed
    if keys[pygame.K_UP]:
        player.y -= speed
    if keys[pygame.K_DOWN]:
        player.y += speed

    if keys[pygame.K_LSHIFT]:
        speed = 10
    else:
        speed = 5

    if player.x >= 640 - player.width:
        player.x = 640 - player.width
        touching_wall = True

    if player.x <= 0:
        player.x = 0 
        touching_wall = True

    if player.y >= 480 - player.height:
        player.y = 480 - player.height
        touching_wall = True

    if  player.y <= 0:
        player.y = 0
        touching_wall = True

    if touching_wall:
        player_color = (255, 0, 0)
    else:
        player_color = (0, 255, 0)

    touching_wall = False

    enemy.y += enemy_speed
    if enemy.y > 480:
        enemy.y = -40
        enemy.x = random.randint(0, 600)

    if player.colliderect(enemy):
        print("game over!")
        running = False

    screen.fill((0, 0, 0))
    screen.blit(player_img, player)
    pygame.draw.rect(screen, (255, 0, 0), enemy)
    # screen.draw.rect(a, player_color)
    pygame.display.update()

pygame.quit()