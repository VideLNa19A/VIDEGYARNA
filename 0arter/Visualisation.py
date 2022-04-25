import pygame
import math
from GameField import GameField
from Window import Window
from Entities import Entity
from Food import Food


class Visualisation:
	def __init__(self):
		# Initate pygame and display
		pygame.init()
		self.win = pygame.display.set_mode([Window.width, Window.height])
		pygame.display.set_caption("Visualisation")


	def stop_simulation(self):
		# If exit button is pressed
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return False
		return True


	def reset(self):
		# Refill window
		self.win.fill(Window.colour)


	def draw_field(self, field):
		# Draw the circle / area of simulation
		pygame.draw.circle(self.win, field.colour, field.pos, field.radius)

	
	def get_average_colour(self, c1, c2):
		# Returns the touple colour between two touple colours
			r = round((c1[0] + c2[0]) / 2)
			g = round((c1[1] + c2[1]) / 2)
			b = round((c1[2] + c2[2]) / 2)
			return (r, g, b)

	def draw_entities(self):
		# Draw entities and their sight ranges
		for entity in Entity.entities:
			# Entity body circle
			pygame.draw.circle(self.win, entity.colour, entity.pos, entity.size_adjusted)

			# Entity sight circle
			pygame.draw.circle(self.win, self.get_average_colour(entity.colour, GameField.colour), entity.pos, entity.sight_adjusted, 1)

			# Entity direction, black
			eye_x = entity.x + entity.sight_adjusted * math.cos(entity.angle)
			eye_y = entity.y + entity.sight_adjusted * math.sin(entity.angle)
			eye_pos = [eye_x, eye_y]
			pygame.draw.circle(self.win, (0, 0, 0), eye_pos, 1)
			
			# Turn direciton, shows steer angle, red
			turn_x = entity.x + entity.sight_adjusted * math.cos(entity.desired_angle)
			turn_y = entity.y + entity.sight_adjusted * math.sin(entity.desired_angle)
			turn_pos = [turn_x, turn_y]
			pygame.draw.circle(self.win, (220, 0, 0), turn_pos, 1)

	
	def draw_safe_entities(self):
		# Draw safe and returned entities
		for entity in Entity.safe_entities:
			safe_colour = (121, 135, 122)
			
			# Draw body circle
			pygame.draw.circle(self.win, safe_colour, entity.pos, entity.size_adjusted)

			# Draw sight circle
			pygame.draw.circle(self.win, self.get_average_colour(safe_colour, GameField.colour), entity.pos, entity.sight_adjusted, 1)


	def draw_food(self):
		for food in Food.foods:
			pygame.draw.circle(self.win, food.color, food.pos, food.radius)


	def update(self):
		# Update screen
		pygame.display.flip()


	def quit(self):
		# Quit pygame
		pygame.quit()
