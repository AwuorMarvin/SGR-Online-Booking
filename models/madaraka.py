from train import Train
from passenger import Passenger
class Madaraka:
    train = Train("Mombasa", "10 am", 15)
    train.create_seats()
    def book_seat(self, fname, lname, seat_no):
        passenger = Passenger(fname, lname)
        name = passenger.get_name()
        train.add_booking(int(seat_no), name)
    
    def retrieve_manifest(self):
        pass