# Simulation of an elevator
# this implementation does not allow stops in the middle of a journey
# Simulation of an elevator

class Elevator:
    def __init__(self, nr_floors):
        self.nr_floors = nr_floors
        # always start on the first floor
        self.current_floor = 1
        # flag to indicate if the elevator is:
        #   1 moving up
        #   0 stopped
        #   -1 moving down
        self.moving = 0
        # needs to be a set (no repeated elements)
        self.stops = ()

    def elevator_called(self, floor):
        '''
        :param floor: floor where the elevator is called
        '''
        print("Elevator called at floor {}".format(floor))
        # travel from current floor towards where the elevator
        # has been called
        # this action has a lower priority than the action
        # requested from a passanger inside the elevator
        if self.moving == 0:
            # transform into a high priority action
            self.button_pressed(floor)
        elif self.moving == 1 and floor > self.current_floor:
            # add stop on the journey
            print("Stop added")
            self.stops.adds(floor)

        elif self.moving == -1 and floor < self.current_floor:
            # add stop on the journey
            print("Stop added")
            self.stops.adds(floor)
        # otherwise the request is ignored
        return

    def button_pressed(self, floor):
        '''
        :param floor: floor button pressed inside the elevator
        '''
        print("Request to travel to floor {}".format(floor))
        # This is the action that has the highest priority
        # lock the elevator
        while self.current_floor != floor:
            self.current_floor = self.next_move(floor)
            print("Passing floor {}".format(self.current_floor))
            self.check_stops()

        print("Arrived to floor {}".format(self.current_floor))
        self.open_doors(self.current_floor)
        self.moving = 0
        return

    def next_move(self, floor):
        if self.current_floor < floor:
            self.moving = 1
            return (self.current_floor + 1)
        self.moving = -1
        return (self.current_floor - 1)

    def check_stops(self):
        if len(self.stops) > 0:
            if self.current_floor in self.stops:
                self.open_doors(self.current_floor)
                self.stops.remove(self.current_floor)
        return

    def open_doors(self, floor):
        '''
        Informative method logging where the doors has been opened
        :param floor: floor where the doors are open
        '''
        print("Doors opening at {}".format(floor))
        return


ele = Elevator(5)
ele.elevator_called(2)
ele.button_pressed(5)
ele.elevator_called(4)
