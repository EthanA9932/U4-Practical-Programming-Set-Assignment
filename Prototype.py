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
# | Requirements:                                                                     | Complete? |
# +-----------------------------------------------------------------------------------+-----------+
# | 1. Linear search the data when it is sorted.                                      |     N     |
# | 2. Linear search the data when it is unsorted.                                    |     N     |
# | 3. Search the data using a binary search.                                         |     N     |
# | 4. Sort the data using a bubble sort.                                             |     N     |
# | 5. Sort the data using a quick sort.                                              |     N     |
# | 6. Compare the efficiency (execution time) of the different searches.             |     N     |
# | 7. Compare the efficiency (execution time) of the different sorts.                |     N     |
# | 8. Provide analysis for the user (most productive vendor, number of vegan hotdogs |     N     |
# |    versus meat hotdogs supplied, vendor using the least amount of ketchup, etc.)  |           |
# | 9. Save results of analysis to an output file.                                    |     N     |
# +-----------------------------------------------------------------------------------+-----------+

# Creating variables and setting up foundational information ----------------------------------------+
print("Available vendors:\n 1. Dolly Dogs\n 2. Korner Kart")                                         #
available_vendors = ['blank', 'Dolly Dogs', 'Korner Kart']                                           #
metadata = []                                                                                        #
search_query = str(input("\nPlease enter the name of the vendor you would like to search (2-25): ")) #
length_check = False                                                                                 #
available_check = False                                                                              #
#----------------------------------------------------------------------------------------------------+

# Looping validations for 'search_query' ---------------------------------------------------+ #[D]
while length_check != True or available_check != True:                                      #
    # Length Validaton -------------------------------------+                               #
    if len(search_query) >= 2 and len(search_query) <= 25:  #                               #
        length_check = True                                 #                               #
        # Presence Check ----+                              #                               #
    elif search_query == "": #                              #                               #
        length_check = False #                              #                               #
        #--------------------+                              #                               #
    else:                                                   #                               #
        length_check = False                                #                               #
    #-------------------------------------------------------+                               #
    # Lookup Validation -------------------------+                                          #
    if search_query in available_vendors:        #                                          #
        available_check = True                   #                                          #
    #--------------------------------------------#                                          #
    if length_check != True or available_check != True:                                     #
        search_query = str(input("Vendor not found, or name out of length range (2-25): ")) #
#-------------------------------------------------------------------------------------------#

# Dictionary handling ----------------------+ [E]
file = open("hotdogs.txt", "r")             #
for line in file:  #[A]                     #
    if line.find(search_query) != -1:       #
        parts = line.strip().split(",")     #
        data = {                            #
            "vendor_id": parts[0],          #
            "vendor_name": parts[1],        #
            "year_week": parts[2],          #
            "vegan_hotdogs": int(parts[3]), #
            "meat_hotdogs": int(parts[4]),  #
            "onions": float(parts[5]),      #
            "ketchup": float(parts[6]),     #
        }                                   #
    else:                                   #
        continue                            #
    # Adding dictionary to list --+         #
    metadata.append(data)         #         #
    #-----------------------------+         #
#-------------------------------------------#

# Defining search algorithms ---------------------------------+ [F]
def linear_search(items, target):                             #
    index = 0                                                 #
    found = False                                             #
                                                              #
    while found == False and index < len(items):              #
        if target == items[index]:                            #
            found = True                                      #
            print(f"Found {target} at {index+1}.")            #
        else:                                                 #
            index += 1                                        #
                                                              #
    if found == False:                                        #
        print(f"{target} not found.")                         #
                                                              #
def binary_search(items, target):                             #
    found = False                                             # 
    first = 0                                                 #
    last = len(items) - 1                                     #
    midpoint = 0                                              #
    passes = 0                                                #
                                                              #
    while first <= last and found == False:                   #
        midpoint = (first + last) / 2                         #
        if type(midpoint) == float:                           #
            midpoint += 0.5                                   #
            midpoint = int(midpoint)                          #
        if items[midpoint] == target:                         #
            found = True                                      #
            print(f"Found {target} after {passes} pass(es).") #
        elif items[midpoint] < target:                        #
            first = midpoint + 1                              #
        else:                                                 #
            last = midpoint - 1                               #
        passes += 1                                           #
#-------------------------------------------------------------+

# User-inputted category search -----------------------------------------------------|
print("\nAvailable categories:\n 1. vendor_id\n 2. vendor_name\n 3. year_week\n 4. vegan_hotdogs\n 5. meat_hotdogs\n 6. onions\n 7. ketchup")
user_search = str(input("\nWhat category would you like to search the data in? "))   #
while user_search not in data:                                                       #
    user_search = str(input("Category not found, ensure underscores are present: ")) #
target_filter = user_search                                                          #


#------------------------------------------------------------------------------------|

# +------------------+
# | Repository Links |
# +------------------+
# | Line 40 - [D]    |
# | Line 60 - [E]    |
# | Line 62 - [A]    |
# | Line 82 - [F]    |
# | Line ?? - [?]    |
# | Line ?? - [?]    |
# | Line ?? - [?]    |
# | Line ?? - [?]    |
# | Line ?? - [?]    |
# | Line ?? - [?]    |
# | Line ?? - [?]    |
# | Line ?? - [?]    |
# | Line ?? - [?]    |
# | Line ?? - [?]    |
# | Line ?? - [?]    |
# | Line ?? - [?]    |
# | Line ?? - [?]    |
# | Line ?? - [?]    |
# | Line ?? - [?]    |
# | Line ?? - [?]    |
# +------------------+
