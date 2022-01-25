#THE ROCK GAME V2.0
import time
import pygame as pg
import win32api
pg.init()


white = (255,255,255)

speed = 20
tela = pg.display.set_mode((500,500))


# IMAGENS
rock = pg.image.load(r"therock.jpg").convert(tela)
rock = pg.transform.scale(rock, (100,100))
inimigo = pg.image.load(r"rianito.png")
inimigo = pg.transform.scale(inimigo, (100,100))
riancol = inimigo.get_rect()

fonte = pg.font.Font('freesansbold.ttf', 20)

x1 = 250
y1 = 250

miny = 0
maxy = 500
minx = 0
maxx = 500
class Enemy:
    def __init__(self,foto,x,y):
        self.x = x
        self.y = y 
        self.foto = foto
        self.a = 1
    
    def move(self):
        self.y += 0.5

        if self.y >= maxy-100:
            self.y = miny
        
    def draw(self):
        tela.blit(self.foto, (self.x, self.y))

    def shoot(self):
        if self.a != self.x:
            if self.a > maxx:
                self.a = self.x

        self.a += 2
        tiro = pg.draw.rect(tela,color=(255,0,0),rect=[self.a, self.y, 20,20])
        return tiro

class Player:
    def __init__(self, x, y, foto):
        self.x = x
        self.y = y
        self.foto = foto 
    def draw(self):
        a = tela.blit(self.foto, (self.x,self.y))
        return a


life = 100

enemy = Enemy(inimigo, 0, 250)


pg.mixer.music.load(r"audio.mp3")
pg.mixer.music.play(loops=-1)
pg.mixer.music.set_pos(23)
pg.mixer.music.set_volume(150)

while True:
    
    tela.fill((0,255,255))

    jogador = Player(x1,y1,rock)
    

    for e in pg.event.get():
        if e.type == pg.QUIT:
            pg.quit()

            quit()
        if e.type == pg.KEYDOWN:
            if e.key == pg.K_LEFT and x1-10>=minx:
                x1 -= speed
            if e.key == pg.K_RIGHT and x1+10<=maxx-100:
                x1 += speed
            if e.key == pg.K_DOWN and y1+10<=maxy-100:
                y1 += speed
            if e.key == pg.K_UP and y1-10>=miny:
                y1 -= speed
    texto = f'Vida: {int(life)}'

    vidatxt = fonte.render(texto,True, white)

    ground = pg.draw.rect(tela, color=(0,255,0), rect=[1, 200, 500, 500])

    enemy.draw()
    enemy.move()
    enemy.shoot()
    enemy.draw()
    jogador.draw()
    
    desenho = jogador.draw()
    if desenho.colliderect(enemy.shoot()):
       life = life - 0.1
        
        

    sun = pg.draw.circle(tela, color=(255,255,0), center=(4,4), radius=70)

    #GUI
    tela.blit(vidatxt, (10,10))

    if life < 0 or life == 0:
        win32api.MessageBox(0, 'Rianito venceu!', 'Perdedor!')
        break

    pg.display.update()
