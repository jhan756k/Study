import pygame
import sys

pygame.init()

# 화면 크기 설정
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong Game")

clock = pygame.time.Clock()

# 색
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# 패들 설정
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 100

left_paddle = pygame.Rect(20, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
right_paddle = pygame.Rect(WIDTH - 30, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)

# 공 설정
ball = pygame.Rect(WIDTH//2 - 10, HEIGHT//2 - 10, 20, 20)
ball_speed_x = 5
ball_speed_y = 5

# 점수
score_left = 0
score_right = 0
font = pygame.font.SysFont(None, 60)

# 공 리셋 함수
def reset_ball():
    global ball_speed_x, ball_speed_y
    ball.center = (WIDTH//2, HEIGHT//2)
    ball_speed_x *= -1  # 방향 반전
    ball_speed_x = 5 * (1 if ball_speed_x > 0 else -1)
    ball_speed_y = 5


# --------------------------
#       게임 루프
# --------------------------
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 키 입력
    keys = pygame.key.get_pressed()

    # 왼쪽 패들 움직임
    if keys[pygame.K_w]:
        left_paddle.y -= 6
    if keys[pygame.K_s]:
        left_paddle.y += 6

    # 오른쪽 패들 움직임
    if keys[pygame.K_UP]:
        right_paddle.y -= 6
    if keys[pygame.K_DOWN]:
        right_paddle.y += 6

    # 패들 화면 밖으로 못 나가게 제한
    left_paddle.y = max(0, min(HEIGHT - PADDLE_HEIGHT, left_paddle.y))
    right_paddle.y = max(0, min(HEIGHT - PADDLE_HEIGHT, right_paddle.y))

    # 공 움직임
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    ball_speed_x *= 1.001
    ball_speed_y *= 1.001   

    # 위 아래 벽 충돌 → 반사
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed_y *= -1

    # 패들과 충돌 → 반사
    if ball.colliderect(left_paddle) or ball.colliderect(right_paddle):
        ball_speed_x *= -1

    # 점수 처리
    if ball.left <= 0:      # 오른쪽 점수
        score_right += 1
        reset_ball()

    if ball.right >= WIDTH: # 왼쪽 점수
        score_left += 1
        reset_ball()

    # 화면 그리기
    screen.fill(BLACK)

    pygame.draw.rect(screen, WHITE, left_paddle)
    pygame.draw.rect(screen, WHITE, right_paddle)
    pygame.draw.ellipse(screen, WHITE, ball)

    # 중앙 라인
    pygame.draw.aaline(screen, WHITE, (WIDTH//2, 0), (WIDTH//2, HEIGHT))

    # 점수 표시
    text = font.render(f"{score_left}   {score_right}", True, WHITE)
    screen.blit(text, (WIDTH//2 - 50, 20))

    pygame.display.flip()
    clock.tick(60)
