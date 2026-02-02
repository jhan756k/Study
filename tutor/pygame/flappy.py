import pygame
import sys
import random

pygame.init()

# =====================
# 화면 설정
# =====================
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")
clock = pygame.time.Clock()

# 색상
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 200, 0)
BG = (30, 30, 30)

font = pygame.font.SysFont(None, 50)

# =====================
# Bird 클래스
# =====================
class Bird:
    def __init__(self):
        self.rect = pygame.Rect(50, HEIGHT // 2, 30, 30)
        self.vel = 0
        self.gravity = 0.35
        self.jump_power = -6

    def jump(self):
        self.vel = self.jump_power

    def update(self):
        self.vel += self.gravity
        self.rect.y += self.vel

    def draw(self):
        pygame.draw.rect(screen, YELLOW, self.rect)

    def out_of_screen(self):
        return self.rect.top <= 0 or self.rect.bottom >= HEIGHT

    def reset(self):
        self.rect.x = 50
        self.rect.y = HEIGHT // 2
        self.vel = 0


# =====================
# Pipe 클래스
# =====================
PIPE_WIDTH = 60
PIPE_GAP = 150
PIPE_SPEED = 3

class Pipe:
    def __init__(self):
        center = random.randint(200, 450)

        self.top = pygame.Rect(
            WIDTH,
            center - PIPE_GAP - 400,
            PIPE_WIDTH,
            400
        )
        self.bottom = pygame.Rect(
            WIDTH,
            center,
            PIPE_WIDTH,
            400
        )

        self.scored = False

    def move(self):
        self.top.x -= PIPE_SPEED
        self.bottom.x -= PIPE_SPEED

    def draw(self):
        pygame.draw.rect(screen, GREEN, self.top)
        pygame.draw.rect(screen, GREEN, self.bottom)

    def collide(self, bird):
        return (
            bird.rect.colliderect(self.top)
            or bird.rect.colliderect(self.bottom)
        )

    def off_screen(self):
        return self.top.right < 0

    def check_score(self, bird):
        global score
        if not self.scored and self.top.right < bird.rect.left:
            score += 1
            self.scored = True


# =====================
# 게임 변수
# =====================
bird = Bird()
pipes = [Pipe()]
score = 0
game_active = True

# =====================
# 게임 루프
# =====================
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_active:
                bird.jump()

            if event.key == pygame.K_SPACE and not game_active:
                bird.reset()
                pipes = [Pipe()]
                score = 0
                game_active = True

    screen.fill(BG)

    if game_active:
        # 새 업데이트
        bird.update()
        bird.draw()

        # 파이프 생성
        if pipes[-1].top.x < 200:
            pipes.append(Pipe())

        # 파이프 처리
        for pipe in pipes[:]:
            pipe.move()
            pipe.draw()

            if pipe.collide(bird):
                game_active = False

            pipe.check_score(bird)

            if pipe.off_screen():
                pipes.remove(pipe)

        # 화면 충돌
        if bird.out_of_screen():
            game_active = False

        # 점수 표시
        score_text = font.render(str(score), True, WHITE)
        screen.blit(score_text, (WIDTH // 2 - 10, 20))

    else:
        over = font.render("Game Over", True, WHITE)
        restart = font.render("Press SPACE", True, WHITE)
        screen.blit(over, (WIDTH // 2 - 100, HEIGHT // 2 - 40))
        screen.blit(restart, (WIDTH // 2 - 120, HEIGHT // 2 + 10))

    pygame.display.update()
    clock.tick(60)
