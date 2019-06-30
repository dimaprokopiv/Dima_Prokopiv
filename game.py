#pylint: disable=C0321 
import pygame


pygame.init()
screen = pygame.display.set_mode((500,500))
pygame.display.set_caption("My first game")
x=50
y=50
width=40
height=60
vol=5

#clock = pygame.time.Clock()

done = False
clock = pygame.time.Clock()

while not done:
    pygame.time.delay(20)
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            done=True
    
    keys=pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and x != 0:
        x=x-vol
    if keys[pygame.K_RIGHT] and x < 500-width:
        x=x+vol
    if keys[pygame.K_UP] and y != 0:
        y=y-vol
    if keys[pygame.K_DOWN] and y < 500-height:
        y=y+vol
    screen.fill((0,0,0))    
    pygame.draw.rect(screen, (255,0,0), [x, y, width, height])
    pygame.draw.circle(screen, (0,0,0), (x+15, y+15), 10)     
    
    
    pygame.display.update()


	# clock.tick(60)