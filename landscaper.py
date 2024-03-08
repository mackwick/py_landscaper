## Player Starting Info
player = {
        "tool": 0, 
        "savings": 0
}

## Tools List
tools = [
        {"name": "teeth", "cost": 0, "income": 1}, 
        {"name": "rusty scissors", "cost": 5, "income": 5}, 
        {"name": "push mower", "cost": 25, "income": 50}, 
        {"name": "fancy mower", "cost": 250, "income": 100}, 
        {"name": "underpaid team", "cost": 500, "income": 250}
]

# print(tools[player["tool"]]["name"])

## Functions

def get_input():
        choice = str(input(f"Good morning and welcome to another day in the land of the free. Would you like to [c]ut grass, [b]uy a new tool, or [d]o something fun with the people you love?: "))
        if (choice == "c"):
               print("Great! Get to work!")
               cut_lawns()
        elif (choice == "b"):
                print("Alrighty, let's go down to the market.")
                buy_tool()
        elif (choice == "d"):
                print("You're not rich enough for that kind of freedom. Maybe if you stop being lazy and pull yourself up by your bootstraps, you can enjoy your life one day.")
                cut_lawns()
        else:
                print("That's not an option. Try again.")
                get_input()

def cut_lawns():
        print(f"You just earned ")
        # When player savings >= the cost of the tool at the current index +1, they can choose to buy a tool or keep cutting lawns
        # check win

def buy_tool():
        print("buying a tool") 
        ## If player buys a tool, tool index +1, and savings - tool[index]["cost"]
        # if (player["savings"] >= tools[player["tool"]]["cost"]):
        #        player["tool"] += 1
        #        player["savings"] -= tools[player["tool"]["cost"]] 
        #        print(f"Okie doke. You just bought yourself a new {}")

        ## check win

def win_conditions():
        pass ## Win conditions: a team of students and $1000 (let user know they win) -- won game will equal True and we celebrate, if not cut_lawns

get_input()