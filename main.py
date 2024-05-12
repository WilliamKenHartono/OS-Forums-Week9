import random as rand

# A hard-drive disk has 5,000 cylinders numbered 0 to 4,999. Write a program that implements
# the following disk-scheduling algorithms:
# a. FCFS
# b. SCAN
# c. C-SCAN
# The program will read from the text file a random series of 1,000 cylinder requests and service
# them according to each of the algorithms listed above. The program will be passed the initial
# position of the disk head and a text file (as the parameters on the command line).

# Constants
REQUEST_COUNT = 20
MIN_INT = 0
MAX_INT = 4999

# File outputs
disk = 'disk.txt'
fcfs_optimized_disk = 'fcfs_optimized_disk.txt'
scan_optimized_disk = 'scan_optimized_disk.txt'
cscan_optimized_disk = 'cscan_optimized_disk.txt'

# Generates random numbers with no empty spaces
def producer():
    output_file = open(disk, 'w')
    for i in range(REQUEST_COUNT):
        num = rand.randint(MIN_INT, MAX_INT)
        output_file.writelines(f'{num}')
        if i < REQUEST_COUNT-1:
            output_file.writelines('\n')
    output_file.close()


# First Come First Serve Scheduling
def FCFS(var_list, head):
    # Where the algorithm starts
    head_distance_total = 0
    for i in range(len(var_list)):
        curr_position = var_list[i]
        # Absolute distance calculator so there are no negative numbers
        distance = abs(curr_position - head)
        head_distance_total += distance
        # curr_position replaces head to keep algorithm going
        head = curr_position

    print(f'Total amount of head movements for FCFS is: {head_distance_total}')

# SCAN algorithm Scheduling
def SCAN(var_list, head, direction):
    distance = 0
    # curr_position set to 0 to errorproof code
    curr_position = 0
    # Seperate left and right variables for easier calculation
    left = []
    right = []
    head_distance_total = 0
    # service order for testing 
    # service_order = []

    # if initial direction is left, it will continue till it reaches 0, if initial direction is right, it will continue scanning till it reaches the end of the line in the txt files  
    if direction == "left":
        left.append(0)
    elif direction == "right":
        right.append(REQUEST_COUNT-1)

    # appends everything thats in the left and right side of the list into a seperate list
    for i in range(len(var_list)):
        if var_list[i] < head:
            left.append(var_list[i])
        if (var_list[i] > head):
            right.append(var_list[i])
    
    # Sorts both lists to make distance calculation easier
    left.sort()
    right.sort()

    # Ensures the following code loops only twice
    loop_counter = 2
    while loop_counter != 0:
        if direction == "left":
            # starts from the end of the left list and counts down to the start of the left list
            for i in range(len(left) -1, -1, -1):
                curr_position = left[i]
                
                # for testing purposes
                # service_order.append(curr_position)

                distance = abs(curr_position - head)

                head_distance_total += distance

                head = curr_position
            direction = "right"
        elif direction == "right":
            for i in range(len(right)):
                curr_position = right[i]

                # For testing
                # service_order.append(curr_position)

                distance = abs(curr_position - head)

                head_distance_total += distance

                head = curr_position
            direction = "left"
        
        loop_counter -= 1
    
    print(f'Total amount of head movements for SCAN is: {head_distance_total}')
    # print(f'Service Order SCAN: {service_order}')

# CSCAN algorithm
def CSCAN(var_list, head):
    distance = 0
    # curr_position set to 0 to errorproof code
    curr_position = 0
    # Seperate left and right variables for easier calculation
    left = []
    right = []

    # testing purposes

    # service_order = []

    head_distance_total = 0
    # initial direction of C-SCAN does not matter
    left.append(0)
    right.append(REQUEST_COUNT-1)

    for i in range(len(var_list)):
        if var_list[i] < head:
            left.append(var_list[i])
        if var_list[i] > head:
            right.append(var_list[i])
    
    left.sort()
    right.sort()

    for i in range(len(right)):
        curr_position = right[i]

        # Testing purposes
        # service_order.append(curr_position)

        distance = abs(curr_position - head)

        head_distance_total += distance

        head = curr_position
    
    head = 0


    head_distance_total += (REQUEST_COUNT - 1)

    # Counts variables from left to the initial head
    for i in range(len(left)):
        curr_position = left[i]

        # Testing purposes
        # service_order.append(curr_position)

        distance = abs(curr_position - head)

        head_distance_total += distance

        head = curr_position
    print(f'Total amount of head movements for C-SCAN is: {head_distance_total}')

    # print(f'Service Order C-SCAN: {service_order}')

