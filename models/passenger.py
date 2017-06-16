class Passenger:
    def __init__(self, fname, lname):
        self.first_name = fname
        self.last_name = lname
        
    def get_name(self):
        return self.first_name + self.last_name