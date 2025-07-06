#Pygame - Space 

import pygame
import time
import random
pygame.font.init()

WIDE, HEIGHT = 1000, 800
WIN= pygame.display.set_mode((WIDE, HEIGHT))
pygame.display.set_caption("Space shooter")
Bg= pygame.transform.scale(pygame.image.load("bg.jpeg"), (WIDE, HEIGHT))
PLAYER_WIDTH=60
PLAYER_HEIGHT=70
PLAYER_VELOCITY= 5
STAR_WIDTH=10
STAR_HEIGHT=15
STAR_VEL= 3

FONT= pygame.font.SysFont("comicsans", 30)

def DISP(player, elapsed_time, stars):

    WIN.blit(Bg, (0,0))
    time_text = FONT.render(f"Time elapsed: {round(elapsed_time)}s", 1, "red")

    WIN.blit(time_text, (5,5))


    pygame.draw.rect(WIN, "red", player)
    for star in stars:
        pygame.draw.rect(WIN, "white", star)
    
    pygame.display.update()


def main():
    flag = True
    
    player=pygame.Rect(500, HEIGHT-PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)
    
    clock=pygame.time.Clock()

    start_time = time.time()
    
    elapsed_time = 0

    star_add_increment= 2000

    star_count= 0

    stars=[]

    while flag:
        star_count+= clock.tick(120)
        elapsed_time= time.time() - start_time
        hit= False
        if star_count>star_add_increment:
            for _ in range(3):
                star_x = random.randint(0, WIDE-STAR_WIDTH)
                star= pygame.Rect(star_x, -STAR_HEIGHT, STAR_WIDTH, STAR_HEIGHT)
                stars.append(star)

            star_add_increment=max(200, star_add_increment-50)
            star_count= 0

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                flag=False
                break
        
        keys=pygame.key.get_pressed()
        
        if( keys[pygame.K_LEFT] and player.x - PLAYER_VELOCITY>=0):
            player.x -= PLAYER_VELOCITY 
        
        if( keys[pygame.K_RIGHT] and player.x + PLAYER_VELOCITY + PLAYER_WIDTH <=WIDE):
            player.x+= PLAYER_VELOCITY
        
        for star in stars[:]:
            star.y+=STAR_VEL
            if star.y>HEIGHT:
                stars.remove(star)
            elif star.y + star.height >= player.y and star.colliderect(player):
                stars.remove(star)
                hit= True
                break 
        
        if hit:
            LOST_TEXT = FONT.render("YOU LOST! Thanks for playing Aathi's first game!", 1, 'white')
            WIN.blit(LOST_TEXT, (WIDE/2 - LOST_TEXT.get_width()/2, HEIGHT/2 - LOST_TEXT.get_height()/2))
            pygame.display.update()
            pygame.time.delay(5000)
            break
        DISP(player, elapsed_time,stars)
    pygame.quit()
if __name__=="__main__":
    main()