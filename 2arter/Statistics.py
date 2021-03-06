class Statistics:
	@staticmethod
	def show_stats(generation_amount, entity_amounts, entity_statistics):
		#Imports and style
		import numpy as np
		import matplotlib.pyplot as plt
		plt.style.use('dark_background')
		

		# Initiate the subplot function by number of rows and columns
		figure, axis = plt.subplots(2, 3)
		

		# List for x axis
		x = [i for i in range(0, generation_amount)]
		# List for x_ticks
		x_ticks = [i for i in range(0, generation_amount + 1, 50)]
		# Y-ticks (For entity attributes)
		y_ticks = [i for i in range(0, 11)]


		#region Plot 1 
		# For Entity Amount
		entity_amount_s1 = [entity_amounts[generation][0] for generation in range(len(entity_amounts))]
		entity_amount_s2 = [entity_amounts[generation][1] for generation in range(len(entity_amounts))]

		#entity_amount_s1 = Statistics.get_average_over_generations_list(np, entity_amount_s1)
		#entity_amount_s2 = Statistics.get_average_over_generations_list(np, entity_amount_s2)

		axis[0, 0].set_xticks(x_ticks)
		if max(entity_amount_s1) >= max(entity_amount_s2):
			axis[0, 0].set_yticks([i for i in range(0, max(entity_amount_s1) + 1, 4)])
		else:
			axis[0, 0].set_yticks([i for i in range(0, max(entity_amount_s2) + 1, 4)])

		entity_amount_s1 = Statistics.get_average_of_every_x(np, entity_amount_s1, 5)
		entity_amount_s2 = Statistics.get_average_of_every_x(np, entity_amount_s2, 5)

		s1, = axis[0, 0].plot(x, entity_amount_s1)
		s2, = axis[0, 0].plot(x, entity_amount_s2)

		s1.set_color("springgreen")
		s2.set_color("red")

		s1.set_label("Bytesdjur")
		s2.set_label("Rovdjur")
		axis[0, 0].legend()

		axis[0, 0].set_xlabel("Generation")
		axis[0, 0].set_ylabel("Antal individer")
		axis[0, 0].set_title("Antal individer")
		#endregion
		

		#region Plot 2 
		# For Entity Ages
		entity_ages_s1 = Statistics.get_stat_list(entity_statistics, "age", "Art1")
		average_s1 = Statistics.get_average_list(entity_ages_s1)
		#average_s1 = Statistics.get_average_over_generations_list(np, average_s1)

		entity_ages_s2 = Statistics.get_stat_list(entity_statistics, "age", "Art2")
		average_s2 = Statistics.get_average_list(entity_ages_s2)
		#average_s2 = Statistics.get_average_over_generations_list(np, average_s2)

		axis[0, 1].set_xticks(x_ticks)
		if max(average_s1) >= max(average_s2):
			axis[0, 1].set_yticks([i for i in range(0, int(max(average_s1)) + 3)])
		else:
			axis[0, 1].set_yticks([i for i in range(0, int(max(average_s2)) + 3)])

		average_s1 = Statistics.get_average_of_every_x(np, average_s1, 5)
		average_s2 = Statistics.get_average_of_every_x(np, average_s2, 5)

		avg_s1, = axis[0, 1].plot(x, average_s1)
		avg_s2, = axis[0, 1].plot(x, average_s2)

		avg_s1.set_color("springgreen")
		avg_s2.set_color("red")

		avg_s1.set_label("Genomsnitt bytesdjur")
		avg_s2.set_label("Genomsnitt rovdjur")
		axis[0, 1].legend()

		axis[0, 1].set_xlabel("Generation")
		axis[0, 1].set_ylabel("??lder")
		axis[0, 1].set_title("Individernas ??ldrar")
		#endregion


		#region Plot 3 
		# For life-span (amount of updates until non-safe/returned entity dies)
		entity_life_spans_s1 = Statistics.get_stat_list(entity_statistics, "life_span", "Art1")
		average_s1 = Statistics.get_average_list(entity_life_spans_s1)
		#average_s1 = Statistics.get_average_over_generations_list(np, average_s1)

		entity_life_spans_s2 = Statistics.get_stat_list(entity_statistics, "life_span", "Art2")
		average_s2 = Statistics.get_average_list(entity_life_spans_s2)
		#average_s2 = Statistics.get_average_over_generations_list(np, average_s2)

		axis[0, 2].set_xticks(x_ticks)
		if max(average_s1) >= max(average_s2):
			axis[0, 2].set_yticks([i for i in range(0, int(max(average_s1)) + 1, 500)])
		else:
			axis[0, 2].set_yticks([i for i in range(0, int(max(average_s2)) + 1, 500)])
		

		average_s1 = Statistics.get_average_of_every_x(np, average_s1, 5)
		average_s2 = Statistics.get_average_of_every_x(np, average_s2, 5)

		avg_s1, = axis[0, 2].plot(x, average_s1)
		avg_s2, = axis[0, 2].plot(x, average_s2)

		avg_s1.set_color("springgreen")
		avg_s2.set_color("red")

		avg_s1.set_label("Genomsnitt bytesdjur")
		avg_s2.set_label("Genomsnitt rovdjur")
		axis[0, 2].legend()

		axis[0, 2].set_xlabel("Generation")
		axis[0, 2].set_ylabel("Antal uppdateringar tills d??d")
		axis[0, 2].set_title("Livsl??ngd om individerna ej hinner ??terv??nda")
		#endregion


		#region Plot 4 
		# For Sight 
		entity_sights_s1 = Statistics.get_stat_list(entity_statistics, "sight", "Art1")
		average_s1 = Statistics.get_average_list(entity_sights_s1)
		average_s1 = Statistics.get_average_over_generations_list(np, average_s1)

		entity_sights_s2 = Statistics.get_stat_list(entity_statistics, "sight", "Art2")
		average_s2 = Statistics.get_average_list(entity_sights_s2)
		average_s2 = Statistics.get_average_over_generations_list(np, average_s2)
		
		average_s1 = Statistics.get_average_of_every_x(np, average_s1, 5)
		average_s2 = Statistics.get_average_of_every_x(np, average_s2, 5)

		avg_s1, = axis[1, 0].plot(x, average_s1)
		avg_s2, = axis[1, 0].plot(x, average_s2)

		avg_s1.set_color("springgreen")
		avg_s2.set_color("red")

		avg_s1.set_label("Genomsnitt bytesdjur")
		avg_s2.set_label("Genomsnitt rovdjur")

		axis[1, 0].legend(framealpha=0.5)

		axis[1, 0].set_xticks(x_ticks)
		axis[1, 0].set_yticks(y_ticks)

		axis[1, 0].set_xlabel("Generation")
		axis[1, 0].set_ylabel("Syn")
		axis[1, 0].set_title("Syn")
		#endregion


		#region Plot 5 
		# For Speed
		entity_speeds_s1 = Statistics.get_stat_list(entity_statistics, "speed", "Art1")
		average_s1 = Statistics.get_average_list(entity_speeds_s1)
		average_s1 = Statistics.get_average_over_generations_list(np, average_s1)
		
		entity_speeds_s2 = Statistics.get_stat_list(entity_statistics, "speed", "Art2")
		average_s2 = Statistics.get_average_list(entity_speeds_s2)
		average_s2 = Statistics.get_average_over_generations_list(np, average_s2)

		average_s1 = Statistics.get_average_of_every_x(np, average_s1, 5)
		average_s2 = Statistics.get_average_of_every_x(np, average_s2, 5)

		avg_s1, = axis[1, 1].plot(x, average_s1)
		avg_s2, = axis[1, 1].plot(x, average_s2)

		avg_s1.set_color("springgreen")
		avg_s2.set_color("red")

		avg_s1.set_label("Genomsnitt bytesdjur")
		avg_s2.set_label("Genomsnitt rovdjur")
		axis[1, 1].legend()

		axis[1, 1].set_xticks(x_ticks)
		axis[1, 1].set_yticks(y_ticks)

		axis[1, 1].set_xlabel("Generation")
		axis[1, 1].set_ylabel("Hastighet")
		axis[1, 1].set_title("Hastighet")
		#endregion


		#region Plot 6 
		# For Size
		entity_sizes_s1 = Statistics.get_stat_list(entity_statistics, "size", "Art1")
		average_s1 = Statistics.get_average_list(entity_sizes_s1)
		average_s1 = Statistics.get_average_over_generations_list(np, average_s1)

		entity_sizes_s2 = Statistics.get_stat_list(entity_statistics, "size", "Art2")
		average_s2 = Statistics.get_average_list(entity_sizes_s2)
		average_s2 = Statistics.get_average_over_generations_list(np, average_s2)

		average_s1 = Statistics.get_average_of_every_x(np, average_s1, 5)
		average_s2 = Statistics.get_average_of_every_x(np, average_s2, 5)
		
		avg_s1, = axis[1, 2].plot(x, average_s1)
		avg_s2, = axis[1, 2].plot(x, average_s2)

		avg_s1.set_color("springgreen")
		avg_s2.set_color("red")

		avg_s1.set_label("Genomsnitt bytesdjur")
		avg_s2.set_label("Genomsnitt rovdjur")
		axis[1, 2].legend()

		axis[1, 2].set_xticks(x_ticks)
		axis[1, 2].set_yticks(y_ticks)

		axis[1, 2].set_xlabel("Generation")
		axis[1, 2].set_ylabel("Storlek")
		axis[1, 2].set_title("Storlek")
		#endregion


		# Add grids for plots
		for x in range(3):
			for y in range(2): 
				axis[y, x].grid(color="dimgrey", linestyle='dashed', linewidth=0.5)

		
		# Adjust positioning of plots
		plt.subplots_adjust(left=0.03, bottom=0.05, right=0.993, top=0.967, wspace=0.17, hspace=0.21)
		# Show plots
		plt.show()



	@staticmethod
	def get_stat_list(entity_statistics, statistic, species="Art1"):
		# Statistic should be "sight", "age" etc
		# Returns in form [[a, b] [c, d, e], ...]
		l = []
		for i in range(len(entity_statistics)):
			l.append([])
			for j in range(len(entity_statistics[i])):
				if entity_statistics[i][j]["species"] == species:
					l[i].append(entity_statistics[i][j][statistic])
		return l
				


