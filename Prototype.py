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
# | 6. Compare the efficiency (execution time) of the different searches.             |     N     |
# | 7. Compare the efficiency (execution time) of the different sorts.                |     N     |
# | 8. Provide analysis for the user (most productive vendor, number of vegan hotdogs |     N     |
# |    versus meat hotdogs supplied, vendor using the least amount of ketchup, etc.)  |           |
# | 9. Save results of analysis to an output file.                                    |     N     |
# +-----------------------------------------------------------------------------------+           |
# |                               Secondary Milestones:                               |           |
# +-----------------------------------------------------------------------------------+           |
# | A. Allow the user to edit the variables within 'hotdogs.txt'.                     |     N     |
# | B. ???                                                                            |     N     | these requirement rows are only for place holder purposes
# +-----------------------------------------------------------------------------------+-----------+

# Creating variables and setting up foundational information ----------------------------------------+
import math                                                                                          #
print("Available vendors:\n 1. Dolly Dogs\n 2. Korner Kart")                                         #
available_vendors = ['Dolly Dogs', 'Korner Kart']                                                    # List of available vendors
search_query = str(input("\nPlease enter the name of the vendor you would like to search (2-25): ")) # >user inputs search query here
#----------------------------------------------------------------------------------------------------+

# Looping validations for 'search_query' ---------------------------------------------------+[D]
length_check = False                                                                        #
available_check = False                                                                     #
while length_check != True or available_check != True:                                      # "While either of these variables are False, run this piece of code until they are both True."
    # Length Validaton ------------------------------------+                                #
    if len(search_query) >= 2 and len(search_query) <= 25: #                                # "If the length of the search query is between the inclusive range of 2 to 25...
        length_check = True                                #                                #  "...the length check becomes True."
        # Presence Check ----+                             #                                #
    elif search_query == "": #                             #                                # "Alternatively, if nothing is inputted..."
        length_check = False #                             #                                #  "...the length check stays False."
        #--------------------+                             #                                #
    else:                                                  #                                # "If all above statements are false..."
        length_check = False                               #                                #  "...the length check is too."
    #------------------------------------------------------+                                #
    # Lookup Validation ------------------+                                                 #
    if search_query in available_vendors: #                                                 # "If the search query is found in our available vendors list..."
        available_check = True            #                                                 #  "...the avialbile check becomes True."
    #-------------------------------------#                                                 #
    if length_check != True or available_check != True:                                     # "If, after all the validations, either check is still false..."
        search_query = str(input("Vendor not found, or name out of length range (2-25): ")) #  "...tell the user to input the query again with an error message."
#-------------------------------------------------------------------------------------------#

# Array handling -----------------------+
hotdog_data = []                        #
file = open("hotdogs.txt", "r")         #
for line in file:                       #[A]
    if line.find(search_query) != -1:   # If the search query (case sensitive) is not found in the line...
        parts = line.strip().split(",") #  ...strip the line from its commas...
        hotdog_data.append(parts)       #  ...and append it to 'hotdog_data'
    else:                               # If the search query is not found in the line...
        continue                        #  ...skip to the next line in the file.
#---------------------------------------#   This may seem incorrect, but due to the query being forced to be EXACTLY how it's presented to the user (e.g. 'Dolly Dog's)...
                                        #   ...the code can't be given an incorrect vendor name that doesn't exist.

# Defining search algorithms ---------------------------+ 
def linear_search(items, target, hidden):               #[E] LINEAR SEARCH
    index = 0                                           #
    found = False                                       #
                                                        #
    while found == False and index < len(items):        #
        if target == items[index]:                      #
            found = True                                #
        else:                                           #
            index += 1                                  #
                                                        #
    if found == False:                                  #
        print(f"{target} not found.")                   #
    if hidden != True:                                  #
        print(f"Found {target} after {index} step(s).") #
                                                        #
def binary_search(items, target, hidden):               #[F] BINARY SEARCH:
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
    if hidden != True:                                  #
        print(f"Found {target} after {index} step(s).") #
#-------------------------------------------------------+

