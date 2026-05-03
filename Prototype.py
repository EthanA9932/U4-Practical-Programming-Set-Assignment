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
# | A. Allow the user to edit the variables within 'hotdogs.txt'.                     |     Y     |
# | B. Allow the user to revert the hotdogs.txt file to its previous state.           |     Y     |
# | C. Allow the user to reset the hotdogs.txt file to its initial state.             |     Y     |
# | D. Validate each variable within the hotdogs.txt file.                            |     Y     |
# | E. Allow the user to add a new line to the hotdogs.txt file.                      |     Y     |
# +-----------------------------------------------------------------------------------+-----------+

# Global filename variable
filename = "hotdogs.txt"

def check_file_integrity(filename):
    """
    Checks the integrity of the first line in the hotdogs.txt file.
    Returns (True, "success message") if valid, (False, "error message") if invalid.
    """
    try:
        with open(filename, 'r') as file:
            first_line = file.readline().strip()
            if not first_line:
                return False, "File is empty"
            
            parts = first_line.split(',')
            if len(parts) != 7:
                return False, "Incorrect number of fields (expected 7)"
            
            # Check vendor_id: XX_000 format
            if not (len(parts[0]) == 6 and parts[0][:2].isupper() and parts[0][2] == '_' and parts[0][3:].isdigit()):
                return False, "Invalid vendor_id format (expected XX_000)"
            
            # Check vendor_name: 2-25 characters
            if not (2 <= len(parts[1]) <= 25):
                return False, "Invalid vendor_name length (expected 2-25 characters)"
            
            # Check year_week: YYYYWW format, year 2000-2026, week 01-52
            if not (len(parts[2]) == 6 and parts[2].isdigit() and 2000 <= int(parts[2][:4]) <= 2026 and 1 <= int(parts[2][4:]) <= 52):
                return False, "Invalid year_week format (expected YYYYWW with valid year/week)"
            
            # Check vegan_hotdogs: integer multiple of 10
            try:
                v = int(parts[3])
                if v % 10 != 0:
                    return False, "Vegan hotdogs not a multiple of 10"
            except ValueError:
                return False, "Invalid vegan_hotdogs (expected integer)"
            
            # Check meat_hotdogs: integer multiple of 10
            try:
                m = int(parts[4])
                if m % 10 != 0:
                    return False, "Meat hotdogs not a multiple of 10"
            except ValueError:
                return False, "Invalid meat_hotdogs (expected integer)"
            
            # Check onions: float multiple of 0.5
            try:
                o = float(parts[5])
                if o % 0.5 != 0:
                    return False, "Onions not a multiple of 0.5"
            except ValueError:
                return False, "Invalid onions (expected float)"
            
            # Check ketchup: integer 1-4
            try:
                k = int(parts[6])
                if not (1 <= k <= 4):
                    return False, "Ketchup out of range (expected 1-4)"
            except ValueError:
                return False, "Invalid ketchup (expected integer 1-4)"
            
            return True, "File integrity check passed"
    except FileNotFoundError:
        return False, "File not found"
    except Exception as e:
        return False, f"Error reading file: {e}"

def validate_all_lines(hotdog_data, filename):
    """
    Validates all lines in the hotdog data file.
    Checks each field against required format and constraints.
    Exits with error if validation fails, otherwise closes file and returns success.
    """

    for line in hotdog_data:
        fields = line.strip().split(',')

        checks = []

        for index, value in enumerate(fields):
            match index:
                case 0:  # ID
                    checks.append(
                        len(value) == 6
                        and value[0].isupper()
                        and value[1].isupper()
                        and value[2] == "_"
                        and value[3:].isdigit()
                    )

                case 1:  # Name
                    checks.append(2 <= len(value) <= 25)

                case 2:  # Year-week
                    checks.append(
                        len(value) == 6
                        and value.isdigit()
                        and 2000 <= int(value[:4]) <= 2026
                        and 1 <= int(value[4:]) <= 52
                    )

                case 3:  # Vegan hotdog count
                    checks.append(
                        value.replace('.', '', 1).isdigit()
                        and float(value) % 10 == 0
                    )

                case 4:  # Meat hotdog count
                    checks.append(
                        value.isdigit()
                        and int(value) % 10 == 0
                    )

                case 5:  # Onion amount
                    try:
                        f = float(value)
                        checks.append(f % 0.5 == 0)
                    except ValueError:
                        checks.append(False)

                case 6:  # Ketchup level
                    checks.append(
                        value.isdigit()
                        and 1 <= int(value) <= 4
                    )

                case _:  # Unexpected extra fields
                    checks.append(False)

        # If any check failed
        if not all(checks):
            print(f"\nError detected within one or more variables inside {filename}. Undoing change...")

            with open("hotdogsMemory.txt", "r") as input_file, open(filename, "w") as output_file:
                for old_line in input_file:
                    output_file.write(old_line)

            print("\nVariable checks:")
            print(f"ID check: {checks[0]}")
            print(f"Name check: {checks[1]}")
            print(f"Year-week check: {checks[2]}")
            print(f"Vegan hotdog check: {checks[3]}")
            print(f"Meat hotdog check: {checks[4]}")
            print(f"Onion check: {checks[5]}")
            print(f"Ketchup check: {checks[6]}")
            exit()

    print(f"\nVariable checks passed, no errors detected in {filename}.")
    hotdog_data.close()

