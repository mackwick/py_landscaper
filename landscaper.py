# some_number = int(input("Give me some number: "))

## Player Stuff
tools = [{"name": "teeth", "cost": 0, "income": 1}, {"name": "rusty scissors", "cost": 5, "income": 5}, {"name": "push mower", "cost": 25, "income": 50}, {"name": "fancy mower", "cost": 250, "income": 100}, {"name": "underpaid team", "cost": 500, "income": 250}]

tool_index = 0

player = {"tool": tools[tool_index]["name"], "savings": 0, "won game": False}






## Functions

def cut_lawns():
        pass ## When player savings >= the cost of the tool at the current index +1, they can choose to buy a tool or keep cutting lawns

def buy_tool():
        pass ## If player buys a tool, tool index +1, and savings - tool[index]["cost"]

def win_conditions():
        pass ## Win conditions: a team of students and $1000 (let user know they win) -- won game will equal True and we celebrate, if not cut_lawns