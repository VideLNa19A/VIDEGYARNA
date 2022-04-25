import math
import random
from Algorithms import Algorithms
from GameField import GameField
from Food import Food


class Entity:
	# List to store entities
	entities = []
	safe_entities = []

	energy_total = (5**3 * 5**2.3 + 5**2) * 600

	starting_colour = (90, 195, 255)

	# Decide if entities have different species and interact accordingly
	has_species = True
	has_predator_and_prey = True

	def __init__(self, sight=5, speed=5, size=5, species="Art1"):
		# Add to entities list
		self.entities.append(self)

		# Attributes
		self.sight = sight
		self.speed = speed
		self.size = size

		# Attributes with adjusted values to make sense for simulation
		self.sight_adjusted = self.sight * 6 + self.size
		self.speed_adjusted = self.speed / 3
		self.size_adjusted = self.size

		self.species = species

		# Entity starting coulour for visualisation
		self.colour = Entity.starting_colour

		# Starting position and angle
		self.change_pos([0,0])
		# Starting positions using set_starting_pos has to be done from main

		# Steering
		self.steer = 2 * math.pi / 90
		self.desired_angle = Algorithms.angle_positions(self.pos, GameField.random_point(0.8))
		self.angle = self.desired_angle

		# Hunger for behaviour
		self.food_eaten = 0

		# Energy usage per time unit, uses leveled values
		if self.species == "Art2" and Entity.has_predator_and_prey:
			self.energy_usage = (self.size)**2.5 * (self.speed)**2.25 + (self.sight)**2
		else:
			self.energy_usage = (self.size)**3 * (self.speed)**2.3 + (self.sight)**2
		self.energy_left = Entity.energy_total
		# Energy at which to return to edge if food_eaten == 1
		self.return_energy = 1.1 * (GameField.radius / self.speed_adjusted) * self.energy_usage

		# Generations survived
		self.age = 0



#region Changing things
	def change_pos(self, pos):
		# Changes x, y and pos to new pos [x, y]
		self.pos = pos
		self.x = pos[0]
		self.y = pos[1]
	

	def normalize_angles(self):
		# Sets angle and desired angle to between 0 - 2pi radians
		self.desired_angle = Algorithms.normalize_angle(self.desired_angle)
		self.angle = Algorithms.normalize_angle(self.angle)


	def change_angle(self):
		# Change angle depending on steer speed, desired angle and distance to rotate
		if self.desired_angle > self.angle:
			if abs(self.angle - self.desired_angle) > math.pi:
				self.angle -= self.steer
			else:
				self.angle += self.steer
		elif self.desired_angle < self.angle:
			if abs(self.angle - self.desired_angle) > math.pi:
				self.angle += self.steer
			else:
				self.angle -= self.steer

	
	def change_colour(self):
		# Change color depending on food eaten for clearer visualisation
		if self.food_eaten == 1:
			self.colour = (163, 89, 255)
		elif self.food_eaten == 2:
			self.colour = (255, 89, 230)
		else: 
			self.colour = (255, 56, 79)
#endregion



#region Moving
	def move(self):
		# Steering, changing maginitude ups randomness
		self.desired_angle += 1.5 * self.steer * (random.random() * 2 - 1)

		self.is_fleeing = False
		self.entities_check()

		if Entity.has_predator_and_prey:
			if self.species == "Art1":
				self.food_check()
		else:
			self.food_check()

		self.energy_left -= self.energy_usage

		# Return to edge if energy_left is lower than return_energy and has eaten food or has eaten more than 1 food 
		if self.energy_left < self.return_energy and self.food_eaten > 0 or self.food_eaten > 1:
			self.desired_angle = Algorithms.angle_positions(self.pos, GameField.closest_edge_point(self))

		# If ran out of energy
		if self.energy_left <= 0:
			Entity.entities.remove(self)

		# Change angle towards desired angle
		self.normalize_angles()
		self.change_angle()

		# Calculate new position for entity
		self.x += self.speed_adjusted * math.cos(self.angle)
		self.y += self.speed_adjusted * math.sin(self.angle)
		self.pos = [self.x, self.y]
		
		self.edge_check()



	def reset_pos(self):
		# Change pos to cloest edge point
		self.change_pos(GameField.closest_edge_point(self))

		# "Bounce back" or stay depending on if hasn't eaten enough food or has time left for eating more 
		if self.energy_left > self.return_energy and self.food_eaten < 2 or self.food_eaten < 1:
			self.angle = Algorithms.angle(self, GameField)
		else:
			self.angle = Algorithms.angle(self, GameField) + math.pi
		
		self.desired_angle = Algorithms.angle_positions([self.x, self.y], GameField.random_point(0.95))

		# Normalize angles
		self.normalize_angles()


	def set_starting_pos(self):
		# Returns starting position for self depending on position in Enity.entities 
		# 	to give a uniform distribution around gamefield
		
		# Angle from centre towards new position
		temp_angle = ((2 * math.pi) / len(Entity.entities)) * Entity.entities.index(self)

		# New position
		self.x = (GameField.radius - 1) * math.cos(temp_angle) + GameField.x
		self.y = (GameField.radius - 1) * math.sin(temp_angle) + GameField.y
		self.pos = [self.x, self.y]

		# Set own angle towards centre of gamefield
		self.angle = Algorithms.normalize_angle(temp_angle - math.pi)
		self.desired_angle = self.angle

	
	def edge_check(self):
		# Checks if entity is outside gamefield and changes pos if true
		distance = Algorithms.distance(self, GameField)
		if distance > GameField.radius:
			self.reset_pos()
			# If entities have returned with food then move to Entity.safe_entitites for next round
			if self.food_eaten >= 2 or self.food_eaten == 1 and self.energy_left < self.return_energy:
				if self in Entity.entities:
					# Make self safe
					Entity.safe_entities.append(self)
					Entity.entities.remove(self)
