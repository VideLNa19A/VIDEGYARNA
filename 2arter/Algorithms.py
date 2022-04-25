import math


class Algorithms:
	@staticmethod
	def angle(e1, e2):
		# Returns angle of from position of enitity 1 to entity 2
		return math.atan2((e2.y-e1.y), (e2.x-e1.x))

	@staticmethod
	def angle_positions(p1, p2):
		# Returns angle of from position 1 to position 2, [x, y]
		return math.atan2((p2[1]-p1[1]), (p2[0]-p1[0]))

	@staticmethod
	def distance(e1, e2):
		# Returns distance between positions of entity 1 and 2
		return math.sqrt((e1.x-e2.x)**2 + (e1.y-e2.y)**2)
	
	@staticmethod
	def normalize_angle(angle):
		# Set angle to between 0 and 2pi
		return abs((angle) % (2 * math.pi))
		