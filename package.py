# package.py

class Package:
    def __init__(self, package_id, destination, deadline=None):
        self.id = package_id
        self.destination = destination
        self.deadline = deadline  # in HH:MM if needed
        self.status = "At hub"
        self.delivery_time = None

    def mark_delivered(self, time):
        self.delivery_time = time
        if self.deadline and time > self.deadline:
            self.status = "Late"
        else:
            self.status = "Delivered"