# Variable checking --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#[B]
import os

file_found = False
while not file_found:
    filename = input("Enter the filename to open (default: hotdogs.txt): ").strip()
    if filename == "":
        filename = "hotdogs.txt"
    
    if os.path.exists(filename):
        # Perform file integrity check on the first line
        integrity_passed, integrity_message = check_file_integrity(filename)
        if integrity_passed:
            try:
                hotdog_data = open(filename, "r")
                file_found = True
                print(f"File '{filename}' found and opened successfully.\n{integrity_message}\n")
            except IOError as e:
                print(f"Error opening {filename}: {e}\n")
        else:
            print(f"File integrity check failed: {integrity_message}\nPlease try again.\n")
    else:
        print(f"Error: {filename} file not found. Please try again.\n")
                                                                                                                                                                                                                                                                #
validate_all_lines(hotdog_data, filename)
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

# Creating variables and setting up foundational information ---------------------------------------------------------------+
import time                                                                                                                 # Importing Module
available_vendors = []                                                                                                      # Initial variable assignment
for line in open(filename, "r"):                                                                                             # Looping through the lines in the text file
    line = line.strip().split(",")                                                                                          # Strip the line from its commas, and set it as our available vendors list.
    vendor_name = line[1]                                                                                                   # Vendor name is the 2nd item in the list
    if vendor_name not in available_vendors:                                                                                # If vendor_name is not already in available_vendors:
        available_vendors.append(str(vendor_name))                                                                          # |Append the vendor name to the list
print("\nAvailable vendors:\n")                                                                                             # Prints header
j = 1                                                                                                                       # Creates variable to make print message
for i in available_vendors:                                                                                                 # For every item in available_vendors:
    print(f" {j}. {i}")                                                                                                     # |Print j, then i
    j += 1                                                                                                                  # Print the available vendors in a numbered list for the user to see.
available_vendors.append("Admin")                                                                                           # Adding "Admin" as an available vendor for the user to search, which will allow them to edit the data.
search_query = str(input("\nPlease enter the name of the vendor you would like to search (2-25, or type Admin to edit): ")) # User inputs search query here
search_query = search_query.title()                                                                                         # Program converts input into title-case
#---------------------------------------------------------------------------------------------------------------------------+

# Looping validations for 'search_query' ---------------------------------------------------+[D]
length_check = False                                                                        #
available_check = False                                                                     #
while length_check != True or available_check != True:                                      # "While either of these variables are False, run this piece of code until they are both True."
                                                                                            # Reset available_check at the start of each iteration
    available_check = False                                                                 #
    # Length Validaton ------------------------------------+                                #
    if len(search_query) >= 2 and len(search_query) <= 25: #                                #[C] "If the length of the search query is between the inclusive range of 2 to 25...
        length_check = True                                #                                #    |"...the length check becomes True."
        # Presence Check ----+                             #                                #
    elif search_query == "": #                             #                                # "Alternatively, if nothing is inputted..."
        length_check = False #                             #                                # |"...the length check stays False."
        #--------------------+                             #                                #
    else:                                                  #                                # "If all above statements are false..."
        length_check = False                               #                                # |"...the length check is too."
    #------------------------------------------------------+                                #
    # Lookup Validation -------------------------+                                          #
    if search_query in available_vendors:        #                                          # "If the search query is found in our available vendors list..."
        available_check = True                   #                                          # |"...the avialbile check becomes True."
    #--------------------------------------------#                                          #
    if search_query == "Admin":                                                             # "If the user inputs 'ADMIN' as the search query..."
        print("Admin mode activated:")                                                      # |"...tell the user that admin mode is activated..."
        available_check = True                                                              # |"...set available_check to True and break..."
        break                                                                               # |"...and break out of the while loop early."
    if length_check != True or available_check != True:                                     # "If, after all the validations, either check is still false..."
        search_query = str(input("Vendor not found, or name out of length range (2-25): ")) # |"...tell the user to input the query again with an error message."
        search_query = search_query.title()                                                 # Converting Search_query To Title Case
