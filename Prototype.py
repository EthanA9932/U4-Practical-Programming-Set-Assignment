'''
██╗░░░██╗░░██╗██╗██╗  ██████╗░██████╗░░█████╗░░█████╗░████████╗██╗░█████╗░░█████╗░██╗░░░░░
██║░░░██║░██╔╝██║╚═╝  ██╔══██╗██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██║██╔══██╗██╔══██╗██║░░░░░
██║░░░██║██╔╝░██║░░░  ██████╔╝██████╔╝███████║██║░░╚═╝░░░██║░░░██║██║░░╚═╝███████║██║░░░░░
██║░░░██║███████║░░░  ██╔═══╝░██╔══██╗██╔══██║██║░░██╗░░░██║░░░██║██║░░██╗██╔══██║██║░░░░░
╚██████╔╝╚════██║██╗  ██║░░░░░██║░░██║██║░░██║╚█████╔╝░░░██║░░░██║╚█████╔╝██║░░██║███████╗
░╚═════╝░░░░░░╚═╝╚═╝  ╚═╝░░░░░╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░░░░╚═╝░░░╚═╝░╚════╝░╚═╝░░╚═╝╚══════╝
██████╗░██████╗░░█████╗░░██████╗░██████╗░░█████╗░███╗░░░███╗███╗░░░███╗██╗███╗░░██╗░██████╗░
██╔══██╗██╔══██╗██╔══██╗██╔════╝░██╔══██╗██╔══██╗████╗░████║████╗░████║██║████╗░██║██╔════╝░
██████╔╝██████╔╝██║░░██║██║░░██╗░██████╔╝███████║██╔████╔██║██╔████╔██║██║██╔██╗██║██║░░██╗░
██╔═══╝░██╔══██╗██║░░██║██║░░╚██╗██╔══██╗██╔══██║██║╚██╔╝██║██║╚██╔╝██║██║██║╚████║██║░░╚██╗
██║░░░░░██║░░██║╚█████╔╝╚██████╔╝██║░░██║██║░░██║██║░╚═╝░██║██║░╚═╝░██║██║██║░╚███║╚██████╔╝
╚═╝░░░░░╚═╝░░╚═╝░╚════╝░░╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝░░░░░╚═╝╚═╝╚═╝░░╚══╝░╚═════╝░
'''

# The bottom of the python file has repository links. Show line numbers for easier locating.
# +-----------------------------------------------------------------------------------+-----------+
# |                                Primary Milestones:                                | Complete? |
# +-----------------------------------------------------------------------------------+-----------+
# | 0. Read the data from the text file.                                              |     Y     |
# | 1. Linear search the data when it is sorted.                                      |     Y     |
# | 2. Linear search the data when it is unsorted.                                    |     Y     |
# | 3. Search the data using a binary search.                                         |     Y     |
# | 4. Sort the data using a bubble sort.                                             |     Y     |
# | 5. Sort the data using a quick sort.                                              |     Y     |
# | 6. Compare the efficiency (execution time) of the different searches.             |     Y     |
# | 7. Compare the efficiency (execution time) of the different sorts.                |     Y     |
# | 8. Provide analysis for the user (most productive vendor, number of vegan hotdogs |     Y     |
# |    versus meat hotdogs supplied, vendor using the least amount of ketchup, etc.)  |           |
# | 9. Save results of analysis to an output file.                                    |     Y     |
# +-----------------------------------------------------------------------------------+           |
# |                               Secondary Milestones:                               |           |
# +-----------------------------------------------------------------------------------+           |
# | A. Allow the user to edit the variables within 'hotdogs.txt'.                     |     M     |
# | B. Allow the user to revert the hotdogs.txt file to its previous state.           |     M     |
# | C. Allow the user to reset the hotdogs.txt file to its initial state.             |     M     |
# | D. Validate each variable within the hotdogs.txt file.                            |     Y     |
# | E. Allow the user to add a new line to the hotdogs.txt file.                      |     M     |
# +-----------------------------------------------------------------------------------+-----------+

