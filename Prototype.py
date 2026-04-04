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

# Creating variables and setting up foundational information --------------------------------------+
print("Available vendors:\n 1. Dolly Dogs\n 2. Korner Kart\n")                                     #
available_vendors = ['Dolly Dogs', 'Korner Kart']                                                  #
metadata = []                                                                                      #
search_query = str(input("Please enter the name of the vendor you would like to search (2-25): ")) #
vendor_check = False                                                                               #
available_check = False                                                                            #
#--------------------------------------------------------------------------------------------------+

# Looping validations for 'search_query' ---------------------------------------------------+ #[D]
while vendor_check == False and available_check == False:                                   #
    # Length Validaton -------------------------------------+                               #
    if len(search_query) >= 2 and len(search_query) <= 25:  #                               #
        vendor_check = True                                 #                               #
        # Presence Check ----+                              #                               #
    elif search_query == "": #                              #                               #
        vendor_check = False #                              #                               #
        #--------------------+                              #                               #
    else:                                                   #                               #
        vendor_check = False                                #                               #
    #-------------------------------------------------------+                               #
    # Lookup Validation -------------------------+                                          #
    for i in [0, len(available_vendors)-1]:      #                                          #
        if search_query == available_vendors[i]: #                                          #
            available_check = True               #                                          #
            break                                #                                          #
        else:                                    #                                          #
            available_check = False              #                                          #
    #--------------------------------------------#                                          #
    if vendor_check == False and available_check == False:                                  #
        search_query = str(input("Vendor not found, or name out of length range (2-25): ")) #
#-------------------------------------------------------------------------------------------#

# Dictionary handling ----------------+
file = open("Hotdogs.txt", "r")       #
for line in file:  #[A]               #
    if line.find(search_query) != -1: #
        data = line.split(",")        #
        data == {  #[B]               #
            "vendor_id": data[0],     #
            "vendor_name": data[1],   #
            "year_week": data[2],     #
            "vegan_hotdogs": data[3], #
            "meat_hotdogs": data[4],  #
            "onions": data[5],        #
            "ketchup": data[6]        #
        }                             #
    else:                             #
        continue                      #
    # Adding dictionary to list --+   #
    metadata.append(data)         #   #
    print(metadata)               #   #
    #-----------------------------+   #
#-------------------------------------#

# +------------------+
# | Repository Links |
# +------------------+
# | Line 65 - [A]    |
# | Line 68 - [B]    |
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
# | Line ?? - [?]    |
# | Line ?? - [?]    |
# +------------------+
