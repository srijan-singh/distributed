# All available systems
systems = [7, 6, 5, 4, 3, 2, 1]

# Status (True:Active, False:Inactive)
systems_status = {
    7:True,
    6:True,
    5:True,
    4:True,
    3:True,
    2:True,
    1:True
}

# Maximum priority number
cordinator = 7 

# Length of system
length = len(systems)

# Cordinator has been crashed thus it's status is false
systems_status[cordinator] = False

# Node which noticed that cordinator failed
current_node = 3

# If no node will be active this current node would be considered as default cordinator
new_cordinator = current_node

# Finding the maximum priority number greater than current node and whose status is active
for current_system in systems:
    if current_node < current_system and systems_status[current_system] == True:
        new_cordinator = max(new_cordinator, current_system)

# New Cordinator
print(new_cordinator)

