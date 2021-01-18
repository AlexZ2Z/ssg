import pygame
import os
playerImages = []
playerImages.append(pygame.image.load('../res/img/Base pack/Player/p1_stand.png'))


class Player(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = playerImages
		self.image.set_colorkey(0, 0, 0)
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