#-------------------------------------------------------------------------------------------#

# Array handling -----------------------+
hotdogs_data = []                       # Creates hotdog_data list
max_lines = 0                           # Initialises lines cap variable
file = open(filename, "r")              # Opens hotdogs file
for line in file:                       #[A]
    if line.find(search_query) != -1:   # If the search query is found in the line...
        parts = line.strip().split(",") # |...strip the line from its commas...
        hotdogs_data.append(parts)      # |...and append it to 'hotdogs_data'
    max_lines += 1                      # This may seem incorrect, but due to the query being forced to be nearly EXACTLY how it's presented to the user (e.g. 'Dolly Dog's / 'dolly dogs')...
#---------------------------------------# |...the code can't be given an incorrect vendor name that doesn't exist.

# Admin editing ---------------------------------------------------------------------------------------------------------------------------------------------------------------------+
if search_query == "Admin":                                                                                                                                                          #
    print("\nAdmin options:\n 1. Edit a variable\n 2. Revert the file to its previous state\n 3. Reset the file to its initial state\n 4. Add lines")                                # Admin options shown to user
    admin_choice = str(input("Please enter the number of the admin option you would like to use: "))                                                                                 # User inputs admin choice here
    while admin_choice not in ["1", "2", "3", "4"] or admin_choice == "":                                                                                                            # Checking input for admin option
        admin_choice = str(input("Invalid input, please enter a valid admin option: "))                                                                                              # Prints error message if unknown option entered
    if admin_choice == "1":                                                                                                                                                          # If admin option is "1":
        line_edit = int(input(f"What line would you like to edit? (1 - {max_lines}): "))                                                                                             # |Asks user what line they'd like to edit, uses max_lines from, earlier
        while line_edit < 1 or line_edit > max_lines or isinstance(line_edit, int) == False or line_edit == "":                                                                      # |Checks if integer is not in range of 1 to lines cap
            line_edit = str(input("Invalid input, please enter an integer in range: "))                                                                                              # | If not, then asks user again for input
                                                                                                                                                                                     # |
        file = open(filename, "r")                                                                                                                                                 # |Opens hotdogs file
        lines = []                                                                                                                                                                   # |Creates empty list
        for line in file:                                                                                                                                                            # |For every line in file:
            lines.append(line)                                                                                                                                                       # | Append the line to the line list
        file.close()                                                                                                                                                                 # |The editing line is equal to the nth index of the list, where n is line_edit
        editing_line = lines[line_edit-1].strip().split(",")                                                                                                                         # |Strips line to be edited
        print(f"Current line: {lines[line_edit-1]}")                                                                                                                                 # |Prints line selected
        variable_edit = int(input("What variable would you like to edit? (1. vendor_id, 2. vendor_name, 3. year_week, 4. vegan_hotdogs, 5. meat_hotdogs, 6. onions, 7. ketchup): ")) # |Asks user for input on which variable to edit within stripped line
        while variable_edit not in [1, 2, 3, 4, 5, 6, 7] or variable_edit == "" or isinstance(variable_edit, int) == False:                                                          # |If integer input is not 1, 2, 3, 4, 5, 6, 7, or if the input is not an integer:
            variable_edit = int(input("Invalid input, please enter an integer in range: "))                                                                                          # | Asks user again for valid input
        if variable_edit in [1, 2]:                                                                                                                                                  # |Consecutive checks of input
            new_value = str(input("What would you like to change the variable to?: "))                                                                                               # |
        elif variable_edit == 3:                                                                                                                                                     # |
            new_value = int(input("What would you like to change the variable to? (Format: YYYYWW, where YYYY [2000-2026] is the year and WW [01-52] is the week number): "))        # |
        elif variable_edit in [4, 5]:                                                                                                                                                # |
            new_value = int(input("What would you like to change the variable to? (Must be an integer, and a multiple of 10): "))                                                    # |
        elif variable_edit == 6:                                                                                                                                                     # |
            new_value = float(input("What would you like to change the variable to? (Must be a float, and divisible by 0.5): "))                                                     # |
        else:                                                                                                                                                                        # |
            new_value = int(input("What would you like to change the variable to? (Must be an integer between 1 and 4, inclusive): "))                                               # |
                                                                                                                                                                                     # |
        read_file = open(filename, "r")                                                                                                                                         # |Opens hotdogs file in read mode
        write_file = open("hotdogsMemory.txt", "w")                                                                                                                                  # |Opens hotdogsMemory file in write mode
        for line in read_file:                                                                                                                                                       # |Writes every line from reading file to writing file, saving it
            write_file.write(line)                                                                                                                                                   # |
        read_file.close()                                                                                                                                                            # |
        write_file.close()                                                                                                                                                           # |
                                                                                                                                                                                     # |
        lines[line_edit-1] = lines[line_edit-1].strip().split(",")                                                                                                                   # |This is a bit of a hack to maintain the original formatting of the line,
        lines[line_edit-1][int(variable_edit)-1] = new_value                                                                                                                         # ||as the line is split into a list, then the variable is edited,
        lines[line_edit-1] = ",".join(lines[line_edit-1]) + "\n"                                                                                                                     # ||then the list is joined back into a string with commas.
                                                                                                                                                                                     # |
        file = open(filename, "w")                                                                                                                                              # |Opens hotdogs file in write mode
        for i in lines:                                                                                                                                                              # |Writes every entry from lines list into it
            file.write(lines[lines.index(i)])                                                                                                                                        # |
        file.close()                                                                                                                                                                 # |
                                                                                                                                                                                     #
    elif admin_choice == "2":                                                                                                                                                        # If admin option is "2":
        input_file = open("hotdogsMemory.txt", "r")                                                                                                                                  # |Opens hotdogsMemory file in read mode
        output_file = open(filename, "w")                                                                                                                                       # |Opens hotdogs file in write mode
        for line in input_file:                                                                                                                                                      # |Writes every line from Memory file into hotdogs file
            output_file.write(line)                                                                                                                                                  # ||
        input_file.close()                                                                                                                                                           # |Closes both files
        output_file.close()                                                                                                                                                          # ||
                                                                                                                                                                                     #
    elif admin_choice == "3":                                                                                                                                                        # If admin option is "3":
        input_file = open("hotdogsOrigin.txt", "r")                                                                                                                                  # |Opens hotdogsOrigin file in read mode
        output_file = open(filename, "w")                                                                                                                                       # |Opens hotdogs file in write mode
        for line in input_file:                                                                                                                                                      # |Writes every line from Origin file into hotdogs file
            output_file.write(line)                                                                                                                                                  # ||
        input_file.close()                                                                                                                                                           # |Closes both files
        output_file.close()                                                                                                                                                          # ||
                                                                                                                                                                                     #
    else:                                                                                                                                                                            # Else: (if admin option is "4")
        new_line_continue = str(input("Are you sure you want to add a new line to the data? (Y/N): "))                                                                               # |Takes input from user for whether or not they want to continue adding lines
        while new_line_continue != "Y" and new_line_continue != "N" or new_line_continue == "":                                                                                      # |While the input is not "Y", is not "N", or is "":
            new_line_continue = str(input("Unknown command, please enter Y or N: "))                                                                                                 # ||Prints error message and asks user to input again
        if new_line_continue == "N":                                                                                                                                                 # |If the input was "N":
            print("Admin choice cancelled, please run the code again to check the functionality of the data.")                                                                       # ||Prints end line message to user
            exit()                                                                                                                                                                   # ||Ends code early
        if new_line_continue == "Y":                                                                                                                                                 # |If the input was "Y":
            read_file = open(filename, "r")                                                                                                                                     # ||Opens hotdogs file in read mode
            write_file = open("hotdogsMemory.txt", "w")                                                                                                                              # ||Opens hotdogsMemory file in write mode
                                                                                                                                                                                     # |
            for line in read_file:                                                                                                                                                   # ||Writes every line from hotdogs file to hotdogsMemory file
                write_file.write(line)                                                                                                                                               # |
            write_file.close()                                                                                                                                                       # |Closes both files
            read_file.close()                                                                                                                                                        # ||
                                                                                                                                                                                     # ||
            append_file = open(filename, "a")                                                                                                                                    # |Appending hotdogs.txt with new line
            new_vendor_id = str(input("Enter the new vendor's ID (Format: XX_000, where X is an uppercase letter and 0 is a digit): "))                                              # |Adding varioables one by one
            new_vendor_name = str(input("Enter the new vendor's name: "))                                                                                                            # |
            new_year_week = str(input("Enter the year and week of the data (Format: YYYYWW, where YYYY [2000-2026] is the year and WW [01-52] is the week number): "))               # |WARNING:
            new_vegan_hotdogs = int(input("Enter the number of vegan hotdogs supplied (Must be an integer, and a multiple of 10): "))                                                # ||These variables have not been checked.
            new_meat_hotdogs = int(input("Enter the number of meat hotdogs supplied (Must be an integer, and a multiple of 10): "))                                                  # ||However, the code automatically undos the codde in the case of an error.
            new_onions = float(input("Enter the amount of onions supplied (Must be a float, and divisible by 0.5): "))                                                               # ||The undo is used in the first code block, beginning at line 81.
            new_ketchup = int(input("Enter the amount of ketchup supplied (Must be an integer between 1 and 4, inclusive): "))                                                       # |
            print(f"New line to be added:\n{new_vendor_id},{new_vendor_name},{new_year_week},{new_vegan_hotdogs},{new_meat_hotdogs},{new_onions},{new_ketchup}")                     # |Shows the user the line they made
            append_file.write(f"{new_vendor_id},{new_vendor_name},{new_year_week},{new_vegan_hotdogs},{new_meat_hotdogs},{new_onions},{new_ketchup}\n")                              # |Appends new line to hotdogs.txt
                                                                                                                                                                                     # |
    print("Admin choice executed, please run the code again to check the functionality of the data.")                                                                                # Print message to user after admin choice is executed
    exit()                                                                                                                                                                           # Exit the code after admin choice is made, as the user needs to edit
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

