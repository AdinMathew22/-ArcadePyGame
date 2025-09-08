import pygame
import random

# ----------------- Initialization -----------------
pygame.init()
WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Two Player Infinite Scroller")
clock = pygame.time.Clock()

# ----------------- Player Setup -----------------
player_img = pygame.image.load("player.png").convert_alpha()
player_img = pygame.transform.scale(player_img, (40, 50))

# Player 1 (arrows)
player1 = player_img.get_rect(topleft=(150, 300))
vel_y1 = 0
speed_boost1 = 1
wings1 = False
wings_timer1 = 0

# Player 2 (WASD)
player2 = player_img.get_rect(topleft=(300, 300))
vel_y2 = 0
speed_boost2 = 1
wings2 = False
wings_timer2 = 0

gravity = 0.5
jump_speed = -10

# ----------------- Ground Setup -----------------
ground_height = 50
ground_y = HEIGHT - ground_height
ground_speed = 5
ground_block_width = 200
ground_rects = [pygame.Rect(x, ground_y, ground_block_width, ground_height)
                for x in range(0, WIDTH + ground_block_width, ground_block_width)]

# ----------------- Power-ups -----------------
speed_img = pygame.image.load("speed.jpg").convert_alpha()
speed_img = pygame.transform.scale(speed_img, (30, 30))
speed_item = speed_img.get_rect(center=(random.randint(100, WIDTH-100), 320))
speed_last_spawn = pygame.time.get_ticks()
speed_respawn_time = random.randint(20000, 30000)

wings_img = pygame.image.load("angel.png").convert_alpha()
wings_img = pygame.transform.scale(wings_img, (30, 30))
wings_item = wings_img.get_rect(center=(random.randint(100, WIDTH-100), 320))
wings_last_spawn = pygame.time.get_ticks()
wings_respawn_time = random.randint(20000, 30000)

# ----------------- Game Loop -----------------
running = True
while running:
    clock.tick(60)
    now = pygame.time.get_ticks()
    screen.fill((135, 206, 235))  # sky blue

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    # ----------------- Player 1 Controls (Arrows + CTRL) -----------------
    p1_speed = 5 * speed_boost1
    if keys[pygame.K_RIGHT]:
        player1.x += p1_speed
    if keys[pygame.K_LEFT]:
        player1.x -= p1_speed
    if keys[pygame.K_RCTRL] or keys[pygame.K_LCTRL]:
        if wings1 or vel_y1 == 0:
            vel_y1 = jump_speed

    # ----------------- Player 2 Controls (WASD + SPACE) -----------------
    p2_speed = 5 * speed_boost2
    if keys[pygame.K_d]:
        player2.x += p2_speed
    if keys[pygame.K_a]:
        player2.x -= p2_speed
    if keys[pygame.K_SPACE]:
        if wings2 or vel_y2 == 0:
            vel_y2 = jump_speed

    # ----------------- Gravity -----------------
    if not wings1:
        vel_y1 += gravity
        player1.y += vel_y1
    else:
        vel_y1 = 0
    if not wings2:
        vel_y2 += gravity
        player2.y += vel_y2
    else:
        vel_y2 = 0

    # ----------------- Collision with Ground -----------------
    for plat in ground_rects:
        if player1.colliderect(plat) and vel_y1 >= 0:
            player1.bottom = plat.top
            vel_y1 = 0
        if player2.colliderect(plat) and vel_y2 >= 0:
            player2.bottom = plat.top
            vel_y2 = 0

    # ----------------- Scroll Ground -----------------
    for plat in ground_rects:
        plat.x -= ground_speed
    if ground_rects[0].right < 0:
        ground_rects.pop(0)
        new_x = ground_rects[-1].right
        ground_rects.append(pygame.Rect(new_x, ground_y, ground_block_width, ground_height))

    # ----------------- Power-up Collisions -----------------
    # Speed
    if player1.colliderect(speed_item):
        speed_boost1 = 1.5
        speed_item.x = -100
        speed_last_spawn = now
        speed_respawn_time = random.randint(20000, 30000)
    if player2.colliderect(speed_item):
        speed_boost2 = 1.5
        speed_item.x = -100
        speed_last_spawn = now
        speed_respawn_time = random.randint(20000, 30000)

    # Wings
    if player1.colliderect(wings_item):
        wings1 = True
        wings_timer1 = now + 10000
        wings_item.x = -100
        wings_last_spawn = now
        wings_respawn_time = random.randint(20000, 30000)
    if player2.colliderect(wings_item):
        wings2 = True
        wings_timer2 = now + 10000
        wings_item.x = -100
        wings_last_spawn = now
        wings_respawn_time = random.randint(20000, 30000)

    # Wings timeout
    if wings1 and now > wings_timer1:
        wings1 = False
    if wings2 and now > wings_timer2:
        wings2 = False

    # ----------------- Power-up Respawn -----------------
    if now - speed_last_spawn > speed_respawn_time and speed_item.x < 0:
        speed_item.center = (random.randint(100, WIDTH-100), 320)
    if now - wings_last_spawn > wings_respawn_time and wings_item.x < 0:
        wings_item.center = (random.randint(100, WIDTH-100), 320)

    # ----------------- Drawing -----------------
    for plat in ground_rects:
        pygame.draw.rect(screen, (50, 200, 50), plat)
    screen.blit(player_img, player1)
    screen.blit(player_img, player2)
    screen.blit(speed_img, speed_item)
    screen.blit(wings_img, wings_item)

    pygame.display.flip()

pygame.quit()
