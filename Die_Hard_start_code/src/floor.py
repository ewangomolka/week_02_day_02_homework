class Floor:
    def __init__(self):
        self.people = []

    def floor_count(self):
        return len(self.people)
    
    def add_person(self, person):
        self.people.append(person)

    def remove_person(self, person):
        self.people.remove(person)