# Defining search algorithms ---------------------------+ 
def linear_search(items, target, hidden, request):      #[E] LINEAR SEARCH
    start_time = time.perf_counter()                    # |Saves current time as variable
    index = 0                                           # |Hasn't searched yet, begins index at 0
    found = False                                       # |Starts code with found as False
                                                        # |
    while found == False and index < len(items):        # |While found is false and index is less than the length of items:
        if target == items[index]:                      # ||If the target is the currently searched item:
            found = True                                # |||The item is found, found is True
        else:                                           # ||Else:
            index += 1                                  # |||Index is incremented by 1, if statement moves to next item
    end_time = time.perf_counter()                      # |Saves current time as variable
                                                        # |
    if found == False:                                  # |If found is false:
        print(f"{target} not found.")                   # ||Print to the user that the target is not found
    if hidden != True:                                  # |If hidden is not true:
        print(f"Found {target} after {index} step(s).") # ||Prints message for user, telling what was found where
    if request == "time":                               # |If request is "time":
        return (end_time - start_time)                  # ||Returns this calculation, resulting in how long the code took
    else:                                               # |If request is anything else:
        return index                                    # ||Return the index of the item found
                                                        #
def binary_search(items, target, hidden, request):      #[F] BINARY SEARCH:
    start_time = time.perf_counter()                    # |Saves current time as variable
    found = False                                       # |Starts code with fpound as false
    first = 0                                           # |First variable is set to 0
    last = len(items) - 1                               # |Last variable is set to one less the length of items
    midpoint = 0                                        # |Midpoint is also set to 0
    steps = 0                                           # |Hasn't searched yet, begins steps at 0
                                                        # |
    while first <= last and found == False:             # |While first is less or equal than last and found is False:
        midpoint = (first + last) / 2                   # ||Midpoint is half of the sum of first and last
        if type(midpoint) == float:                     # ||If the type of midpoint is a float (if the sum of first and last resulted in an odd number):
            midpoint += 0.5                             # |||Midpoint is incrmented by 0.5
            midpoint = int(midpoint)                    # |||Midpoint is converted into an integer
        if items[midpoint] == target:                   # ||If the midpoint of items is the target:
            found = True                                # |||Sets found to True
        elif items[midpoint] < target:                  # ||Elif if midpoint of items is less than target:
            first = midpoint + 1                        # |||First is set to one more of the midpoint
        else:                                           # ||If every other argument is false
            last = midpoint - 1                         # |||Last is set to one less of the midpoint
        steps += 1                                      # ||Add one to the steps counter
    end_time = time.perf_counter()                      # |Saves current time as variable
                                                        # |
    if hidden != True:                                  # |If hidden is not true:
        print(f"Found {target} after {steps} step(s).") # ||Prints message for user, telling what was found where
    if request == "time":                               # |If request is "time":
        return (end_time - start_time)                  # ||Returns this calculation, resulting in how long the code took
    else:                                               # |If request is anything else:
        return steps                                    # ||Return the steps took by the algorithm
