# this implementation with yield is not working

import time


class ElevatorButtonPanel:
    def __init__(self, elevator):
        self.elevator = elevator

    # Logic of the elevator
    def request_button_pressed(self, floor):
        self.elevator.go_to_floor(floor)


class Elevator:
    def __init__(self):
        self.eventlog = []

        # Python thinks it's a dict if you
        # initialize an empty set
        self.floors_to_visit = {1}
        self.floors_to_visit.remove(1)

        self.current_floor = 1
        self.going_up = True

    def keep_it_moving(self):
        while True:
            yield self.next_move()

    def next_move(self):
        print("call to next move")
        if self.floors_to_visit:
            if len(self.floors_to_visit) == 1 and self.current_floor in self.floors_to_visit:
                self.stay_on_floor()
            elif self.going_up and max(self.floors_to_visit) > self.current_floor:
                self.move_floors(1)
            else:
                self.going_up == False
                self.move_floors(-1)

    def go_to_floor(self, floor):
        self.log(f"Stop requested for floor {floor}")
        self.floors_to_visit.add(floor)
        next(self.keep_it_moving())
        time.sleep(1)

    def stay_on_floor(self):
        self.floors_to_visit.remove(self.current_floor)
        self.open_doors()

    def move_floors(self, num_floors):
        self.current_floor += num_floors
        self.log(message=f"On floor {self.current_floor}")
        self.handle_making_a_stop()

    def handle_making_a_stop(self):
        if self.current_floor in self.floors_to_visit:
            self.log(f"Stopping at floor {self.current_floor}")
            self.open_doors()
            self.floors_to_visit.remove(self.current_floor)
            print("after removing")
            print(self.floors_to_visit)

    def open_doors(self):
        self.log(f"Opening doors at floor {self.current_floor}")
        self.log(f"DOORS CLOSING")

    def log(self, message):
        self.eventlog.append(message)
        print(message)


ele = Elevator()
ebp = ElevatorButtonPanel(ele)
ebp.request_button_pressed(5)
# ebp.request_button_pressed(3)