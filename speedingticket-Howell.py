# Speeding Ticket
# Seneca Howell
# Computational Foundations 2 - Spring 2023
# Recitation 011

# Opens the input file (to follow the input format)
file_in = open("speeding.in", "r")

# Reads the first line of the file to get the really cool number of road segments and Bessie segments
n_and_m = file_in.readline().split()
n_road_segments = int(n_and_m[0])
m_bessie_segments = int(n_and_m[1])

# Declares a list for the speed limits
speed_limit_list = []

# While the counter is less than the number of road segments
i = 0
while i < n_road_segments:
    # Read the line and store the length of that segment and the speed limit for that segment
    road_info = file_in.readline().split()
    road_length = int(road_info[0])
    road_speed = int(road_info[1])

    # While the counter is less than the length of the road segment
    j = 0
    while j < road_length:
        # Add that speed limit to the speed limit list
        speed_limit_list.append(road_speed)
        # Don't forget to add to the counter so we don't get stuck on a while loop carousel!
        j += 1

    # Don't forget to add to the counter so we don't get stuck on a while loop carousel, part two!
    i += 1

# Declares a list for the speeds bessie is going
bessie_speed_list = []

# While the counter is less than the number of Bessie speed segments
k = 0
while k < m_bessie_segments:
    # Read the line and store the length of that segment and the speed she was going for that segment
    bessie_info = file_in.readline().split()
    bessie_length = int(bessie_info[0])
    bessie_speed = int(bessie_info[1])

    # While the counter is less than the length of the segment
    l = 0
    while l < bessie_length:
        # Add that speed to the Bessie speed list
        bessie_speed_list.append(bessie_speed)
        # Don't forget to add to the counter so we don't get stuck on a while loop carousel, part three!
        l += 1

    # Don't forget to add to the counter so we don't get stuck on a while loop carousel, part four!
    k += 1

# Initialize the max_over_limit variable
max_over_limit = 0

# While the counter is less than 100
o = 0
while o < 100:
    # Calculate how much Bessie was over (amount_over_limit) by subtracting the actual speed limit from the speed Bessie was going
    amount_over_limit = bessie_speed_list[o] - speed_limit_list[o]

    # If the amount she went over the limit is greater than the current max over the limit, make that number the new max
    if amount_over_limit > max_over_limit:
        max_over_limit = amount_over_limit
    
    # Don't forget to add to the counter so we don't get stuck on a while loop carousel, part five!
    o += 1

# Writes the max over the limit to the output file and closes it
print(max_over_limit, file = open('speeding.out', 'w'))