# List Optimization

def closest(lst, number):
    # returns variable with minimum difference after finding every number's absolute difference with the number variable
    return lst[min(range(len(lst)), key = lambda i: abs(lst[i]-number))]

def FCFSlist(head):
    temp_list = []
    opti_list = []

    with open(disk) as file:
        for line in file:
            temp_list.append(int(line))

    for i in range(len(temp_list)):
        nearest_num = closest(temp_list, head)
        opti_list.append(nearest_num)
        head = nearest_num
        temp_list.remove(nearest_num)
    
    output_file = open(fcfs_optimized_disk, 'w')
    for i in range(len(opti_list)):
        output_file.writelines(f'{opti_list[i]}')
        if i < REQUEST_COUNT-1:
            output_file.writelines('\n')
    output_file.close()

    # print(f'Closest is: {opti_list}')
    return opti_list
    
def SCANlist(head, direction):
    temp_list = []
    opti_list = []
    left = []
    right = []

    with open(disk) as file:
        for line in file:
            temp_list.append(int(line))
    
    for i in range(len(temp_list)):
        if temp_list[i] < head:
            left.append(temp_list[i])
        if temp_list[i] > head:
            right.append(temp_list[i])

    if direction == left:
        left.sort()
        right.sort(reverse=True)
    elif direction == right:
        right.sort()
        left.sort(reverse=True)

    for i in range(len(left)):
        opti_list.append(left[i])
    for i in range(len(right)):
        opti_list.append(right[i])
    
    output_file = open(scan_optimized_disk, 'w')
    for i in range(len(temp_list)):
        output_file.writelines(f'{temp_list[i]}')
        if i < REQUEST_COUNT-1:
            output_file.writelines('\n')
    output_file.close()

    # print(opti_list)
    return opti_list

def CSCANlist(head):
    temp_list = []
    opti_list = []
    left = []
    right = []

    with open(disk) as file:
        for line in file:
            temp_list.append(int(line))
    
    for i in range(len(temp_list)):
        if temp_list[i] < head:
            left.append(temp_list[i])
        if temp_list[i] > head:
            right.append(temp_list[i])
    left.sort()
    right.sort()

    for i in range(len(right)):
        opti_list.append(right[i])
    for i in range(len(left)):
        opti_list.append(left[i])
    

    output_file = open(cscan_optimized_disk, 'w')
    for i in range(len(temp_list)):
        output_file.writelines(f'{temp_list[i]}')
        if i < REQUEST_COUNT-1:
            output_file.writelines('\n')
    output_file.close()
    # print(opti_list)
    return opti_list

# Main
if __name__ == '__main__':
    # Creates TXT for the list of numbers
    producer()

    # Convert TXT to list
    var_list = []
    with open(disk) as file:
        for line in file:
            var_list.append(int(line))

    # For all initial disk positions, I will assume the initial disk position is the variable below
    head = 3000

    
    dist_to_start = head
    dist_to_end = abs(REQUEST_COUNT-head)

    # Assuming initial direction is towards innermost of list
    # if dist_to_start < dist_to_end:
    #     direction = "left"
    # elif dist_to_end < dist_to_start:
    #     direction = "right"
    direction = "left"

    FCFS(var_list, head)

    SCAN(var_list, head, direction)

    CSCAN(var_list, head)

    # Optimized version of the lists

    opti_fcfs_list = FCFSlist(head)
    FCFS(opti_fcfs_list, head)

    opti_scan_list = SCANlist(head, direction)
    SCAN(opti_scan_list, head, direction)

    opti_cscan_list = CSCANlist(head)
    CSCAN(opti_cscan_list, head)
    

