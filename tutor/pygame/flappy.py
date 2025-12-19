import pygame
import random

pygame.init()

WIDTH = 400
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("bird game")

clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BIRD_COLOR = (255, 255, 0)
PIPE_COLOR = (0, 200, 0)
BG_COLOR = (30, 30, 30)

bird = pygame.Rect(50, HEIGHT//2 - 15, 30, 30)
bird_speed = 0
gravity = 0.35
jump_strength = -6
game_active = True

pipe_width = 60
pipe_height = 400
pipe_gap = 150
pipe_speed = 3
pipes = []
score = 0
font = pygame.font.SysFont(None, 50)

def create_pipe():
    center = random.randint(200, 450)

    top_pipe = pygame.Rect(WIDTH, center - pipe_height - pipe_gap, pipe_width, pipe_height)
    bottom_pipe = pygame.Rect(WIDTH, center, pipe_width, pipe_height)

    top_pipe.scored = False
    bottom_pipe.scored = False
    return top_pipe, bottom_pipe

pipes.extend(create_pipe())
 
running = True
while running:
    fps = clock.tick(60)
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_active:
                bird_speed = jump_strength
            if event.key == pygame.K_SPACE and not game_active:
                bird.x = 50 
                bird.y = HEIGHT//2 - 15
                bird_speed = 0
                pipes.clear()
                pipes.extend(create_pipe())
                score = 0
                game_active = True
        

    screen.fill(BG_COLOR)

    if game_active:
        bird_speed += gravity
        bird.y += bird_speed
        pygame.draw.rect(screen, BIRD_COLOR, bird)
      
        if pipes[-1].x < 150:
            pipes.extend(create_pipe())

        for pipe in list(pipes):
            pipe.x -= pipe_speed
            pygame.draw.rect(screen,PIPE_COLOR,pipe)

            if pipe.x < -pipe_width:
                pipes.remove(pipe) 

        for pipe in pipes:
            if bird.colliderect(pipe):
                game_active = False

        if bird.y <= bird.height or bird.y >= HEIGHT:
            game_active = False
            
        score_text = font.render(str(score), True, WHITE)
        screen.blit(score_text, (WIDTH//2 - 10, 20))

        for pipe in pipes:
            if pipe.x + pipe_width < bird.x and not pipe.scored:
                score += 0.5
                pipe.scored = True
    else:
        game_over_text = font.render("GAME OVER", True, WHITE)
        restart_text = font.render("Press SPACE",True, WHITE)
        screen.blit(game_over_text, (WIDTH//2 - 100, HEIGHT//2 - 50))
        screen.blit(restart_text, (WIDTH//2 - 100, HEIGHT//2 + 10))

    pygame.display.update()
        