#region Avg, median, Q1,2,3 etc.
	@staticmethod
	def get_average_list(l):
		# Returns 1D list of average values from 2D linked list 
		avg = []
		for ll in l:
			if len(ll) > 0:
				avg.append(sum(ll) / len(ll))
			else:
				avg.append(0)
		return avg


	@staticmethod
	def get_average_over_generations_list(np, l):
		# Takes in list and returns list with values that are the averages of those around it
		lc = l.copy()
		for i in range(len(l)):
			if i == 0 or i == len(l) - 1:
				continue
			elif i == 1 or i == len(l) - 2:
				lc[i] = np.average(l[i-1:i+2])
			else:
				lc[i] = np.average(l[i-2:i+3])
			return lc
	
	@staticmethod
	def get_average_of_every_x(np, l, x):
		# Uses k to get a make [1, 3, 4, 5] to [1, 2, 3, 4] <-- where 4 is average of the 3 (x) that come after index 0
		# Used for creating a less cluttered line graph  
		lc = l.copy()
		count = 0
		current_average = lc[0]
		for i in range(1, len(lc)):
			if count == 0:
				new_average = np.average(lc[i:i+x])
				current_k = (current_average - new_average) / (-x)
				previous_average = current_average
				current_average = new_average
			count += 1
			lc[i] = previous_average + current_k * count
			if count == x:
				count = 0
		return lc



	@staticmethod
	def get_highest_list(l):
		# Returns 1D list of highest values from 2D linked list 
		hgh = []
		for ll in l:
			if len(ll) > 0:
				hgh.append(max(ll))
			else:
				hgh.append(0)
		return hgh


	def get_q3_list(np, l):
		# Returns 1D list of 3rd quartile values from 2D linked list 
		q3 = []
		for ll in l:
			if len(ll) > 0:
				q3.append(np.percentile(ll, 75))
			else:
				q3.append(0)
		return q3


	@staticmethod
	def get_median_list(np, l):
		# Returns 1D list of median / Q2 values from 2D linked list 
		med = []
		for ll in l:
			if len(ll) > 0:
				med.append(np.percentile(ll, 50))
			else:
				med.append(0)
		return med
		

	def get_q1_list(np, l):
		# Returns 1D list of 1st quartile values from 2D linked list 
		q1 = []
		for ll in l:
			if len(ll) > 0:
				q1.append(np.percentile(ll, 25))
			else:
				q1.append(0)
		return q1


	@staticmethod
	def get_lowest_list(l):
		# Returns 1D list of highest values from 2D linked list 
		low = []
		for ll in l:
			if len(ll) > 0:
				low.append(min(ll))
			else:
				low.append(0)
		return low
