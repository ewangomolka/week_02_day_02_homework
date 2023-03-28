
class Bus:
    def __init__(self, route_number, destination):
        self.route_number = route_number
        self.destination = destination
        self.passengers = []

    
    def drive(self):
        return "Brum brum"
    
    def passenger_count(self):
        return len(self.passengers)
    
    def pick_up(self, person):
        self.passengers.append(person)
    
    def drop_off(self, person):
        self.passengers.remove(person)

    def empty_bus(self):
        self.passengers.clear()

    def pick_up_from_stop(self, bus_stop_to_pick_up_from):
        for passenger in bus_stop_to_pick_up_from.queue:
            self.passengers.append(passenger)
        bus_stop_to_pick_up_from.clear_queue()



    