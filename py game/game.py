
#Py Game
import pygame
import os 
import random 
import math


pygame.init()

screen=pygame.display.set_mode((800,600))
pygame.display.set_caption('space shooter game')


BACKGROUND_SPACE_IMAGE = pygame.image.load(os.path.join('Assets','space.png'))
YELLOW_SPACE_IMAGE = pygame.image.load(os.path.join('Assets','spaceship_yellow.png'))
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACE_IMAGE,(70,60)),180)


FPS = 300
spaceshipX = 370
spaceshipY = 490

changeX=0

font =pygame.font.SysFont('Arial',32,'bold')
def score_text():

    img= font.render('score:{score}',True,'white')
    screen.blit(img,(10,10))
font_Gameover =pygame.font.SysFont('Arial',64,'bold')

def Gameover():
      img_Gameover= font_Gameover.render('Game over',True,'white')
      screen.blit(img_Gameover,(200,250))

ALIEN = []
alienX=[]
alienY=[]
alienspeedX=[]
alienspeed=[]

no_of_aliens=6
for i in range(no_of_aliens):
     ALIEN = pygame.image.load('enemy.png')
     alienX=random.randint(0,736)
     alienY=random.randint(30,150)

     alienspeedX=1
     alienspeedY=40
     
     
                 
     


BULLET = pygame.image.load('bullet.png')
check = False
bulletX=383.5
bulletY=460
score=0


        
       

def draw_window():
     screen.blit(YELLOW_SPACESHIP,(spaceshipX,spaceshipY))
     screen.blit(ALIEN,(alienX,alienY))
     
        

clock = pygame.time.Clock()
running= True
while running:
    clock.tick(FPS)
    screen.blit(BACKGROUND_SPACE_IMAGE,(0,0))
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type==pygame.KEYDOWN:
                 if event.key==pygame.K_LEFT:
                      changeX=-1
                 if event.key==pygame.K_RIGHT:
                      changeX=1
                 if event.key==pygame.K_SPACE:
                    if check is False:
                      check=True
                      bulletX=spaceshipX+13.5
                 
                    if event.type==pygame.KEYUP:
                         changeX=0
                    
                    if alienY>420:
                         alienY=2000
                         Gameover()
                 
    
    
    spaceshipX+= changeX 
    if spaceshipX<=0:
         spaceshipX=0
    elif spaceshipX>=730:
         spaceshipX=730
    
    for i in range(no_of_aliens):
     if alienY[i] > 420:
           for j in range(no_of_aliens):
               alienY[j]=2000
           Gameover()
           break
     alienX[i]+= alienspeedX
     if alienX[i]<=0:
          alienspeedX[i]=1
          alienY[i]+=alienspeedY
     if alienX[i]>=730:
          alienspeedX[i]=-1
          alienY[i]+=alienspeedY
     
     distance = math.sqrt(math.pow(bulletX-alienX[i],2)+math.pow(bulletY-alienY[i],2))
     if distance <27:
    
         bulletY = 460
         check = False

         alienX[i]=random.randint(0,736)
         alienY[i]=random.randint(30,150)
         score+=1

     screen.blit(ALIEN[i],(alienX[i],alienY[i]))    
    if bulletY<=0:
         bulletY=460
         check = False
    if check is True:
        screen.blit(BULLET,(bulletX,bulletY))
        bulletY = -1
           
    
       
        
     
    
    


    

     
         
        

    
         
    score_text()
    draw_window()
    pygame.display.update()

    
   