# Variable checking --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#[B]
hotdog_data = open("hotdogs.txt", "r")                                                                                                                                                                                                                          #
                                                                                                                                                                                                                                                                #
for line in hotdog_data:                                                                                                                                                                                                                                        #
    i = line.strip().split(',')                                                                                                                                                                                                                                 #
    if len(i[0]) == 6 and i[0][0].isupper() == True and i[0][1].isupper() == True and i[0][2] == "_" and i[0][3].isdigit() == True and i[0][4].isdigit() == True and i[0][5].isdigit() == True:                                                                 #
        id_check = True                                                                                                                                                                                                                                         #
    else:                                                                                                                                                                                                                                                       #
        id_check = False                                                                                                                                                                                                                                        #
                                                                                                                                                                                                                                                                #
    if len(i[1]) >= 2 and len(i[1]) <= 25:                                                                                                                                                                                                                      #
        name_check = True                                                                                                                                                                                                                                       #
    else:                                                                                                                                                                                                                                                       #
        name_check = False                                                                                                                                                                                                                                      #
                                                                                                                                                                                                                                                                #
    if len(i[2]) == 6 and i[2].isdigit() and 2000 <= int(i[2][:4]) <= 2026 and 1 <= int(i[2][4:]) <= 52:                                                                                                                                                        #
        year_week_check = True                                                                                                                                                                                                                                  #
    else:                                                                                                                                                                                                                                                       #
        year_week_check = False                                                                                                                                                                                                                                 #
                                                                                                                                                                                                                                                                #
    if isinstance(float(i[3]), float) == True and isinstance(int(i[3]) % 10, int) == True:                                                                                                                                                                      #
        v_hotdog_check = True                                                                                                                                                                                                                                   #
    else:                                                                                                                                                                                                                                                       #
        v_hotdog_check = False                                                                                                                                                                                                                                  #
                                                                                                                                                                                                                                                                #
    if isinstance(int(i[4]), int) == True and isinstance(int(i[4]) % 10, int) == True:                                                                                                                                                                          #
        m_hotdog_check = True                                                                                                                                                                                                                                   #
    else:                                                                                                                                                                                                                                                       #
        m_hotdog_check = False                                                                                                                                                                                                                                  #
                                                                                                                                                                                                                                                                #
    if isinstance(float(i[5]), float) == True and (float(i[5]) % 0.5 == 0) == True:                                                                                                                                                                             #
        onion_check = True                                                                                                                                                                                                                                      #
    else:                                                                                                                                                                                                                                                       #
        onion_check = False                                                                                                                                                                                                                                     #
                                                                                                                                                                                                                                                                #
    if isinstance(int(i[6]), int) == True and 1 <= int(i[6]) <= 4:                                                                                                                                                                                              #
        ketchup_check = True                                                                                                                                                                                                                                    #
    else:                                                                                                                                                                                                                                                       #
           ketchup_check = False                                                                                                                                                                                                                                #
                                                                                                                                                                                                                                                                #
    if id_check == False or name_check == False or year_week_check == False or v_hotdog_check == False or m_hotdog_check == False or onion_check == False or ketchup_check == False:                                                                            #
        print("\nError detected within one or more variables inside hotdogs.txt. Please undo the change or reset the data after running this code again.")                                                                                                      #
        print(f"\nVariable checks:\nID check: {id_check}\nName check: {name_check}\nYear-week check: {year_week_check}\nVegan hotdog check: {v_hotdog_check}\nMeat hotdog check: {m_hotdog_check}\nOnion check: {onion_check}\nKetchup check: {ketchup_check}") #
        exit()                                                                                                                                                                                                                                                  #
