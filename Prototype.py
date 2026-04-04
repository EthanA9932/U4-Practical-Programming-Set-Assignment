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
# | Milestones:                                                                       | Complete? |
# +-----------------------------------------------------------------------------------+-----------+
# | 0. Read the data from the text file.                                              |     Y     |
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
available_vendors = ['Dolly Dogs', 'Korner Kart']                                                    # List of available vendors
search_query = str(input("\nPlease enter the name of the vendor you would like to search (2-25): ")) # >user inputs search query here
hotdog_data = []                                                                                     # Creating placeholder list for 'hotdog.txt' 
length_check = False                                                                                 #
available_check = False                                                                              #
#----------------------------------------------------------------------------------------------------+

# Looping validations for 'search_query' ---------------------------------------------------+ [D]
while length_check != True or available_check != True:                                      #
    # Length Validaton -------------------------------------+                               #
    if len(search_query) >= 2 and len(search_query) <= 25:  #                               # "If the length of the search is between the inclusive range of 2 to 25...
        length_check = True                                 #                               # "...the length check becomes true."
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

# Array handling ---------------------------+ [E]
file = open("hotdogs.txt", "r")             #
for line in file:  #[A]                     #
    if line.find(search_query) != -1:       #
        parts = line.strip().split(",")     #
        hotdog_data.append(parts)           #
    else:                                   #
        continue                            #
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

# Defining sort algorithms --?

#----------------------------?

# User-inputted category search ---------------------------------|
query_check = False                                              #
print("\nAvailable categories:\n 1. vendor_id\n 2. vendor_name\n 3. year_week\n 4. vegan_hotdogs\n 5. meat_hotdogs\n 6. onions\n 7. ketchup\n")
while query_check != True:                                       #
    try:                                                         #
        user_search = int(input("What category would you like to search the data in? (Enter a number from 1 to 7): "))   #
        for i in [0, len(hotdog_data)]:                          #
            while user_search < 1 or user_search > 7:            #
                user_search = int(input("Category not found, ensure input is within range: "))
        if user_search > 1 or user_search < 7:                   #
           query_check = True                                    #
    except ValueError:                                           #
        print("Input is not an integer.")                        #
#----------------------------------------------------------------|

# SEARCH --------------------------------------------------------------------+
file = open("hotdogs.txt", "r")
a = 0

def filter_scraper(target_filter, data):
    for line in file:
        if line.find(hotdog_data[user_search-1]) == -1:
            print(hotdog_data)

filter_scraper(user_search, hotdog_data)
#----------------------------------------------------------------------------+

# +------------------+
# | Repository Links |
# +------------------+
# | Line 41 - [D]    |
# | Line 61 - [E]    |
# | Line 63 - [A]    |
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

# +------+------------------------------------------------------------------------------------+
# | Line | Diary                                                                              |
# +------+------------------------------------------------------------------------------------+
# | 33   | 1. This doesn't skim the file for every vendor name and format it into Title Case. |
# | 1??  | 2. I feel like there is a much simpler way to extract a variable from an array.    |
# | ???  | 3. ???                                                                             |
# | ???  | 4. ???                                                                             |
# | ???  | 5. ???                                                                             |
# +-------------------------------------------------------------------------------------------+
