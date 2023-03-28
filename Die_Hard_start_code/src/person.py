class Person:
    def __init__(self, name, no_of_kills):
        self.name = name
        self.no_of_kills = no_of_kills
    
    def add_kill(self):
        self.no_of_kills += 1

    def check_name(self):
        if "Gennero" in self.name:
            return "Holly is using her maiden name again"
        else:
            return "Yippee Kiyaay"
        
        