#endregion



#region Entities
	def eat_entity(self, entity):
		# To eat entity
		Entity.entities.remove(entity)
		self.food_eaten += 1

		self.change_colour()


	def entities_check(self):
		# If species are turned on
		if Entity.has_species:
			# Check for other entities and execute behaviours
			for entity in Entity.entities:
				# If entities aren't of the same species
				if entity.species != self.species:
					# Get distance
					distance = Algorithms.distance(self, entity)

					# If self can see body of entity
					if distance != 0 and distance - entity.size_adjusted < self.sight_adjusted:
						size_diff = 1.1

						if Entity.has_predator_and_prey:
							# Chase if self.size is size_diff times bigger
							if self.size > entity.size * size_diff and self.species == "Art2":
								self.desired_angle = Algorithms.angle(self, entity)
								self.normalize_angles()

								# Eat entity if bodies touch
								if distance <= self.size_adjusted + entity.size_adjusted and self.species != "Art1":
									self.eat_entity(entity)

							# Flee if entity is size_diff times bigger
							elif self.size * size_diff < entity.size and self.species == "Art1":
								self.desired_angle = Algorithms.angle(entity, self)
								self.normalize_angles()
								self.is_fleeing = True

						else:
							# Chase if self.size is size_diff times bigger
							if self.size > entity.size * size_diff:
								self.desired_angle = Algorithms.angle(self, entity)
								self.normalize_angles()

								# Eat entity if bodies touch
								if distance <= self.size_adjusted + entity.size_adjusted:
									self.eat_entity(entity)

							# Flee if entity is size_diff times bigger
							elif self.size * size_diff < entity.size:
								self.desired_angle = Algorithms.angle(entity, self)
								self.normalize_angles()
								self.is_fleeing = True
					
		# If species are turned off
		else:
			# Check for other entities (same species or not) and execute behaviours
			for entity in Entity.entities:
				# Get distance
				distance = Algorithms.distance(self, entity)

				# If self can see body of entity
				if distance != 0 and distance - entity.size_adjusted < self.sight_adjusted:
					size_diff = 1.1

					# Chase if self.size is size_diff times bigger
					if self.size > entity.size * size_diff:
						self.desired_angle = Algorithms.angle(self, entity)
						self.normalize_angles()

						# Eat entity if bodies touch
						if distance <= self.size_adjusted + entity.size_adjusted:
							self.eat_entity(entity)

					# Flee if entity is size_diff times bigger
					elif self.size * size_diff < entity.size:
						self.desired_angle = Algorithms.angle(entity, self)
						self.normalize_angles()
						self.is_fleeing = True
#endregion
	


#region Food
	def eat_food(self, food):
		# To eat food
		Food.foods.remove(food)
		self.food_eaten += 1

		self.change_colour()


	def food_check(self):
		# Loops through food and chases to eat it if entity isn't being chased
		for food in Food.foods:
			distance = Algorithms.distance(self, food)

			# If entity can see the food and isn't fleeing, chase food
			if distance <= self.sight_adjusted + food.radius and self.is_fleeing == False:
				self.desired_angle = Algorithms.angle(self, food)

			# If entity is toching the food, eat
			if distance <= self.size_adjusted + food.radius:
				self.eat_food(food)

#endregion


#region Evolution
	@classmethod
	def evolve(cls):
		# Method for adding new entities based on safe entities' attributes and food eaten
		change = 0.5
		for entity in cls.safe_entities:
			if entity.food_eaten > 1:
				for i in range(entity.food_eaten - 1):
					max2 = lambda x: 2 if x > 2 else x

					# Set new entity's sight
					sight_change_direction = random.randint(-1, 1)
					if sight_change_direction == 1:
						sight = entity.sight + sight_change_direction * max2(11.25 - 5/4 * entity.sight) * change * random.random()
					elif sight_change_direction == -1:
						sight = entity.sight + sight_change_direction * max2(-1.25 + 5/4 * entity.sight) * change * random.random()
					else:
						sight = entity.sight

					# Set new entity's speed
					speed_change_direction = random.randint(-1, 1)
					if speed_change_direction == 1:
						speed = entity.speed + speed_change_direction * max2(11.25 - 5/4 * entity.speed) * change * random.random()
					elif speed_change_direction == -1:
						speed = entity.speed + speed_change_direction * max2(-1.25 + 5/4 * entity.speed) * change * random.random()
					else:
						speed = entity.speed

					# Set new entity's size
					size_change_direction = random.randint(-1, 1)
					if size_change_direction == 1:
						size = entity.size + size_change_direction * max2(11.25 - 5/4 * entity.size) * change * random.random()
					elif size_change_direction == -1:
						size = entity.size + size_change_direction * max2(-1.25 + 5/4 * entity.size) * change * random.random()
					else:
						size = entity.size

					Entity(sight, speed, size, entity.species)

					# Old: speed = entity.speed + random.randint(-1, 1) * max2(5 - 5/4 * abs(entity.speed - 5)) * change * random.random()

#endregion
