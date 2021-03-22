class TaskManager:
    def __init__(self):
        self.tasks = []
        
    def parse(self, command):
        if(command[0] == "+"):
            return Action("add", command[2:])
        elif(command[0] == "-"):
            return Action("remove", command[2:])
        elif(command[0] == "x"):
            return Action("done", command[2:])
    
    
    
class Action:
    def __init__(self, name, description):
        self.name = name
        self.description = description
