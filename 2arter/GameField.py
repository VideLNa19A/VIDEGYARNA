import math
import random
from Algorithms import Algorithms
from Window import Window


class GameField:
		# Position of center
		x = Window.width / 2
		y = Window.height / 2
		pos = [x, y]

		# Radius set after distance to closest edge
		if Window.width <= Window.height:
			radius = Window.width / 2
		else:
			radius = Window.height / 2

		# Colour for visualisation
		colour = (17, 137, 0)


		@classmethod
		def random_point(cls, range):
			# Returns a random point within decimal range of circle radius, 1=100% etc
			a = random.random() * 2 * math.pi
			r = cls.radius * math.sqrt(random.random()) * range
			x = r * math.cos(a) + cls.x
			y = r * math.sin(a) + cls.y

			return [x, y]

		@classmethod
		def random_edge_point(cls, range):
			# Returns a random point at the edge of range of circle radius
			a = random.random() * 2 * math.pi
			x = cls.radius * range * math.cos(a) + cls.x
			y = cls.radius * range * math.sin(a) + cls.y

			return [x, y]
		
		@classmethod
		def closest_edge_point(cls, entity):
			# Returns closest point on edge for point in circle
			a = Algorithms.angle(cls, entity)
			x = cls.radius * math.cos(a) + cls.x
			y = cls.radius * math.sin(a) + cls.y

			return [x, y]
