import pygame
import random
import time
import os

#параметры
WIDTH = 1000 
HEIGHT = 1000
FPS = 60 

#параметры прыжка
isJump = False
jumpCount = 10
#эксперимент
mobSpeed = 5
#экран

screen = pygame.display.set_mode((WIDTH, HEIGHT))



#настройка папки ассетов
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'img')
player_img = pygame.image.load(os.path.join(img_folder, 'Base pack\Player\p1_jump.png')).convert()





#цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (0, 255, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
c1 = (47 , 49, 54)
c2 = (255, 219, 77)
c3 = (105, 123, 174)


#классы



#платфотмы
class Platform(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface((100, 15))
		self.image.fill(c2)
		self.rect = self.image.get_rect()
		self.rect.x = random.randrange(WIDTH - self.rect.width)
		self.rect.y = random.randrange(-1000, -15) 
		self.speedy = 3
	def update(self):
		self.rect.y += self.speedy
		if self.rect.top > HEIGHT + 10:
			self.rect.x = random.randrange(WIDTH - self.rect.width)
			self.rect.y = random.randrange(-100, -40)
			self.speedy = 3
#мобы	
class Mob(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface((93.75, 150))
		self.image.fill((182, 26, 0))
		self.rect = self.image.get_rect()
		self.rect.x = WIDTH - 200
		self.rect.y = HEIGHT - 200
		self.speedx = mobSpeed 
	def update(self):
		self.rect.x += self.speedx
		
		if self.rect.right > WIDTH:
			self.rect.right = WIDTH
		if self.rect.left < 0:
			self.rect.left = 0
		if self.rect.top < 0:
			self.rect.top = 0
		if self.rect.bottom > HEIGHT:
			self.rect.bottom = HEIGHT
#игрок			
class Player(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = player_img
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
		self.rect.centerx = WIDTH / 2 
		self.rect.centery = HEIGHT -100
		self.isJump = False
		self.jumpCount = 10
		self.rect.x = 500
		self.rect.y = 500
	
	def update(self):
		#передвижение
		self.speedx = 0
		self.speedy = 0
		keystate = pygame.key.get_pressed()
		if keystate[pygame.K_a]:
			self.speedx = -7
		if keystate[pygame.K_d]:
			self.speedx = 7 
		if keystate[pygame.K_w]:
			self.speedy = -7
		if keystate[pygame.K_s]:
			self.speedy = 7
		self.rect.x += self.speedx
		self.rect.y += self.speedy
		
		#границы экрана
		if self.rect.right > WIDTH:
			self.rect.right = WIDTH
		if self.rect.left < 0:
			self.rect.left = 0
		if self.rect.top < 0:
			self.rect.top = 0
		if self.rect.bottom > HEIGHT:
			self.rect.bottom = HEIGHT
		#прыжок
		if self.isJump:
			if self.jumpCount >= -10:
				neg = 1
				if self.jumpCount < 0:
					neg = -1
				self.rect.y -= self.jumpCount ** 2 * neg // 2
				self.jumpCount -= 1
			else:
				self.isJump = False
				self.jumpCount = 10
# игра
pygame.init()
pygame.mixer.init()
pygame.display.set_caption("Project S&S")
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
for i in range(60):
	pt = Platform()
	all_sprites.add(pt)
	#platforms.add(t)
m = Mob()
all_sprites.add(m)
Mob.add(m)

player = Player()
all_sprites.add(player)
	

#цикл игры

running = True

while running:
	keystate = pygame.key.get_pressed()
	#скорость цикла
	clock.tick(FPS)
			
	#ввод процесса(события)
	for event in pygame.event.get():
			
				
		#закрыть програму
			
		if keystate[pygame.K_ESCAPE]:
			running = False
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				player.isJump = True	
					
		elif event.type == pygame.QUIT:
			running = False

	#обновление
	all_sprites.update()
			
	#рендеринг
	screen.fill(c3)
	all_sprites.draw(screen)
			
	#переворот экрана
	pygame.display.flip()
	pygame.display.update()



pygame.quit()
