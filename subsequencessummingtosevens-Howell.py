# Subsequences Summing to Sevens
# Seneca Howell
# Computational Foundations 2 - Spring 2023
# Recitation 011

# Read in the given data (as provided)
with open('div7.in') as read:
	cows = [int(read.readline()) for _ in range(int(read.readline()))]

# Declare the variable that will the store the number of cows in the largest group
largest_group = 0

# Declare a list for the prefix sum
prefix = []

# While the counter is less than the length of the cows list
p_count = 0
while p_count < len(cows):
    # Add the given cow's ID to the prefix list
    prefix.append(cows[p_count])
    p_count += 1

# Add a one to the end of the prefix list
prefix.append(1)

# While the counter is less than the length of the cows list
i = 0
while i < len(cows):
    # Calculate the prefix sum, modulus seven
    prefix[i + 1] = (prefix[i] + cows[i]) % 7
    i += 1

# Declare the last_found list
last_found = []

# While the counter is less than 7
k = 0
while k < 7:
    # Fill the list with -1
    last_found.append(-1)
    k += 1

# While the counter is less than the length of the prefix list
l = 0
while l < len(prefix):
    # If the given value has already been found
    if last_found[prefix[l]] == -1:
        # Assign it to the current index
        last_found[prefix[l]] = l
    # Otherwise (there is a number with the same prefix value previously)
    else:
        # Make the new maximum the max of the size and itself
        largest_group = max(l - last_found[prefix[l]], largest_group)

    l += 1

# Print our output to the given file
print(largest_group, file=open('div7.out', 'w'))