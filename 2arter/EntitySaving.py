from os import stat
from Entities import Entity
from csv import reader
import re

class EntitySaving:
	@classmethod
	def potentially_save_entities(cls):
		# Choose wether or not to save entities to "SavedEntities" - file
		while True:
			# Input
			x = input("\nSave entities? y/n: ")
		
			if x == "n" or x == "N" or x.lower() == "no" or x == "2":
				break
			elif x == "y" or x == "Y" or x.lower() == "yes" or x == "1":
				# If yes write entity attributes to file 
				cls.save_entities()
				break
			else:
				#print("Entry invalid\n")
				break


	@staticmethod
	def save_entities():
		# Function will save entities in Entity.entities to "SavedEntities.txt", can be done at any point
		with open("SavedEntities.txt", "w") as file:
			for entity in Entity.entities:
				text = "%s\t%s\t%s\n" % (entity.sight, entity.speed, entity.size)
				file.write(text)
			print("Save successful")


	@staticmethod
	def load_entities(file, amount, species):
		# Creates entities with attributes from SavedEntities.txt to simulation
		with open(file) as f:
			for i in range(amount):
				# create list for entity attributes and change str values to float
				entity_attributes = f.readline()
				entity_attributes = re.split(r'\t+', entity_attributes.rstrip('\t'))
				for i in range(3):
					entity_attributes[i] = float(entity_attributes[i])
				# Create entities
				Entity(entity_attributes[0], entity_attributes[1], entity_attributes[2], species)