#-------------------------------------------------------+

# Defining sort algorithms ----------------------------------------------------------------------------------------+
def bubble_sort(items, hidden, request):                                                                           # BUBBLE SORT:
    start_time = time.perf_counter()                                                                               # |Saves current time as variable
    swaps = 0                                                                                                      # |Sets swaps to 0
    n = len(items)                                                                                                 # |n is equal to the length of items
    for i in range(n):                                                                                             # |For every number in the range of 0 to n:
        for j in range(0, n - i - 1):                                                                              # ||For every number in the range of 0 to n minus i minus 1:
            if items[j] > items[j + 1]:                                                                            # |||If items[j] is more than items[i + 1]
                items[j], items[j + 1] = items[j + 1], items[j]                                                    # ||||Swaps the position of the two entries
                swaps += 1                                                                                         # ||||Adds one to the swaps counter
    end_time = time.perf_counter()                                                                                 # |Saves current time as variable
                                                                                                                   # |
    if hidden != True:                                                                                             # |If hidden is not true:
        print(f"Sorted after {swaps} swap(s).")                                                                    # ||Prints message to user, telling how many steps it took to sort
    if request == "swaps":                                                                                         # |If request is "swaps":
        return swaps                                                                                               # |Returns the swaps counter
    if request == "time":                                                                                          # |If the request is "time"
        return (end_time - start_time)                                                                             # ||Returns this calculation, resulting in how long the code took
    else:                                                                                                          # |If request is anything else:
        return items                                                                                               # |Returns the sorted items
                                                                                                                   #
