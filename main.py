import pygame
import sys

# 初期化
pygame.init()
WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

# プレイヤー情報
player_color = (0, 255, 0)
player_size = 50
player_x, player_y = WIDTH // 2, HEIGHT // 2
speed = 5

# メインループ
running = True
while running:
    screen.fill((0, 0, 0))  # 背景黒

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # キー操作
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= speed
    if keys[pygame.K_RIGHT]:
        player_x += speed
    if keys[pygame.K_UP]:
        player_y -= speed
    if keys[pygame.K_DOWN]:
        player_y += speed

    # プレイヤー描画
    pygame.draw.rect(screen, player_color, (player_x, player_y, player_size, player_size))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
