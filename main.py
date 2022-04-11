import random

import pygame

# Initializer el pygame
pygame.init()
# Screen
screen = pygame.display.set_mode((800, 600))

background = pygame.image.load('pngs/background.png')

# Titulo y icono
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("pngs/ovni.png")
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('pngs/nekito.png')
playerX = 370
playerY = 480
playerX_change = 0

enemyImg = pygame.image.load('pngs/aylmao.png')
enemyX = random.randint(0, 730)
enemyY = random.randint(10, 150)
enemyX_change = 0.6
enemyY_change = 20

bulletImg = pygame.image.load("pngs/ikura.png")
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 2
bulletState = "Ready"


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y):
    screen.blit(enemyImg, (x, y))


def fire_bullet(x, y):
    global bulletState
    bulletState = "Fire"
    screen.blit(bulletImg, (x, y))


# Game Loop
running = True
while running:
    # RGB pantalla negra

    screen.fill((0, 0, 0))

    screen.blit(background, (-1000, -500))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # checkear tecla
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.7
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.7
            if event.key == pygame.K_SPACE:
                if bulletState == "Ready":
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # Player movement
    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # Enemy movement
    enemyX += enemyX_change

    if enemyX <= 0:
        enemyX_change = 0.6
        enemyY += enemyY_change
    elif enemyX >= 736:
        enemyX_change = -0.6
        enemyY += enemyY_change

    # Bullet movement
    if bulletY <= 0:
        bulletY = 480
        bulletState = "Ready"
    if bulletState == "Fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()