def quick_sort(items, hidden, request):                                                                            # QUICK SORT:
    start_time = time.perf_counter()                                                                               # |Saves current time as variable
    swaps = 0                                                                                                      # |Sets swaps to 0
    if len(items) <= 1:                                                                                            # |If the length of items is less or equal to 1:
        return items                                                                                               # ||Return items
    pivot = items[len(items) // 2]                                                                                 # |Pivot is equal to the index halfway along the items
    left = [x for x in items if x < pivot] #[G]                                                                    # |Left is equal to 'for x in items, if x is less than pivot'
    swaps += len(left)                                                                                             # |Swaps is incrememnted by the length of left
    middle = [x for x in items if x == pivot]                                                                      # |Middle is equal to 'for x in items, if x is equal to pivot'
    swaps += len(middle)                                                                                           # |Swaps is incremented by the length of middle
    right = [x for x in items if x > pivot]                                                                        # |Right is equal to 'for x in items, if x is more than pivot'
    swaps += len(right)                                                                                            # |Swaps is incremented by the length of right
    end_time = time.perf_counter()                                                                                 # |Saves current time as variable
                                                                                                                   # |
    if hidden != True:                                                                                             # |If hidden is not true:
        print(f"Sorted after {swaps} swap(s).")                                                                    # ||Prints messages to user, telling how many steps it took to sort
    if request == "swaps":                                                                                         # |If request is "swaps":
        return swaps                                                                                               # ||Returns the swaps counter
    if request == "time":                                                                                          # |If request is "time":
        return (end_time - start_time)                                                                             # ||Returns this calculation, resulting in how long the code took
    else:                                                                                                          # |If request is anything else:
        return quick_sort(left, hidden=True, request=None) + middle + quick_sort(right, hidden=True, request=None) # ||Returns the sorted items of left. then middle, then the sorted items of right
#------------------------------------------------------------------------------------------------------------------+ 

# User-inputted category search ----------------------------------------------------------------------------------------------------------------+
query_check = False                                                                                                                             # Initial boolean assignment
print("\nAvailable categories:\n 1. vendor_id\n 2. vendor_name\n 3. year_week\n 4. vegan_hotdogs\n 5. meat_hotdogs\n 6. onions\n 7. ketchup\n") # Prints the available categories in a bullet point list
while query_check != True:                                                                                                                      # |While query_cehck is not True:
    try:                                                                                                                                        # |Try command used to prevent errors
        user_search = int(input("What category would you like to search the data in? (Enter a number from 1 to 7): "))                          # ||Ask user to input an INTEGER from 1 to 7, inclusive
        for i in [0, len(hotdogs_data)]:                                                                                                        # ||For every number in range of 0 to the length of hotdogs_data
            while user_search < 1 or user_search > 7 or user_search == "":                                                                      # |||While user_search is less than 1, more than 7, or is "":
                user_search = int(input("Category not found, ensure input is within range: "))                                                  # ||||Prints error messages, and asks again for valid input
        if user_search > 1 or user_search < 7:                                                                                                  # ||If user_search is more than 1 or less than 7
           query_check = True                                                                                                                   # ||Query_check is turned True
    except ValueError:                                                                                                                          # |Except error called to stop code crash
        print("Input is not an integer.")                                                                                                       # ||Prints error message, telling user input was not an integer
#-----------------------------------------------------------------------------------------------------------------------------------------------+

# Filtering data -------------------------------------------------------------+
def filter_scraper(target_filter, vendor_name, hotdogs_data, hidden):         # Defines filter scraper algorithm
    file = open(filename, "r")                                                # |Opens hotdogs file in read mode
    items = []                                                                # |Sets empty list as items
    i = 0                                                                     # |Creates i variable inside algorithm
    for line in file:                                                         # |For everu line in hotdogs file:
        i += 1                                                                # ||i is incremented by 1
        segment = []                                                          # ||Segment list is emptied
        line = line.strip().split(",")                                        # ||Line is stripped and splitted
        if vendor_name in line:                                               # |If the vendor_name is in the line list
            segment = line[target_filter-1]                                   # ||Segment is the line list's index using one less of the target_filter
            items.append(segment)                                             # ||Appends segment to items list
    if not hidden:                                                            # |If hidden is not true:
        print(f"{target_filter} for {vendor_name}: {items}")                  # ||Prints messgae, telling user their target filter, the vendor name, and the items found
    file.close()                                                              # |Closes file
    return items                                                              # |Returns scraped items
                                                                              #
items = filter_scraper(user_search, search_query, hotdogs_data, hidden=False) # |Items equal the algorithms call of the 4 arguments listed, with hidden being false to show the user the print message
#-----------------------------------------------------------------------------+

# Sorting if wanted ----------------------------------------------------------------------------------------------------+
sort_input = str(input("\nWould you like to sort the data before searching? (Y/N): "))                                  # Sort input is taken from user
sort_options = ["Bubble Sort", "Quick Sort"]                                                                            # Sort options are "Bubble Sort" and "Quick Sort"
while sort_input != "Y" and sort_input != "N" or sort_input == "":                                                      # While the input from user is not "Y", not "N", or is "":
    sort_input = str(input("Invalid input, please enter Y or N: "))                                                     # |Asks user again for valid sort input
if sort_input == "Y":                                                                                                   # If the sort input is "Y":
    sort_choice = str(input(f"Which sorting algorithm would you like to use? ({sort_options[0]}/{sort_options[1]}): ")) # |Sorting code initiated, asking user for algorithm choice
    while sort_choice not in sort_options or sort_choice == "":                                                         # |While the choice input is not in sort_options list or is "":
        sort_choice = str(input("Invalid input, please enter a valid sorting algorithm: "))                             # ||Asks user again for valid choice input
    if sort_choice == sort_options[0]:                                                                                  # |If sort choice is index 0 of sort_options ("Bubble Sort"):
        items = bubble_sort(items, hidden=False, request="items")                                                       # ||Items is sorted through the bubble sort algorithm
    else:                                                                                                               # |Else ("Quick Sort"):
        items = quick_sort(items, hidden=False, request="items")                                                        # ||Items is sorted through the quick sort algorithm
#-----------------------------------------------------------------------------------------------------------------------+

# Searching ----------------------------------------------------------------------------------------------------------------+
target = str(input("What is your search query?: "))                                                                         # Target input is taken from user
while target not in items or target == "":                                                                                  # |While target input is not in items, or is "":
    target = str(input("Query not found, please enter a valid query: "))                                                    # ||Asks user for valid target input
                                                                                                                            #
search_options = ["Linear Search", "Binary Search"]                                                                         # Creates search options with "Linear Search" and "Binary Search"
search_choice = str(input(f"Which searching algorithm would you like to use? ({search_options[0]}/{search_options[1]}): ")) # Search choice is taken from the printed info message, accurately telling the user of the choices available
while search_choice not in search_options or search_choice == "":                                                           # |While search choice is not in search options list, or is "":
    search_choice = str(input("Invalid input, please enter a valid searching algorithm: "))                                 # ||Asks user again for valid choice input
if search_choice == search_options[0]:                                                                                      # |If search choice is index 0 of search_options ("Linear Search"):
    linear_search(items, target, False, "placeholder")                                                                      # ||Items is searched through the linear search algorithm
else:                                                                                                                       # |Else ("Binary Search"):
    print("WARNING: Binary Search requires sorting before it is used.")                                                     # ||<-- This warning is put in place because binary sort requires a sorted list
    binary_search(items, target, False, "placeholder")                                                                      # ||Items is searched through the binary search algorithm
#---------------------------------------------------------------------------------------------------------------------------+

# Secondary variable association --------------------------------------+ Calling filter scraper algorithm with different target filters.
v_hotdogs = filter_scraper(4, search_query, hotdogs_data, hidden=True) # 4 = vegan_hotdogs
total_v_hotdogs = 0                                                    # Creates total vegan hotdog counter
for i in v_hotdogs:                                                    # For every index in v_hotdogs:
    total_v_hotdogs += int(i)                                          # |Increment the total vegan hotdog counter by i, converted to an integer.
                                                                       #
m_hotdogs = filter_scraper(5, search_query, hotdogs_data, hidden=True) # 5 = meat_hotdogs
total_m_hotdogs = 0                                                    # Creates total meat hotdog counter
for i in m_hotdogs:                                                    # For every index in m_hotdogs:
    total_m_hotdogs += int(i)                                          # |Increment the total meat hotdog counter by i, converted to an integer.
                                                                       #
onions = filter_scraper(6, search_query, hotdogs_data, hidden=True)    # 6 = onions
total_onions = 0                                                       # Creates total onions counter
for i in onions:                                                       # For every index in onions:
    total_onions += float(i)                                           # |Increment the total onions counter by i, converted to an integer.
                                                                       #
ketchup = filter_scraper(7, search_query, hotdogs_data, hidden=True)   # 7 = ketchup
total_ketchup = 0                                                      # Creates total ketchup counter
for i in ketchup:                                                      # For every index in ketchup:
    total_ketchup += int(i)                                            # |Increment the total ketchup counter by i, converted to an integer.
                                                                       #
file.close()                                                           # Closes file
#----------------------------------------------------------------------+

# Background algorithms hidden from user ---------------------------------------+
items = filter_scraper(user_search, search_query, hotdogs_data, hidden=True)    # Resetting items to original state
                                                                                #
linear_steps = linear_search(items, target, hidden=True, request="placeholder") # Linear steps is the linear search algorithm, with hidden as True
bubble_sort(items, hidden=True, request="placeholder")                          # Sorts items using bubble sort algorithm for binary search algorithm to work properly
binary_steps = binary_search(items, target, hidden=True, request="placeholder") # BInary steps is the binary search algorithm, with hidden as True
                                                                                #
items = filter_scraper(user_search, search_query, hotdogs_data, hidden=True)    # Resetting items to original state for sorting algorithms
bubble_swaps = bubble_sort(items, hidden=True, request="swaps")                 # Bubble swaps is the bubble sort algorithm, with hidden as True and request as "swaps"
quick_swaps = quick_sort(items, hidden=True, request="swaps")                   # Quick swaps is the quick sort algorithm, with hidden as True and request as "swaps"
#-------------------------------------------------------------------------------+

# Analysis output! =========================================================================================================================================================================+
file = open("analysis.txt", "w")                                                                                                                                                            # Opening file
file.write("Analysis of hotdog data:\n")                                                                                                                                                    # Start of analysis file
file.write(f"Vendor searched: {search_query}\n")                                                                                                                                            # This line is from the search query of the user.
                                                                                                                                                                                            #
file.write(f"Number of vegan hotdogs supplied: {total_v_hotdogs}\n")                                                                                                                        # These four lines are
file.write(f"Number of meat hotdogs supplied: {total_m_hotdogs}\n")                                                                                                                         # |from the variable
file.write(f"Total amount of onions supplied: {total_onions}\n")                                                                                                                            # |association section, where
file.write(f"Total amount of ketchup supplied: {total_ketchup}\n")                                                                                                                          # |the data is totalled up.
file.write(f"-------------------------------------------------------\n")                                                                                                                    #
file.write(f"Algorithm comparisons:\n")                                                                                                                                                     #
file.write(f"Linear search found {target} in {linear_steps} steps, and took {(linear_search(items, target, hidden=True, request="time")*1000000):.2f} microseconds.\n")                     # These four lines are from the
file.write(f"Binary search, after sorting, found {target} in {binary_steps} steps, and took {binary_search(items, target, hidden=True, request="time")*1000000:.2f} microseconds.\n")       # |previous section with the
file.write(f"Bubble sort sorted {len(items)} items in {bubble_swaps} steps, and took {bubble_sort(items, hidden=True, request="time")*1000000:.2f} microseconds.\n")                        # |hidden algorithms simulating
file.write(f"Quick sort sorted {len(items)} items in {quick_swaps} steps, and took {quick_sort(items, hidden=True, request="time")*1000000:.2f} microseconds.\n")                           # |the algorithms
file.close()                                                                                                                                                                                #
#===========================================================================================================================================================================================+

# +------------------+
# | Repository Links |
# +------------------+
# | Line 146 - [A]   |
# | Line 041 - [B]   |
# | Line 120 - [C]   |
# | Line 113 - [D]   |
# | Line 249 - [E]   |
# | Line 177 - [F]   |
# | Line 327 - [G]   |
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

4. ADDING
  - Asks user if they want to continue adding lines
  - Hotdogs.txt is copied to HotdogsMemory.txt
  - Every line from Hotdogs.txt is put into a list
  - Takes input of every variable one-by-one from user
  - Appends line into list of lines
  - Writes the new list of lines to Hotdogs.txt
  - Loop back to start
'''
