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
        print(f"You earned ${tools[player['tool']]['income']} cutting lawns with your {tools[player['tool']]['name']} today.")
        player["savings"] += tools[player['tool']]['income']
        win_conditions()

        

def buy_tool():
        print("buying a tool") 
        ## If player buys a tool, tool index +1, and savings - tool[index]["cost"]
        # if (player["savings"] >= tools[player["tool"]]["cost"]):
        #        player["tool"] += 1
        #        player["savings"] -= tools[player["tool"]["cost"]] 
        #        print(f"Okie doke. You just bought yourself a new {}")

        ## check win

def win_conditions():
        if (player["savings"] >= 1000 and player["tool"] == 4):
                print(f"Congratulations! You have ${player['savings']} and a {tools[player['tool']]['name']}. You're a vital part of the broken capitalist system. You win!")
        else:
                print(f"You have saved ${player['savings']}. Nice job. Get some rest so you can work more tomorrow!")
                get_input()


get_input()