# Why Did the Cow Cross the Road III
# Seneca Howell
# Computational Foundations 2 - Spring 2023
# Recitation 011

# Opens the input file (to follow the input format)
file_in = open("cowqueue.in", "r")

# Reads the first line of the file (with the lovely value of n on it) and assigns that value to my n variable (so cool)
num_data = file_in.readline()
n = int(num_data)

# Intializes a counter and two lists (one for the time the cows enter at and one for the durations)
i = 0
cow_enter = []
cow_duration = []

# Populate both lists with the given data
while i < n:
    cow_data = file_in.readline().split()

    temp_enter = int(cow_data[0])
    temp_duration = int(cow_data[1])

    cow_enter.append(temp_enter)
    cow_duration.append(temp_duration)

    i += 1
  
# Declare a been_processed boolean list
been_processed = []

# Populate the been_processed list with False (default values)
c = 0
while c < n:
    been_processed.append(False)
    c += 1

# Declare a time variable
time = 0

# While a counter is less than n
j = 0
while j < n:
    # Declare a next to enter variable
    next_to_enter = -1

    # While a counter is less than n
    k = 0
    while k < n:
        # If been_processed is false at the given index and next_to_enter is -1 (first iteration) or the given cow_enter is less than next to enter
        if (not(been_processed[k]) and (next_to_enter == -1 or cow_enter[k] < cow_enter[next_to_enter])):
            # Make that value the next next to enter (double next)
            next_to_enter = k
        k += 1
    
    # Set that index in the been_processed list to true
    been_processed[next_to_enter] = True

    # If the value at next_to_enter is greater than the time
    if(cow_enter[next_to_enter] > time):
        # Set time to the time the cow enters plus the amount of time the cow spends
        time = cow_enter[next_to_enter] + cow_duration[next_to_enter]
    # Otherwise, set time to the current time plus the amount of time the cow spends
    else:
        time = time + cow_duration[next_to_enter]

    j += 1

# Print the final time to the output file
print(time, file=open('cowqueue.out', 'w'))