# Imports
import time
from tracemalloc import stop
from GameField import GameField
from Entities import Entity
from Food import Food
from EntitySaving import EntitySaving


# Visualise simulation and/or display statistics
visualise_simulation = False
display_statistics = True

if visualise_simulation:
	from Visualisation import Visualisation
	# Initiate displaying simulation
	vis = Visualisation()

if display_statistics:
	from Statistics import Statistics
	# Initiate variables
	entity_amounts = [] # [[start_amount_gen0, end_amount_gen0], [start_amount_gen1, end_amount_gen1], ...]
	entity_statistics = [] # [[{entity attributes}, {entity attributes}], [gen1:{}.{}.]]


# Amount of generations before stopping loop
generation_amount = 501

# Initiating variables
generation = 0


# Initate gamefield
field = GameField()


# Initiate entities for first generation
for i in range(50):
	if i % 5 == 0:
		Entity(6, 6, 6, "Art2")
	Entity(5, 5, 5, "Art1")

#EntitySaving.load_entities("Entities20food.txt", 50, "Art1")
#EntitySaving.load_entities("Entities100food.txt", 50, "Art2")


# Set entity starting positions
for entity in Entity.entities:
	entity.set_starting_pos()

stop_in_x = False

print("Påbörjar simulation")
run = True
if __name__ == "__main__":
	# Loop for generations
	while run and generation < generation_amount:
		# Spawn food at start of generation
		Food.foods.clear() # Clear foods for new generation
		for i in range(int(100)):
			Food()

		# Gather statistics before each generation
		if display_statistics or Entity.has_predator_and_prey:
			# Save entity amount at start of generation
			s1 = 0
			s2 = 0

			for entity in Entity.entities:
				if entity.species == "Art1":
					buffer_prey = [entity.sight, entity.speed, entity.size, "Art1"]
					s1 += 1
				elif entity.species == "Art2":
					buffer_predator = [entity.sight, entity.speed, entity.size, "Art2"]
					s2 += 1
			
			if s1 == 0:
				Entity(buffer_prey[0], buffer_prey[1], buffer_prey[2], buffer_prey[3])
				s1 += 1
			if s2 == 0:
				Entity(buffer_prey[0], buffer_prey[1] + 0.5, buffer_prey[2] * 1.15, buffer_predator[3])
				s2 += 1

			if (s1 == 0 or s2 == 0) and stop_in_x == False:
				stop_in_x = 4

			entity_amounts.append([s1, s2])
			print([s1, s2])

			# Save entity statistics
			entity_statistics.append([])
			for entity in Entity.entities:
				entity_statistics[generation].append({
				"sight": entity.sight, 
				"speed": entity.speed, 
				"size": entity.size, 
				"age": entity.age, 
				"life_span": Entity.energy_total / entity.energy_usage, 
				"species": entity.species
				})


		# Loop within generation
		while run and len(Entity.entities) > 0:
			# Move entities
			for entity in Entity.entities:
				entity.move()

			# visualise simulation
			if visualise_simulation:
				# Change time speed of visualisation
				time.sleep(0.02)

				run = vis.stop_simulation()

				vis.reset()

				vis.draw_field(field)
				vis.draw_entities()
				vis.draw_safe_entities()
				vis.draw_food()

				vis.update()


		# Increase age of survived entities
		for entity in Entity.safe_entities:
			entity.age += 1

		# Create new entities from- and who are similar to survived entities 
		Entity.evolve()

		# Reset entity lists after generation
		Entity.entities += Entity.safe_entities.copy()
		Entity.safe_entities = []

		# Reset entity variables for next generation
		for entity in Entity.entities:
			entity.set_starting_pos()
			entity.food_eaten = 0
			entity.energy_left = entity.energy_total
			entity.colour = Entity.starting_colour
		
		print(generation)
		generation += 1 # Increase generation count then loop

		if stop_in_x != False:
			stop_in_x -= 1
			if stop_in_x == 0:
				run = False



# Quit displaying simulation
if visualise_simulation:
	vis.quit()

print("Simulation avslutad")


# Start multi-threading for getting info while displaying plots
from threading import Thread

thread_2 = Thread(target=Statistics.get_info, args=(entity_statistics,))

# Display statistics
if display_statistics:
    # Ask for getting info on thread 2
	thread_2.start()

    # Shows stats on main thread
	Statistics.show_stats(generation, entity_amounts, entity_statistics)

	# Join thread 2 to main thread
	thread_2.join()


# Ask if last generation's entities should be saved
EntitySaving.potentially_save_entities()
