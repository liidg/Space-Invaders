import math
import random

import pygame
from pygame import mixer

# Initialize the pygame
pygame.init()

# Screen
screen = pygame.display.set_mode((800, 600))

# Background
background = pygame.image.load('media/background.png')
mixer.music.load('media/Moon-Crystals.mp3')
mixer.music.play(-1)
# Titulo y icono
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("media/ovni.png")
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('media/nekito.png')
playerX = 370
playerY = 480
playerX_change = 0

# Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
numberOfEnemies = 12

for i in range(numberOfEnemies):
    enemyImg.append(pygame.image.load('media/aylmao.png'))
    enemyX.append(random.randint(0, 730))
    enemyY.append(random.randint(10, 150))
    enemyX_change.append(1.2)
    enemyY_change.append(20)

bulletImg = pygame.image.load("media/ikura.png")
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 3
bulletState = "Ready"

# Score
score_value = 0
font = pygame.font.Font("freesansbold.ttf", 32)

textX = 10
textY = 10

# Game Over
announcement_font = pygame.font.Font("freesansbold.ttf", 256)


def show_score(x, y):
    score = font.render("Score :" + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


def announcement():
    announcement_text = font.render("Game Over", True, (255, 255, 255))
    screen.blit(announcement_text, (300, 250))


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


def fire_bullet(x, y):
    global bulletState
    bulletState = "Fire"
    screen.blit(bulletImg, (x, y))


def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False


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
                playerX_change = -1.5
            if event.key == pygame.K_RIGHT:
                playerX_change = 1.5
            if event.key == pygame.K_SPACE:
                if bulletState == "Ready":
                    bullet_sound = mixer.Sound('media/catmeow.wav')
                    bullet_sound.play()
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
    for i in range(numberOfEnemies):

        # Game Over
        if enemyY[i] > 440:
            for j in range(numberOfEnemies):
                enemyY[j] = 2000
            announcement()
            break

        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 1.2
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -1.2
            enemyY[i] += enemyY_change[i]

        # Collision
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            collision_sound = mixer.Sound('media/sparkle.wav')
            collision_sound.play()
            bulletY = 480
            bulletState = "Ready"
            score_value += 1
            print(score_value)
            enemyX[i] = random.randint(0, 735)
            enemyY[i] = random.randint(50, 150)

        enemy(enemyX[i], enemyY[i], i)

    # Bullet movement
    if bulletY <= 0:
        bulletY = 480
        bulletState = "Ready"
    if bulletState == "Fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    player(playerX, playerY)
    show_score(textX, textY)
    pygame.display.update()
