import random,math,pygame
from pygame import mixer
#initialize
pygame.init()
#create game window
screen = pygame.display.set_mode((900,700))
#background
background = pygame.image.load('PythonMiniProjects/Space Invader/Files/space.jpg')
#title and icon
pygame.display.set_caption('Space Invader')
icon = pygame.image.load('PythonMiniProjects/Space Invader/Files/993515.png')
#player
playerimg = pygame.image.load('PythonMiniProjects/Space Invader/Files/spaceship.png')
playerX = 418
playerY = 550
player_X_change = 0
player_Y_change = 0
#Enemy
enemyimg = []
enemyX = []
enemyY = []
enemy_X_change = []
enemy_Y_change = []
num_of_enemies  = 7
for i in range(num_of_enemies):
    enemyimg.append(pygame.image.load('PythonMiniProjects/Space Invader/Files/monster.png'))
    enemyX.append(random.randint(30,770))
    enemyY.append(random.randint(30,130))
    enemy_X_change.append(0.5)
    enemy_Y_change.append(30)
#Bullet
bulletimg = pygame.image.load('PythonMiniProjects/Space Invader/Files/bullet.png')
bulletY = 550
bulletX = 0
bullet_Y_change = 5
bullet_state = 'ready'
pygame.display.set_icon(icon)
def enemy(x,y):
    screen.blit(enemyimg[i],(x,y))
def player(x,y):
    screen.blit(playerimg,(x,y))
def bullet(x,y) :
    global bullet_state 
    bullet_state = 'fired'
    screen.blit(bulletimg,(x+16,y+20))
def collision_detection(enemyX,enemyY,bulletX,bulletY):
    #find the distacne between enemy and bullet to detect collision
    distance = math.sqrt(math.pow(enemyX-bulletX,2)+ math.pow(enemyY-bulletY,2))
    if distance < 25 :
        return True
    else :
        return False
score_value = 0
font = pygame.font.Font('freesansbold.ttf',32)
textX = 10
textY = 10
def score(x,y):
    show_score = font.render('Score : ' + str(score_value) , True , (255,255,255))
    screen.blit(show_score,(x,y))
running = True
while running :
    screen.fill((0,0,0))
    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #binding with keys on keyboard
    #And KEYDOWN means pressing the key
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_RIGHT :
                player_X_change = 1
            if event.key == pygame.K_LEFT :
                player_X_change = -1
            if event.key == pygame.K_SPACE :
                if bullet_state == 'ready' :
                    bulletX = playerX
                    shoot = mixer.Sound ('PythonMiniProjects/Space Invader/shoot.wav')
                    shoot.play()
                    bullet(bulletX,bulletY)

        elif event.type == pygame.KEYUP :
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT :
                player_X_change = 0
    #Player motion          
    if playerX <= 0:
        playerX = 0
    if playerX >=838:
        playerX = 838
    #Enemy motion
    for i in range(num_of_enemies):
        if enemyY[i] >= 500 :
            enemyY[i] = 2000
            break
        if enemyX[i] <= 0 :
            enemy_X_change[i] -=0.5
            enemyY[i] += enemy_Y_change[i]
        if enemyX[i] >=868 :
            enemy_X_change[i] += 0.5
            enemyY[i] += enemy_Y_change[i]
        enemyX[i] -= enemy_X_change[i]
        enemy(enemyX[i],enemyY[i])
        collision = collision_detection(enemyX[i],enemyY[i],bulletX,bulletY)
        if collision :
            fall = mixer.Sound('PythonMiniProjects/Space Invader/falling.wav')
            fall.play()
            bullet_state = 'ready'
            bulletY = 550
            score_value +=1
            enemyX[i] = random.randint(30,770)
            enemyY[i] = random.randint(30,130)
    playerX += player_X_change    
    playerY += player_Y_change
    if bulletY <=0 :
        bulletY = 550
        bullet_state = 'ready'
    #Show the score
    score(textX,textY)
    #break the game
    if enemyY[i] == 2000 :
        break
    #bullet motion
    if bullet_state == 'fired' :
        bulletY -= bullet_Y_change
        bullet(bulletX,bulletY)    
    player(playerX,playerY)
    pygame.display.update()

