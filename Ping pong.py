import pygame as pg

from random import choice

class Base_sprite(pg.sprite.Sprite):
    def __init__(self, pic, x, y, w, h, speed):
        super().__init__()
        self.picture = pg.transform.scale(pg.image.load(pic), (w, h))
        self.rect = self.picture.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.image = self.picture
        self.speed = speed

    def draw(self):
        mw.blit(self.picture, (self.rect.x, self.rect.y))

class Rocket(Base_sprite):
    
    def update_l(self):
        keys = pg.key.get_pressed()

        if (keys[pg.K_w]) and self.rect.y >= 5:
            self.rect.y -= self.speed

        if (keys[pg.K_s]) and self.rect.y <= win_h - (self.rect.width + 80):
            self.rect.y += self.speed

    
    def update_r(self):
        keys = pg.key.get_pressed()

        if (keys[pg.K_UP]) and self.rect.y >= 5:
            self.rect.y -= self.speed

        if (keys[pg.K_DOWN]) and self.rect.y <= win_h - (self.rect.width + 80):
            self.rect.y += self.speed

class Ball(Base_sprite): 

    def update(self):
        global lifes1
        global lifes2
        
        if self.rect.x >= win_w:
            self.rect.x = win_w/2
            self.rect.y = win_h/2
            lifes1 = lifes1 - 1

        if self.rect.x <= 0:
            self.rect.x = win_w/2
            self.rect.y = win_h/2
            lifes2 = lifes2 - 1


win_w = 700    
win_h = 500

dx = 2
dy = 2

lifes1 = 3
lifes2 = 3

pg.font.init()
font1 = pg.font.SysFont('Arial', 40)
win1 = font1.render('1 player, you win', True, (240, 232, 10))
win2 = font1.render('2 player, you win', True, (240, 232, 10))
lose1 = font1.render('1 player, you lose', True, (235, 19, 19))
lose2 = font1.render('2 player, you lose', True, (235, 19, 19))
font2 = pg.font.SysFont('Arial', 36)

mw = pg.display.set_mode((win_w, win_h)) 
pg.display.set_caption('Ping-pong')
clock = pg.time.Clock()

fon = pg.transform.scale(pg.image.load('fon.jpg'), (win_w, win_h))

rocket1 = Rocket('ping_rocket1.png', 30, 200, 25, 100, 4)
rocket2 = Rocket('ping_rocket2.png', 640, 200, 25, 100, 4)

ball = Ball('ball.png', win_w/2, win_h/2, 50, 50, 2)

rocket2_heart1 = Base_sprite('life1.png', win_w - 60, 20, 50, 40, 0)
rocket2_heart2 = Base_sprite('life1.png', win_w - 110, 20, 50, 40, 0)
rocket2_heart3 = Base_sprite('life1.png', win_w - 160, 20, 50, 40, 0)
rocket1_heart1 = Base_sprite('life1.png', 10, 20, 50, 40, 0)
rocket1_heart2 = Base_sprite('life1.png', 60, 20, 50, 40, 0)
rocket1_heart3 = Base_sprite('life1.png', 110, 20, 50, 40, 0)

pg.mixer.init()
bounce = pg.mixer.Sound('schelchok-vklyucheniya.ogg')

play = True
game_finish = False
while play:

    for e in pg.event.get():
        if e.type == pg.QUIT or \
                (e.type == pg.KEYDOWN and e.key == pg.K_ESCAPE):
            play = False 

    if game_finish == False:

        mw.blit(fon, (0,0))

        ball.rect.x -= dx
        ball.rect.y -= dy

        if ball.rect.y >= win_h - 50 or ball.rect.y <= 0:
            dy *= -1
            bounce.play()


        if ball.rect.colliderect(rocket1.rect) or ball.rect.colliderect(rocket2.rect):
            dx *= -1
            bounce.play()


        if lifes1 == 3:
            rocket2_heart1.draw()
            rocket2_heart2.draw()
            rocket2_heart3.draw()

        if lifes1 == 2:
            rocket2_heart1.draw()
            rocket2_heart2.draw()

        if lifes1 == 1:
            rocket2_heart1.draw()
     
        
        if lifes2 == 3:
            rocket1_heart1.draw()
            rocket1_heart2.draw()
            rocket1_heart3.draw()
            
        if lifes2 == 2:
            rocket1_heart1.draw()
            rocket1_heart2.draw()
            
        if lifes2 == 1:
            rocket1_heart1.draw()
            

        ball.update()
        rocket1.update_l()
        rocket2.update_r()

        rocket1.draw()
        rocket2.draw()
        ball.draw()


        if lifes2 <= 0:
            mw.blit(fon, (0,0))

            game_finish = True
            mw.blit(lose1, (30,80))
            mw.blit(win2, (355, 80))

        if lifes1 <= 0:
            mw.blit(fon, (0,0))

            game_finish = True
            mw.blit(lose2, (355,80))
            mw.blit(win1, (30,80)) 

    else:
        pg.time.delay(4000)
        finish = False
        lifes1 = 3
        lifes2 = 3


    pg.display.update()
    clock.tick(60)