# Imports
import time
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
generation_amount = 101

# Initiating variables
generation = 0


# Initate gamefield
field = GameField()


# Initiate entities for first generation
for i in range(100):
	Entity()

for entity in Entity.entities:
	entity.set_starting_pos()



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
		if display_statistics:
			# Save entity amount at start of generation
			entity_amounts.append([len(Entity.entities)])

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
				time.sleep(0.01)

				run = vis.stop_simulation()

				vis.reset()

				vis.draw_field(field)
				vis.draw_entities()
				vis.draw_safe_entities()
				vis.draw_food()

				vis.update()
		

		# Gather statistics after each generation
		if display_statistics:
			entity_amounts[generation].append(len(Entity.safe_entities))

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