#endregion


	def get_info(entity_statistics):
		# Loop for getting information about specific extreme entities in generations
		while True:
			# Get input and maybe exit simulation
			try:
				ge = input("\nGeneration: ")
				if ge == "":
					break
				pt = input("Plot 2-6: ")
				if pt == "":
					break

				pt, ge = int(pt), int(ge)
				
				mm = input("Min / max: ")
				if mm == "":
					break

			except ValueError:
				print("Fel input")
				continue
			
			try:
				# Get plot list
				if pt == 2:
					l = Statistics.get_stat_list(entity_statistics, "age")
				elif pt == 3:
					l = Statistics.get_stat_list(entity_statistics, "life_span")
				elif pt == 4:
					l = Statistics.get_stat_list(entity_statistics, "sight")
				elif pt == 5:
					l = Statistics.get_stat_list(entity_statistics, "speed")
				else:
					l = Statistics.get_stat_list(entity_statistics, "size")

				# Get index of entity
				if mm == "min" or mm == 1:
					i = l[ge].index(min(l[ge]))
				elif mm == "max" or mm == 2:
					i = l[ge].index(max(l[ge]))
				
				# Entity dictionary
				entity = entity_statistics[ge][i]
				
				# Get and round entity attributes
				energy = round(entity["life_span"], 3)
				age = entity["age"]
				species = entity["species"]
				sight = round(entity["sight"], 3)
				speed = round(entity["speed"], 3)
				size = round(entity["size"], 3)

				# Print rounded attributes
				print(f"\n??lder: {age}. Antal uppdateringar innan slut p?? energi: {energy}. Art: {species}")
				print(f"Syn: {sight}. Hastighet: {speed}. Storlek: {size}")
					
			except IndexError:
				print("Fel input")
				continue
