import pygame
from random import *
from time import *
pygame.init()
abc = 0
window = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()
blue = [76, 147, 248]
green = [55, 106, 0]
white = [0, 0, 0]
yellow = (255,255,0)
blockColors = [[255, 255, 255]]
snakeLenghs = 1
snakeXcoord = 250
snakeYcoord = 250
blocks = [] #[snakeXcoord, snakeYcoord+10], [snakeXcoord, snakeYcoord+20]
record = 0
isEat = False
direction = 'up'
eatX = 110
eatY = 110
def RandomColor():
    x = randint(0, 255)
    y = randint(0, 255)
    z = randint(0, 255)
    return [x,y,z]
def gradient():
    oldColors = blockColors[len(blockColors)-1]
    oldX = oldColors[0]
    oldY = oldColors[1]
    oldZ = oldColors[2]
    ooldX = 0
    ooldY = 0
    ooldZ = 0
    if oldX < 255 and oldX != 0:
        ooldX = oldX + 51
    if oldY < 255 and oldY != 0:
        ooldY = oldY + 51
    if oldZ < 255 and oldZ != 0:
        ooldZ = oldZ + 51
    if oldX == 255 and oldY == 0:
        ooldZ = oldZ + 51
    if oldZ == 255 and oldY == 0:
        ooldX = oldX - 51
    if oldZ == 255 and oldX == 0:
        ooldY = oldY + 51
    if oldY == 255 and oldX == 0:
        ooldZ = oldZ - 51
    if oldX == 0 and oldZ == 0:
        ooldX = oldX + 51
    if oldY == 255 and oldX == 0:
        ooldY = oldY - 51
    x = ooldX
    y = ooldY
    z = ooldZ
    return [x,y,z]
def newC(eatX, eatY):
    eatX = randint(1,22) * 10
    eatY = randint(1,22) * 10
    return [eatX, eatY]
startEatPos = newC(eatX, eatY)
eatX = startEatPos[0]
eatY = startEatPos[1]
def move(snakeXcoord, snakeYcoord, isEat, eatX, eatY):
    clear()
    if direction == 'up':
        snakeYcoord -= 10
    if direction == 'down':
        snakeYcoord += 10
    if direction == 'right':
        snakeXcoord += 10
    if direction == 'left':
        snakeXcoord -= 10
    for pos in blocks:
        if pos == blocks[0]:
            color = yellow
        else:
            if abc == 0:
                color = green
            else:
                color = blockColors[blocks.index(pos)]
        snake = pygame.Rect(pos[0], pos[1], 10, 10)
        pygame.draw.rect(window,color,snake)
    eat = pygame.Rect(eatX,eatY,10,10)
    pygame.draw.rect(window,blue,eat)
    pygame.display.update()
    return [snakeXcoord, snakeYcoord, isEat]
def clear():
    window.fill((0,0,0))
def isGameEnd():
    for block in blocks[1:]:
            b = blocks[0]
            if b[0] == block[0] and b[1] == block[1]:
                return True
while True:
    if isGameEnd() == True:
        print('Вы проиграли! Счёт:', record)
        break
    blocks.insert(0, list([snakeXcoord, snakeYcoord]))
    k = 0
    a = move(snakeXcoord, snakeYcoord, isEat, eatX, eatY)
    snakeXcoord = a[0]
    snakeYcoord = a[1]
    isEat = a[2]
    if snakeXcoord >= 505:
        print('Вы проиграли! Счёт:', record)
        break
    if snakeYcoord >= 505:
        print('Вы проиграли! Счёт:', record)
        break
    if snakeXcoord <= -5:
        print('Вы проиграли! Счёт:', record)
        break 
    if snakeYcoord <= -5:
        print('Вы проиграли! Счёт:', record)
        break
    if eatX == snakeXcoord and eatY == snakeYcoord:
        print('Сьедена еда! Счёт:', record)
        if abc == 1:
            blockColors.append(RandomColor())
        if abc == 2:
            blockColors.append(gradient())
        snakeLenghs += 1
        b = newC(eatX, eatY)
        eatX = b[0]
        eatY = b[1]
        record += 1
    else:
        blocks.pop()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                if direction == 'down':
                    direction == 'down'
                else:
                    direction = 'up'
            if event.key == pygame.K_s:
                if direction == 'up':
                    direction == 'up'
                else:
                    direction = 'down'
            if event.key == pygame.K_a:
                if direction == 'right':
                    direction == 'right'
                else:
                    direction = 'left'
            if event.key == pygame.K_d:
                if direction == 'left':
                    direction == 'left'
                else:
                    direction = 'right'
    clock.tick(15)
