import pygame
import sys
import random

pygame.init()

# 화면 크기
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

clock = pygame.time.Clock()

# 색
WHITE = (255, 255, 255)
BIRD_COLOR = (255, 255, 0)
PIPE_COLOR = (0, 200, 0)
BG_COLOR = (30, 30, 30)

# 새 설정
bird = pygame.Rect(50, HEIGHT//2, 30, 30)
bird_movement = 0
gravity = 0.35

# 게임 상태
game_active = True

# 파이프 설정
pipe_width = 60
pipe_gap = 150
pipe_speed = 3
pipes = []

# 점수
score = 0
passed_pipes = set()  # 점수를 중복으로 주지 않기 위해

font = pygame.font.SysFont(None, 50)

# 파이프 생성 함수
def create_pipe():
    # 파이프의 가운데 높이
    center = random.randint(200, 450)

    top_pipe = pygame.Rect(WIDTH, center - pipe_gap - 400, pipe_width, 400)
    bottom_pipe = pygame.Rect(WIDTH, center, pipe_width, 400)
    return top_pipe, bottom_pipe

# 초기 파이프
pipes.extend(create_pipe())

# 게임 루프
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # 점프
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_active:
                bird_movement = -6

            # 게임 오버 → 재시작
            if event.key == pygame.K_SPACE and not game_active:
                bird.x = 50
                bird.y = HEIGHT//2
                bird_movement = 0
                pipes.clear()
                pipes.extend(create_pipe())
                score = 0
                passed_pipes.clear()
                game_active = True

    screen.fill(BG_COLOR)

    if game_active:
        # --- 새 움직임 ---
        bird_movement += gravity
        bird.y += bird_movement

        # --- 새 그리기 ---
        pygame.draw.rect(screen, BIRD_COLOR, bird)

        # --- 파이프 생성 ---
        if pipes[-1].x < 150:  # 마지막 파이프가 어느 정도 왼쪽으로 오면 새 파이프 생성
            pipes.extend(create_pipe())

        # --- 파이프 움직임 & 그리기 ---
        for pipe in list(pipes):
            pipe.x -= pipe_speed
            pygame.draw.rect(screen, PIPE_COLOR, pipe)

            # 화면 밖 제거
            if pipe.x < -100:
                pipes.remove(pipe)

        # --- 충돌 판정 ---
        for pipe in pipes:
            if bird.colliderect(pipe):
                game_active = False

        # 바닥이나 천장 충돌
        if bird.top <= 0 or bird.bottom >= HEIGHT:
            game_active = False

        # --- 점수 계산 ---
        for i in range(0, len(pipes), 2):  # 파이프는 2개씩이므로 2단위로 점검
            pipe_pair_x = pipes[i].centerx
            if pipe_pair_x < bird.centerx and i not in passed_pipes:
                score += 1
                passed_pipes.add(i)

        # 점수 표시
        score_text = font.render(str(score), True, WHITE)
        screen.blit(score_text, (WIDTH//2 - 10, 20))

    else:
        # Game Over 화면
        game_over_text = font.render("Game Over!", True, WHITE)
        restart_text = font.render("Press SPACE", True, WHITE)

        screen.blit(game_over_text, (WIDTH//2 - 100, HEIGHT//2 - 50))
        screen.blit(restart_text, (WIDTH//2 - 110, HEIGHT//2 + 10))

    pygame.display.update()
    clock.tick(60)
