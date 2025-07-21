# truck.py

class Truck:
    def __init__(self, truck_id, start_city="Hub", capacity=5):
        self.id = truck_id
        self.current_city = start_city
        self.capacity = capacity
        self.packages = []
        self.route = []
        self.total_distance = 0

    def assign_packages(self, packages):
        self.packages = packages[:self.capacity]

    def set_route(self, route, distance):
        self.route = route
        self.total_distance = distance
