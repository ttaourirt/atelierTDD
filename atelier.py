class TaskManager:
    def __init__(self):
        self.tasks = []
        
    def parse(self, command):
        return Action("add", command[2:])
    
    
    
class Action:
    def __init__(self, name, description):
        self.name = name
        self.description = description