# Defining sort algorithms -------------------------------------+
def bubble_sort(items, hidden):                                 # BUBBLE SORT:
    swaps = 0                                                   #
    n = len(items)                                              #
    for i in range(n):                                          #
        for j in range(0, n - i - 1):                           #
            if items[j] > items[j + 1]:                         #
                items[j], items[j + 1] = items[j + 1], items[j] #
                swaps += 1                                      #
    if hidden != True:                                          #
        print(f"Sorted after {swaps} swap(s).")                 #
    return items                                                #
                                                                #
def quick_sort(items, hidden):                                  # QUICK SORT:
    swaps = 0                                                   #
    if len(items) <= 1:                                         #
        return items                                            #
    pivot = items[len(items) // 2]                              #
    left = [x for x in items if x < pivot]                      #
    swaps += len(left)                                          #
    middle = [x for x in items if x == pivot]                   #
    swaps += len(middle)                                        #
    right = [x for x in items if x > pivot]                     #
    swaps += len(right)                                         #
    if hidden != True:                                          #
        print(f"Sorted after {swaps} swap(s).")                 #
    return quick_sort(left) + middle + quick_sort(right)        #
#---------------------------------------------------------------+ 

# User-inputted category search ----------------------------------------------------------------------------------------------------------------+
query_check = False                                                                                                                             # Initial boolean assignment
print("\nAvailable categories:\n 1. vendor_id\n 2. vendor_name\n 3. year_week\n 4. vegan_hotdogs\n 5. meat_hotdogs\n 6. onions\n 7. ketchup\n") #
while query_check != True:                                                                                                                      # While loop begun
    try:                                                                                                                                        # Try command used to prevent errors
        user_search = int(input("What category would you like to search the data in? (Enter a number from 1 to 7): "))                          # Ask user to input an INTEGER from 1 to 7, inclusive
        for i in [0, len(hotdog_data)]:                                                                                                         #
            while user_search < 1 or user_search > 7:                                                                                           #
                user_search = int(input("Category not found, ensure input is within range: "))                                                  #
        if user_search > 1 or user_search < 7:                                                                                                  #
           query_check = True                                                                                                                   #
    except ValueError:                                                                                                                          # Except error called to stop code crash
        print("Input is not an integer.")                                                                                                       #
#-----------------------------------------------------------------------------------------------------------------------------------------------+

# Filtering data ------------------------------------------------------------+
def filter_scraper(target_filter, vendor_name, data, hidden):                #
    file = open("hotdogs.txt", "r")                                          #
    items = []                                                               #
    i = 0                                                                    #
    for line in file:                                                        #
        i += 1                                                               #
        segment = []                                                         #
        line = line.strip().split(",")                                       #
        if vendor_name in line:                                              #
            segment = line[target_filter-1]                                  #
            items.append(segment)                                            #
    if not hidden:                                                           #
        print(f"{target_filter} for {vendor_name}: {items}")                 #
    return items                                                             #
    file.close()                                                             #
                                                                             #
items = filter_scraper(user_search, search_query, hotdog_data, hidden=False) #
#----------------------------------------------------------------------------+

# Sorting if wanted ----------------------------------------------------------------------------------------------------+
sort_input = str(input("\nWould you like to sort the data before searching? (Y/N): "))                                  #
sort_options = ["Bubble Sort", "Quick Sort"]                                                                            #
while sort_input != "Y" and sort_input != "N":                                                                          #
    sort_input = str(input("Invalid input, please enter Y or N: "))                                                     #
if sort_input == "Y":                                                                                                   #
    sort_choice = str(input(f"Which sorting algorithm would you like to use? ({sort_options[0]}/{sort_options[1]}): ")) #
    while sort_choice not in sort_options:                                                                              #
        sort_choice = str(input("Invalid input, please enter a valid sorting algorithm: "))                             #
    if sort_choice == sort_options[0]:                                                                                  #
        items = bubble_sort(items, hidden=False)                                                                        #
    else:                                                                                                               #
        items = quick_sort(items, hidden=False)                                                                         #
#-----------------------------------------------------------------------------------------------------------------------+

# Searching ----------------------------------------------------------------------------------------------------------------+
search_input = str(input("What is your search query?: "))                                                                   #
while search_input not in items:                                                                                            #
    search_input = str(input("Query not found, please enter a valid query: "))                                              #
                                                                                                                            #
search_options = ["Linear Search", "Binary Search"]                                                                         #
search_choice = str(input(f"Which searching algorithm would you like to use? ({search_options[0]}/{search_options[1]}): ")) #
while search_choice not in search_options:                                                                                  #
    search_choice = str(input("Invalid input, please enter a valid searching algorithm: "))                                 #
if search_choice == search_options[0]:                                                                                      #
    linear_search(items, search_input, hidden=False)                                                                        #
else:                                                                                                                       #
    print("WARNING: Binary Search requires sorting before it is used.")                                                     #
    binary_search(items, search_input, hidden=False)                                                                        #
#---------------------------------------------------------------------------------------------------------------------------+

# Secondary variable association -------------------------------------+
v_hotdogs = filter_scraper(4, search_query, hotdog_data, hidden=True) #
total_v_hotdogs = 0                                                   #
for i in v_hotdogs:                                                   #
    total_v_hotdogs += int(i)                                         #
                                                                      #
m_hotdogs = filter_scraper(5, search_query, hotdog_data, hidden=True) #
total_m_hotdogs = 0                                                   #
for i in m_hotdogs:                                                   #
    total_m_hotdogs += int(i)                                         #
                                                                      #
onions = filter_scraper(6, search_query, hotdog_data, hidden=True)    #
total_onions = 0                                                      #
for i in onions:                                                      #
    total_onions += float(i)                                          #
                                                                      #
ketchup = filter_scraper(7, search_query, hotdog_data, hidden=True)   #
total_ketchup = 0                                                     #
for i in ketchup:                                                     #
    total_ketchup += int(i)                                           #
                                                                      #
file.close()                                                          #
#---------------------------------------------------------------------+

# Background Algorithms hidden from user --------------------------------------------------?
items = filter_scraper(user_search, search_query, hotdog_data, hidden=True)

#------------------------------------------------------------------------------------------?

# Analysis output! ======================================================================================+
file = open("analysis.txt", "w")                                                                         #
file.write("Analysis of hotdog data:\n\n")                                                               #
file.write(f"Vendor searched: {search_query}\n")                                                         #
file.write(f"Number of vegan hotdogs supplied: {total_v_hotdogs}\n")                                     # These four
file.write(f"Number of meat hotdogs supplied: {total_m_hotdogs}\n")                                      # lines are
file.write(f"Total amount of onions supplied: {total_onions}\n")                                         # from the 
file.write(f"Total amount of ketchup supplied: {total_ketchup}\n")                                       # previous section
file.write(f"-------------------------------------------------------\n")                                 #
file.write(f"Algorithm comparisons:\n\n")                                                                #
file.write(f"Linear search found {search_input} in {len(items)} steps.\n")                               # These four
file.write(f"Binary search found {search_input} in {len(items) // 2} steps.\n")                          # lines are
file.write(f"Bubble sort sorted {len(items)} items in {len(items) ** 2} steps.\n")                       # from the
file.write(f"Quick sort sorted {len(items)} items in {round(len(items) * math.log(len(items)))} steps.") # 'items' length
file.close()                                                                                             #
#========================================================================================================+

# +------------------+
# | Repository Links |
# +------------------+
# | Line 42 - [D]    |
# | Line 64 - [A]    |
# | Line 73 - [E]    |
# | Line 87 - [F]    |
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
# |   36 | 1. This doesn't skim the file for every vendor name and format it into Title Case. |
# |  1?? | 2. I feel like there is a much simpler way to extract a variable from an array.    |
# |  ??? | 3. ???                                                                             |
# |  ??? | 4. ???                                                                             |
# |  ??? | 5. ???                                                                             |
# +-------------------------------------------------------------------------------------------+