print("\nVariable checks passed, no errors detected in hotdogs.txt.")                                                                                                                                                                                           #
hotdog_data.close()                                                                                                                                                                                                                                             #
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

# Creating variables and setting up foundational information ---------------------------------------------------------------+
import time                                                                                                                 # Importing Module
available_vendors = []                                                                                                      # Initial variable assignment
for line in open("hotdogs.txt", "r"):                                                                                       # Looping through the lines in the text file
    line = line.strip().split(",")                                                                                          # Strip the line from its commas, and set it as our available vendors list.
    vendor_name = line[1]                                                                                                   #
    if vendor_name not in available_vendors:                                                                                #
        available_vendors.append(str(vendor_name))                                                                          #
print("\nAvailable vendors:\n")                                                                                             #
j = 1                                                                                                                       #
for i in available_vendors:                                                                                                 #
    print(f" {j}. {i}")                                                                                                     #   
    j += 1                                                                                                                  # Print the available vendors in a numbered list for the user to see.
search_query = str(input("\nPlease enter the name of the vendor you would like to search (2-25, or type ADMIN to edit): ")) # User inputs search query here
search_query = search_query.title()                                                                                         # Program converts input into title-case
#---------------------------------------------------------------------------------------------------------------------------+

# Looping validations for 'search_query' ---------------------------------------------------+[D]
length_check = False                                                                        #
available_check = False                                                                     #
while length_check != True or available_check != True:                                      # "While either of these variables are False, run this piece of code until they are both True."
    # Length Validaton ------------------------------------+                                #
    if len(search_query) >= 2 and len(search_query) <= 25: #                                #[C] "If the length of the search query is between the inclusive range of 2 to 25...
        length_check = True                                #                                #     "...the length check becomes True."
        # Presence Check ----+                             #                                #
    elif search_query == "": #                             #                                # "Alternatively, if nothing is inputted..."
        length_check = False #                             #                                #  "...the length check stays False."
        #--------------------+                             #                                #
    else:                                                  #                                # "If all above statements are false..."
        length_check = False                               #                                #  "...the length check is too."
    #------------------------------------------------------+                                #
    # Lookup Validation -------------------------+                                          #
    if search_query in available_vendors:        #                                          # "If the search query is found in our available vendors list..."
        available_check = True                   #                                          #  "...the avialbile check becomes True."
    #--------------------------------------------#                                          #
    if length_check != True or available_check != True:                                     # "If, after all the validations, either check is still false..."
        search_query = str(input("Vendor not found, or name out of length range (2-25): ")) #  "...tell the user to input the query again with an error message."
        search_query = search_query.title()                                                 # Converting Search_query To Title Case
    if search_query == "ADMIN": #                                                           # "If the user inputs 'ADMIN' as the search query..."
        print("Admin mode activated:") #                                                    #  "...tell the user that admin mode is activated..."
        break                                                                               #  "...and break out of the while loop early."
#-------------------------------------------------------------------------------------------#

# Array handling -----------------------+
hotdogs_data = []                       #
max_lines = 0                           #
file = open("hotdogs.txt", "r")         #
for line in file:                       #[A]
    if line.find(search_query) != -1:   # If the search query is found in the line...
        parts = line.strip().split(",") #  ...strip the line from its commas...
        hotdogs_data.append(parts)      #  ...and append it to 'hotdogs_data'
    max_lines += 1                      # This may seem incorrect, but due to the query being forced to be nearly EXACTLY how it's presented to the user (e.g. 'Dolly Dog's / 'dolly dogs')...
#---------------------------------------# ...the code can't be given an incorrect vendor name that doesn't exist.

