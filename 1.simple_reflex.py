environment = {
    "A": "Dirty",
    "B": "Dirty"
}

location = "A"

def simple_reflex(location, status):
    if status == "Dirty":
        return "Suck"
    elif location == "A":
        return "Right"  
    else:
        return "Left"

def execute_action(environment, location, action):
    if action == "Suck":
        environment[location] = "CLEAN" 

    elif action == "Right":            
        location = "B"

    elif action == "Left":             
        location = "A"

    return environment, location

def display_environment(environment, location, action):
    print("Action:", action)
    print("Current Location:", location)
    print("Room A:", environment["A"])
    print("Room B:", environment["B"])

def run_agent():
    global location

    while not (
         environment["A"] == "CLEAN" 
         and environment["B"] == "CLEAN"
    ):
        status = environment[location]
        action = simple_reflex(location, status)
        environment_new, location_new = execute_action(environment, location, action)
        location = location_new
        display_environment(environment, location, action)

    print("Both rooms are clean!")
    print("Goal achieved.")

run_agent()