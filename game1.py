import pygame

pygame.init()

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('FstGame')
clock = pygame.time.Clock()
dinoImg = pygame.image.load('rsz_dinoo.png')

def dino(x,y):
	gameDisplay.blit(dinoImg,(x,y))

x = 100
y = (display_height * 0.8)
y_change = 0

crashed = False

while not crashed:
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			crashed == True

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				y_change = -5
			elif event.key == pygame.K_DOWN:
				y_change = 5



	gameDisplay.fill(white)
	dino(x,y)
	pygame.display.update()
	clock.tick(60)

pygame.quit()
quit()