# Admin editing ---------------------------------------------------------------------------------------------------------------------------------------------------------------------+
if search_query == "ADMIN":                                                                                                                                                          #
    print("\nAdmin options:\n 1. Edit a variable\n 2. Revert the file to its previous state\n 3. Reset the file to its initial state\n 4. Add lines")                                # Admin options shown to user
    admin_choice = str(input("Please enter the number of the admin option you would like to use: "))                                                                                 # User inputs admin choice here
    while admin_choice not in ["1", "2", "3", "4"] or admin_choice == "":                                                                                                            # Looping validation for admin choice
        admin_choice = str(input("Invalid input, please enter a valid admin option: "))                                                                                              #
    if admin_choice == "1":                                                                                                                                                          #
        line_edit = str(input(f"What line would you like to edit? (1 - {max_lines}"))                                                                                                #
        while line_edit < 1 or line_edit > max_lines or isinstance(line_edit, int) == False or line_edit == "":                                                                      #
            line_edit = str(input("Invalid input, please enter an integer in range."))                                                                                               #
                                                                                                                                                                                     #
        file = open("hotdogs.txt", "r")                                                                                                                                              #
        lines = []                                                                                                                                                                   #
        for line in file:                                                                                                                                                            #
            lines.append(line)                                                                                                                                                       #
        file.close()                                                                                                                                                                 #
        editing_line = lines[line_edit-1].strip().split(",")                                                                                                                         #
        print(f"Current line: {lines[line_edit-1]}")                                                                                                                                 #
        variable_edit = str(input("What variable would you like to edit? (1. vendor_id, 2. vendor_name, 3. year_week, 4. vegan_hotdogs, 5. meat_hotdogs, 6. onions, 7. ketchup): ")) #
        while variable_edit not in ["1", "2", "3", "4", "5", "6", "7"] or variable_edit == "" or isinstance(variable_edit, int) == False:                                            #
            variable_edit = str(input("Invalid input, please enter an integer in range: "))                                                                                          #
        if variable_edit in ["1", "2"]:                                                                                                                                              #
            new_value = str(input("What would you like to change the variable to?: "))                                                                                               #
        elif variable_edit == "3":                                                                                                                                                   #
            new_value = str(input("What would you like to change the variable to? (Format: YYYYWW, where YYYY [2000-2026]is the year and WW [01-52] is the week number): "))         #
        elif variable_edit in ["4", "5"]:                                                                                                                                            #
            new_value = str(input("What would you like to change the variable to? (Must be an integer, and a multiple of 10): "))                                                    #
        elif variable_edit == "6":                                                                                                                                                   #
            new_value = str(input("What would you like to change the variable to? (Must be a float, and divisible by 0.5): "))                                                       #
        else:                                                                                                                                                                        #
            new_value = str(input("What would you like to change the variable to? (Must be an integer between 1 and 4, inclusive): "))                                               #
                                                                                                                                                                                     #
        read_file = open("hotdogs.txt", "r")                                                                                                                                         #
        write_file = open("hotdogsMemory.txt", "w")                                                                                                                                  #
        for line in read_file:                                                                                                                                                       #
            write_file.write(line)                                                                                                                                                   #
        read_file.close()                                                                                                                                                            #
        write_file.close()                                                                                                                                                           #
                                                                                                                                                                                     #
        lines[line_edit-1] = lines[line_edit-1].strip().split(",")                                                                                                                   # This is a bit of a hack to maintain the original formatting of the line,
        lines[line_edit-1][int(variable_edit)-1] = new_value                                                                                                                         #  as the line is split into a list, then the variable is edited,
        lines[line_edit-1] = ",".join(lines[line_edit-1]) + "\n"                                                                                                                     #  then the list is joined back into a string with commas.
                                                                                                                                                                                     #
        file = open("hotdogs.txt", "w")                                                                                                                                              #
        for i in lines:                                                                                                                                                              #
            file.write(lines[lines.index(i)])                                                                                                                                        #
        file.close()                                                                                                                                                                 #
                                                                                                                                                                                     #
    elif admin_choice == "2":                                                                                                                                                        #
        input_file = open("hotdogsMemory.txt", "r")                                                                                                                                  #
        output_file = open("hotdogs.txt", "w")                                                                                                                                       #
        for line in input_file:                                                                                                                                                      #
            output_file.write(line)                                                                                                                                                  #
        input_file.close()                                                                                                                                                           #
        output_file.close()                                                                                                                                                          #
                                                                                                                                                                                     #
    elif admin_choice == "3":                                                                                                                                                        #
        input_file = open("hotdogsOrigin.txt", "r")                                                                                                                                  #
        output_file = open("hotdogs.txt", "w")                                                                                                                                       #
        for line in input_file:                                                                                                                                                      #
            output_file.write(line)                                                                                                                                                  #
        input_file.close()                                                                                                                                                           #
        output_file.close()                                                                                                                                                          #
                                                                                                                                                                                     #
    else:                                                                                                                                                                            #
        new_line_continue = str(input("Are you sure you want to add a new line to the data? (Y/N): "))                                                                               #
        while new_line_continue != "Y" and new_line_continue != "N" or new_line_continue == "":                                                                                      #
            new_line_continue = str(input("Unknown command, please enter Y or N: "))                                                                                                 #
        if new_line_continue == "N":                                                                                                                                                 #
            print("Admin choice cancelled, please run the code again to check the functionality of the data.")                                                                       #
            exit()                                                                                                                                                                   #
        if new_line_continue == "Y":                                                                                                                                                 #
            read_file = open("hotdogs.txt", "r")                                                                                                                                     #
            write_file = open("hotdogsMemory.txt", "w")                                                                                                                              #
                                                                                                                                                                                     #
            for line in read_file:                                                                                                                                                   #
                write_file.write(line)                                                                                                                                               #
            write_file.close()                                                                                                                                                       #
            read_file.close()                                                                                                                                                        #
                                                                                                                                                                                     #
            append_file = open("hotdogs.txt", "a")                                                                                                                                   #
            new_vendor_id = str(input("Enter the new vendor's ID (Format: XX_000, where X is an uppercase letter and 0 is a digit): "))                                              #        
            new_vendor_name = str(input("Enter the new vendor's name: "))                                                                                                            #
            new_year_week = str(input("Enter the year and week of the data (Format: YYYYWW, where YYYY [2000-2026] is the year and WW [01-52] is the week number): "))               #
            new_vegan_hotdogs = str(input("Enter the number of vegan hotdogs supplied (Must be an integer, and a multiple of 10): "))                                                #
            new_meat_hotdogs = str(input("Enter the number of meat hotdogs supplied (Must be an integer, and a multiple of 10): "))                                                  #
            new_onions = str(input("Enter the amount of onions supplied (Must be a float, and divisible by 0.5): "))                                                                 #
            new_ketchup = str(input("Enter the amount of ketchup supplied (Must be an integer between 1 and 4, inclusive): "))                                                       #
            append_file.write(f"{new_vendor_id},{new_vendor_name},{new_year_week},{new_vegan_hotdogs},{new_meat_hotdogs},{new_onions},{new_ketchup}\n")                              #
                                                                                                                                                                                     #
    print("Admin choice executed, please run the code again to check the functionality of the data.")                                                                                # Message to user after admin choice is executed
    exit()                                                                                                                                                                           # Exit the code after admin choice is made, as the user needs to edit
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

