import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Button!")
main_font = pygame.font.SysFont("cambria", 50)

class Button():
	def __init__(self, image, x_pos, y_pos, text_input):
		self.image = image
		self.x_pos = x_pos
		self.y_pos = y_pos
		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
		self.text_input = text_input
		self.text = main_font.render(self.text_input, True, "white")
		self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

	def draw(self):
		screen.blit(self.image, self.rect)
		screen.blit(self.text, self.text_rect)

	def checkForInput(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			print("Button Press!")

	def changeColor(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			self.text = main_font.render(self.text_input, True, "white")
		else:
			self.text = main_font.render(self.text_input, True, "black")

button_surface = pygame.image.load("assets/button.png")
button_surface = pygame.transform.scale(button_surface, (300, 100))

start_button = Button(button_surface, 400, 300, "Start")
#quit_button = Button(button_surface, 400, 500, "Quit")

while True:
	for event in pygame.event.get():
		if(event.type == pygame.QUIT):
			pygame.quit()
			sys.exit()
		if(event.type == pygame.MOUSEBUTTONDOWN):
			start_button.checkForInput(pygame.mouse.get_pos())
	screen.fill("white")
	start_button.draw()
    start_button.changeColor(pygame.mouse.get_pos()) 
    #quit_button.draw()	   
    #quit_button.changeColor(pygame.mouse.get_pos())

	pygame.display.update()
