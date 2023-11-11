# Don't Be Last!
# Seneca Howell
# Computational Foundations 2 - Spring 2023
# Recitation 011

# Opens the input file (to follow the input format)
file_in = open('notlast.in', 'r')

# Read the first line of the file and initialize the n variable to that value
num_data = file_in.readline()
n = int(num_data)

# Delcare a counter variable as well as two lists (one for the names and one for the number of milk units in every given record)
i = 0
cow_names = []
cow_milk = []

# While the counter is less than n, populate the cow_names and cow_milk lists with all provided data
while i < n:
    cow_data = file_in.readline().split()

    temp_name = cow_data[0]
    temp_milk = int(cow_data[1])

    cow_names.append(temp_name)
    cow_milk.append(temp_milk)

    i += 1

# Declare a counter and a variable to keep track of each individual cow's total milk outputs
j = 0
bessie_milk = 0
elsie_milk = 0
daisy_milk = 0
gertie_milk = 0
annabelle_milk = 0
maggie_milk = 0
henrietta_milk = 0

# While the counter is less than n
while j < n:
	# Look at a given cow in the array and add the number of milk units that particular cow had during that milking to their respective variable
	temp_log_name = cow_names[j]

	if temp_log_name == "Bessie":
		bessie_milk += cow_milk[j]
	elif temp_log_name == "Elsie":
		elsie_milk += cow_milk[j]
	elif temp_log_name == "Daisy":
		daisy_milk += cow_milk[j]
	elif temp_log_name == "Gertie":
		gertie_milk += cow_milk[j]
	elif temp_log_name == "Annabelle":
		annabelle_milk += cow_milk[j]
	elif temp_log_name == "Maggie":
		maggie_milk += cow_milk[j]
	else:
		henrietta_milk += cow_milk[j]

	j += 1

# Delcare a final_milk list that includes the final total of milk units for each cow
final_milk = [bessie_milk, elsie_milk, daisy_milk, gertie_milk, annabelle_milk, maggie_milk, henrietta_milk]

# Declare a same variable and a counter for it
same = 0
same_count = 0

# While the counter is less than the number of possible indexes for final_milk pairs
while same_count < 6:
	# If one cow's final milk amount is the same as the cow after it, add one to the same counter
	if final_milk[same_count] == final_milk[same_count + 1]:
		same += 1
	
	same_count += 1

# If every cow's final milk total is the exact same, print "Tie" and be done
if same == 6:
	print("Tie", file = open('notlast.out', 'w'))
# Otherwise, do the rest of the code
else:
	# Declare a counter and a minimum_amount variable with a temporary value
	k = 0
	minimum_amount = 1000

	# While the counter is less than the number of possible indexes for final_milk
	while k < 7:
		# If the current final_milk value is less than the minimum_amount
		if final_milk[k] < minimum_amount:
			# Make that value the new minimum amount
			minimum_amount = final_milk[k]
		
		k += 1

	# Declare a counter and a second smallest value variable with a temporary value
	l = 0
	second_smallest = 1000

	# While the counter is less than the number of possible indexes for final_milk
	while l < 7:
		# If the given final_milk value is greater than the minimum amount but smaller than the current second_smallest amount
		if (final_milk[l] > minimum_amount) and (final_milk[l] < second_smallest):
			# Make that value the new second_smallest amount!!!
			second_smallest = final_milk[l]
		
		l += 1

	# Delcare (like the fifth) counter and a how_many / cow (final answer - we're almost there!) variables
	m = 0
	how_many = 0
	the_cow = " "

	# While the counter is less than the number of possible indexes for final_milk
	while m < 7:
		# If the given final_milk value is equal to the second_smallest value
		if final_milk[m] == second_smallest:
			# Add one to the how_many counter
			how_many += 1

			# Depending on the index value of the second_smallest value, set the final_cow to that cow
			if m == 0:
				final_cow = "Bessie"
			elif m == 1:
				final_cow = "Elsie"
			elif m == 2:
				final_cow = "Daisy"
			elif m == 3:
				final_cow = "Gertie"
			elif m == 4:
				final_cow = "Annabelle"
			elif m == 5:
				final_cow = "Maggie"
			else:
				final_cow = "Henrietta"

		m += 1

	# If the number of cows that have the second smallest value is greater than one, print "Tie" to the output file
	if how_many > 1:
		print("Tie", file = open('notlast.out', 'w'))
	# Otherwise, print the final_cow to the output file
	else:
		print(final_cow, file = open('notlast.out', 'w'))