# Defining search algorithms ---------------------------+ 
def linear_search(items, target, hidden, request):      #[E] LINEAR SEARCH
    start_time = time.perf_counter()                    #
    index = 0                                           #
    found = False                                       #
                                                        #
    while found == False and index < len(items):        #
        if target == items[index]:                      #
            found = True                                #
        else:                                           #
            index += 1                                  #
    end_time = time.perf_counter()                      #
                                                        #
    if found == False:                                  #
        print(f"{target} not found.")                   #
    if hidden != True:                                  #
        print(f"Found {target} after {index} step(s).") #
    if request == "time":                               #
        return (end_time - start_time)                  #
    else:                                               #
        return index                                    #
                                                        #
def binary_search(items, target, hidden, request):      #[F] BINARY SEARCH:
    start_time = time.perf_counter()                    #
    found = False                                       # 
    first = 0                                           #
    last = len(items) - 1                               #
    midpoint = 0                                        #
    steps = 0                                           #
                                                        #
    while first <= last and found == False:             #
        midpoint = (first + last) / 2                   #
        if type(midpoint) == float:                     #
            midpoint += 0.5                             #
            midpoint = int(midpoint)                    #
        if items[midpoint] == target:                   #
            found = True                                #
        elif items[midpoint] < target:                  #
            first = midpoint + 1                        #
        else:                                           #
            last = midpoint - 1                         #
        steps += 1                                      #
    end_time = time.perf_counter()                      #
                                                        #
    if hidden != True:                                  #
        print(f"Found {target} after {steps} step(s).") #
    if request == "time":                               #
        return (end_time - start_time)                  #
    else:                                               #
        return steps                                    #
