class NakatomiPlaza:
    def __init__(self, floor1, floor2, floor3):
        self.floor1 = floor1
        self.floor2 = floor2
        self.floor3 = floor3

    def add_to_floor(self, floor, badguy):
        floor.add_person(badguy)

    def smoke_em_like_it_aint_no_thang(self, john, floor):
        badguys_on_floor = floor.floor_count()
        if badguys_on_floor == floor:
            john.add_kill(badguys_on_floor)
            floor.remove_person(badguys_on_floor)
            
                
	        
            
                      

            

    # def weave(self, other):
    # result = CoordinateRow()
    # for a, b in zip(self.coordinate_row, other.coordinate_row):
    #     result.add(a)
    #     result.add(b)