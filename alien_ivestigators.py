from tkinter import N, Y

team_options = [
    "Harvey (Physicist)",
    "Wendy (Has a really good flashlight)",
    "Andre (Owns the forest)",
    "Julie (Biologist)",
    "Cleetus (Self-proclaimed expert on things)",
    "Marlowe (Private Investigator)",
    "Brian (Talks to animals)",
    "Joan (Zealot)",
    "Winston (Agreed to be alien bait)",
    "Landrel (Anthropologist)",
    "Marvin (Photographer)",
    "Linda (Conspiracy Nut)"
]

print("There have reports of strange lights in the forest.")
print("The locals believe aliens have landed and are trying to recruit woodland creatures for their dastardly schemes.")
print("Your job is to assemble a team of investigators to check out the forest to find out what's really going on.")
print("---")
print()

team = []
#no_mebers = print("\033[H\033[J")

for option in team_options:
    
    print("Team so far:")
    for member in team:
       print("" + member)

    print()
    choice = input("Include '" + option + "'? (y/n) ")
    if choice == "y" or choice == "":
        team.append(option)
        print("\033[H\033[J")

if len(team) == 0:
    exit
else:
     leader = team[0]
     team.remove(leader)
     print("Team Leader: " + leader)

     print("And the rest of the team:")
     for member in team:
        print("  " + member)







