# --------------------------- #
# Intro to CS Final Project   #
# Gaming Social Network       #
# --------------------------- #
#
# Example string input. Use it to test your code.
example_input="John is connected to Bryant, Debra, Walter.\
John likes to play The Movie: The Game, The Legend of Corgi, Dinosaur Diner.\
Bryant is connected to Olive, Ollie, Freda, Mercedes.\
Bryant likes to play City Comptroller: The Fiscal Dilemma, Super Mushroom Man.\
Mercedes is connected to Walter, Robin, Bryant.\
Mercedes likes to play The Legend of Corgi, Pirates in Java Island, Seahorse Adventures.\
Olive is connected to John, Ollie.\
Olive likes to play The Legend of Corgi, Starfleet Commander.\
Debra is connected to Walter, Levi, Jennie, Robin.\
Debra likes to play Seven Schemers, Pirates in Java Island, Dwarves and Swords.\
Walter is connected to John, Levi, Bryant.\
Walter likes to play Seahorse Adventures, Ninja Hamsters, Super Mushroom Man.\
Levi is connected to Ollie, John, Walter.\
Levi likes to play The Legend of Corgi, Seven Schemers, City Comptroller: The Fiscal Dilemma.\
Ollie is connected to Mercedes, Freda, Bryant.\
Ollie likes to play Call of Arms, Dwarves and Swords, The Movie: The Game.\
Jennie is connected to Levi, John, Freda, Robin.\
Jennie likes to play Super Mushroom Man, Dinosaur Diner, Call of Arms.\
Robin is connected to Ollie.\
Robin likes to play Call of Arms, Dwarves and Swords.\
Freda is connected to Olive, John, Debra.\
Freda likes to play Starfleet Commander, Ninja Hamsters, Seahorse Adventures."

# -----------------------------------------------------------------------------
# create_data_structure(string_input):

def create_data_structure(string_input):
    network = {}
    temp_output = string_input.split(".") # list of sentences
    if not string_input:
        return network
    for i in range(0, len(temp_output)-1, 2):
        sentence_contact = temp_output[i].split(" is connected to ")
        participant = sentence_contact[0] # Selection of participant's name
        contacts_list = sentence_contact[1].split(", ") # Preparation of the list of contacts
        sentence_game = temp_output[i+1].split(" likes to play ")
        games_list = sentence_game[1].split(", ")  # Preparation of the list of games
        network[participant]={"contacts": contacts_list, "games": games_list} # filling the network
    return network

# ----------------------------------------------------------------------------- #

# get_connections(network, user):

def get_connections(network, user):
    if user in network:
        return network[user]["contacts"] # the value of the key "contacts" is already defined as a list, even if empty
	return None

# -----------------------------------------------------------------------------
# get_games_liked(network, user):

def get_games_liked(network,user):
    if user not in network:
        return None
    return network[user]["games"]

# -----------------------------------------------------------------------------
# add_connection(network, user_A, user_B):

def add_connection(network, user_A, user_B):
    if user_A not in network or user_B not in network:
        return False
    else:
        if user_B in network[user_A]["contacts"]:
            return network # "network unchanged"
        else:
            network[user_A]["contacts"].append(user_B) # adds user_B to the list of contacts of user_A, even if the list is empty
    return network

# -----------------------------------------------------------------------------
# add_new_user(network, user, games):

def add_new_user(network, user, games):
    if user in network:
        return network #"UNCHANGED"
    else:
        network[user]={"contacts": [], "games": games} # As requested, a new user has no connections
        return network

# -----------------------------------------------------------------------------
# get_secondary_connections(network, user):

def get_secondary_connections(network, user):
    result=[]
    if user in network:
        for first_connections in get_connections(network, user): # list of the first degree connection
            for each_secondary in get_connections(network, first_connections): # list of the second degree connection
                if each_secondary not in result:
                    result.append(each_secondary) # simple addition of the connection if not already there
        return result
    else:
        return None

# -----------------------------------------------------------------------------
# count_common_connections(network, user_A, user_B):

def count_common_connections(network, user_A, user_B):
    if user_A not in network or user_B not in network: # simple check at the beginning of the procedure
        return False
    else:
        count=0
        list_A = get_connections(network, user_A) # list of connection for user_A
        list_B = get_connections(network, user_B) # list of connection for user_B
        for element in list_A:
            if element in list_B:
                count+=1 # counter!!
    return count

# -----------------------------------------------------------------------------
# find_path_to_friend(network, user_A, user_B):

def find_path_to_friend(network, user_A, user_B, viewed=None):
    if viewed==None:
        viewed=[] # initiate the "checker" to keep track of users already explored
    if user_A not in network or user_B not in network:
        return None # the basecase
    else:
        connected = get_connections(network, user_A)
        if user_B in connected:
            return [user_A, user_B] # the simplest situation
        else:
            viewed.append(user_A)
            for each in connected:
                if each not in viewed:
                    path = find_path_to_friend(network, each, user_B, viewed) # the recursion
                    if path:
                        return [user_A] + path
            return None

# Make-Your-Own-Procedure (MYOP)
# -----------------------------------------------------------------------------
# This procedure count the number of occurrence of each games for every participants and return a list of games ordered by popularity
def find_popular_games(network):
    from collections import Counter # importing the command Counter
    list_of_games=[]
    for participants in network:
        list_of_games = list_of_games + network[participants]["games"] # Simply merge the list of the games for every participant
    return Counter(list_of_games).most_common() # count the number of occurence of each game



net = create_data_structure(example_input)
#print net
#print get_connections(net, "Debra")
#print get_connections(net, "Mercedes")
#print get_games_liked(net, "John")
#print add_connection(net, "John", "Freda")
#print add_new_user(net, "Debra", [])
#print add_new_user(net, "Nick", ["Seven Schemers", "The Movie: The Game"]) # True
#print get_secondary_connections(net, "Mercedes")
#print count_common_connections(net, "Mercedes", "John")
#print find_path_to_friend(net, "John", "Ollie")
#print find_popular_games(net)