#-------------------------------------------------------+

# Defining sort algorithms ----------------------------------------------------------------------------------------+
def bubble_sort(items, hidden, request):                                                                           # BUBBLE SORT:
    start_time = time.perf_counter()                                                                               #
    swaps = 0                                                                                                      #
    n = len(items)                                                                                                 #
    for i in range(n):                                                                                             #
        for j in range(0, n - i - 1):                                                                              #
            if items[j] > items[j + 1]:                                                                            #
                items[j], items[j + 1] = items[j + 1], items[j]                                                    #
                swaps += 1                                                                                         #
    end_time = time.perf_counter()                                                                                 #
                                                                                                                   #
    if hidden != True:                                                                                             #
        print(f"Sorted after {swaps} swap(s).")                                                                    #
    if request == "swaps":                                                                                         #
        return swaps                                                                                               #
    if request == "time":                                                                                          #
        return (end_time - start_time)                                                                             #
    else:                                                                                                          #
        return items                                                                                               #
                                                                                                                   #
def quick_sort(items, hidden, request):                                                                            # QUICK SORT:
    start_time = time.perf_counter()                                                                               #
    swaps = 0                                                                                                      #
    if len(items) <= 1:                                                                                            #
        return items                                                                                               #
    pivot = items[len(items) // 2]                                                                                 #
    left = [x for x in items if x < pivot]                                                                         #
    swaps += len(left)                                                                                             #
    middle = [x for x in items if x == pivot]                                                                      #
    swaps += len(middle)                                                                                           #
    right = [x for x in items if x > pivot]                                                                        #
    swaps += len(right)                                                                                            #
    end_time = time.perf_counter()                                                                                 #
                                                                                                                   #
    if hidden != True:                                                                                             #
        print(f"Sorted after {swaps} swap(s).")                                                                    #
    if request == "swaps":                                                                                         #
        return swaps                                                                                               #
    if request == "time":                                                                                          #
        return (end_time - start_time)                                                                             #
    else:                                                                                                          #
        return quick_sort(left, hidden=True, request=None) + middle + quick_sort(right, hidden=True, request=None) #
#------------------------------------------------------------------------------------------------------------------+ 

# User-inputted category search ----------------------------------------------------------------------------------------------------------------+
query_check = False                                                                                                                             # Initial boolean assignment
print("\nAvailable categories:\n 1. vendor_id\n 2. vendor_name\n 3. year_week\n 4. vegan_hotdogs\n 5. meat_hotdogs\n 6. onions\n 7. ketchup\n") #
while query_check != True:                                                                                                                      # While loop begun
    try:                                                                                                                                        # Try command used to prevent errors
        user_search = int(input("What category would you like to search the data in? (Enter a number from 1 to 7): "))                          # Ask user to input an INTEGER from 1 to 7, inclusive
        for i in [0, len(hotdogs_data)]:                                                                                                        #
            while user_search < 1 or user_search > 7 or user_search == "":                                                                      #
                user_search = int(input("Category not found, ensure input is within range: "))                                                  #
        if user_search > 1 or user_search < 7:                                                                                                  #
           query_check = True                                                                                                                   #
    except ValueError:                                                                                                                          # Except error called to stop code crash
        print("Input is not an integer.")                                                                                                       #
#-----------------------------------------------------------------------------------------------------------------------------------------------+

# Filtering data -------------------------------------------------------------+
def filter_scraper(target_filter, vendor_name, hotdogs_data, hidden):         #
    file = open("hotdogs.txt", "r")                                           #
    items = []                                                                #
    i = 0                                                                     #
    for line in file:                                                         #
        i += 1                                                                #
        segment = []                                                          #
        line = line.strip().split(",")                                        #
        if vendor_name in line:                                               #
            segment = line[target_filter-1]                                   #
            items.append(segment)                                             #
    if not hidden:                                                            #
        print(f"{target_filter} for {vendor_name}: {items}")                  #
    file.close()                                                              #
    return items                                                              #
                                                                              #
items = filter_scraper(user_search, search_query, hotdogs_data, hidden=False) #
#-----------------------------------------------------------------------------+

# Sorting if wanted ----------------------------------------------------------------------------------------------------+
sort_input = str(input("\nWould you like to sort the data before searching? (Y/N): "))                                  #
sort_options = ["Bubble Sort", "Quick Sort"]                                                                            #
while sort_input != "Y" and sort_input != "N" or sort_input == "":                                                      #
    sort_input = str(input("Invalid input, please enter Y or N: "))                                                     #
if sort_input == "Y":                                                                                                   #
    sort_choice = str(input(f"Which sorting algorithm would you like to use? ({sort_options[0]}/{sort_options[1]}): ")) #
    while sort_choice not in sort_options or sort_choice == "":                                                         #
        sort_choice = str(input("Invalid input, please enter a valid sorting algorithm: "))                             #
    if sort_choice == sort_options[0]:                                                                                  #
        items = bubble_sort(items, hidden=False, request="items")                                                       #
    else:                                                                                                               #
        items = quick_sort(items, hidden=False, request="items")                                                        #
#-----------------------------------------------------------------------------------------------------------------------+

# Searching ----------------------------------------------------------------------------------------------------------------+
target = str(input("What is your search query?: "))                                                                         #
while target not in items or target == "":                                                                                  #
    target = str(input("Query not found, please enter a valid query: "))                                                    #
                                                                                                                            #
search_options = ["Linear Search", "Binary Search"]                                                                         #
search_choice = str(input(f"Which searching algorithm would you like to use? ({search_options[0]}/{search_options[1]}): ")) #
while search_choice not in search_options or search_choice == "":                                                           #
    search_choice = str(input("Invalid input, please enter a valid searching algorithm: "))                                 #
if search_choice == search_options[0]:                                                                                      #
    linear_search(items, target, False, "placeholder")                                                                      #
else:                                                                                                                       #
    print("WARNING: Binary Search requires sorting before it is used.")                                                     # This warning is put in place because binary sort requires a sorted list.
    binary_search(items, target, False, "placeholder")                                                                      #
#---------------------------------------------------------------------------------------------------------------------------+

# Secondary variable association --------------------------------------+
v_hotdogs = filter_scraper(4, search_query, hotdogs_data, hidden=True) #
total_v_hotdogs = 0                                                    #
for i in v_hotdogs:                                                    #
    total_v_hotdogs += int(i)                                          #
                                                                       #
m_hotdogs = filter_scraper(5, search_query, hotdogs_data, hidden=True) #
total_m_hotdogs = 0                                                    #
for i in m_hotdogs:                                                    #
    total_m_hotdogs += int(i)                                          #
                                                                       #
onions = filter_scraper(6, search_query, hotdogs_data, hidden=True)    #
total_onions = 0                                                       #
for i in onions:                                                       #
    total_onions += float(i)                                           #
                                                                       #
ketchup = filter_scraper(7, search_query, hotdogs_data, hidden=True)   #
total_ketchup = 0                                                      #
for i in ketchup:                                                      #
    total_ketchup += int(i)                                            #
                                                                       #
file.close()                                                           #
#----------------------------------------------------------------------+

# Background algorithms hidden from user ---------------------------------------+
items = filter_scraper(user_search, search_query, hotdogs_data, hidden=True)    # Resetting items to original state
                                                                                #
linear_steps = linear_search(items, target, hidden=True, request="placeholder") # Sorting for binary search
bubble_sort(items, hidden=True, request="placeholder")                          #
binary_steps = binary_search(items, target, hidden=True, request="placeholder") # Searching with binary_search algorithm
                                                                                #
items = filter_scraper(user_search, search_query, hotdogs_data, hidden=True)    # Resetting items to original state
bubble_swaps = bubble_sort(items, hidden=True, request="swaps")                 #
quick_swaps = quick_sort(items, hidden=True, request="swaps")                   #
#-------------------------------------------------------------------------------+

# Analysis output! =========================================================================================================================================================================+
file = open("analysis.txt", "w")                                                                                                                                                            # Opening file
file.write("Analysis of hotdog data:\n")                                                                                                                                                    # Start of analysis file
file.write(f"Vendor searched: {search_query}\n")                                                                                                                                            # This line is from the search query of the user.
                                                                                                                                                                                            #
file.write(f"Number of vegan hotdogs supplied: {total_v_hotdogs}\n")                                                                                                                        # These four lines are
file.write(f"Number of meat hotdogs supplied: {total_m_hotdogs}\n")                                                                                                                         # from the variable
file.write(f"Total amount of onions supplied: {total_onions}\n")                                                                                                                            # association section, where
file.write(f"Total amount of ketchup supplied: {total_ketchup}\n")                                                                                                                          # the data is totalled up.
file.write(f"-------------------------------------------------------\n")                                                                                                                    #
file.write(f"Algorithm comparisons:\n")                                                                                                                                                     #
file.write(f"Linear search found {target} in {linear_steps} steps, and took {(linear_search(items, target, hidden=True, request="time")*1000000):.2f} microseconds.\n")                 # These four lines are from the
file.write(f"Binary search, after sorting, found {target} in {binary_steps} steps, and took {binary_search(items, target, hidden=True, request="time")*1000000:.2f} microseconds.\n") # previous section with the
file.write(f"Bubble sort sorted {len(items)} items in {bubble_swaps} steps, and took {bubble_sort(items, hidden=True, request="time")*1000000:.2f} microseconds.\n")                        # hidden algorithms simulating
file.write(f"Quick sort sorted {len(items)} items in {quick_swaps} steps, and took {quick_sort(items, hidden=True, request="time")*1000000:.2f} microseconds.\n")                           # the algorithms
file.close()                                                                                                                                                                                #
#===========================================================================================================================================================================================+

# +------------------+
# | Repository Links |
# +------------------+
# | Line 101 - [A]   |
# | Line 102 - [B]   |
# | Line 053 - [C]   |
# | Line 048 - [D]   |
# | Line 156 - [E]   |
# | Line 177 - [F]   |
# | Line ??? - [?]   | this requirement row is only for place-holder purposes
# +------------------+

'''
Description of admin options:

1. EDITING
  - Hotdogs.txt is copied to HotdogsMemory.txt
  - User inputs the new value for the variable
  - Edit is made to Hotdogs.txt

2. REVERTING
  - HotdogsMemory.txt is copied to Hotdogs.txt

3. RESETTING
  - HotdogsOrigin.txt is copied to Hotdogs.txt
'''
