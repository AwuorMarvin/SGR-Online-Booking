class Train(object):
	def __init__(self, destination, depature_time, capacity):
		self.destination = destination
		self.depature_time = depature_time
		self.capacity = capacity

		self.manifest = {}
		self.seat_numbers={}


		def create_seats():
			for s in range(1, capacity+1):
				self.seat_numbers[s] = Seats(str(s))

		def add_booking(self, seat_no, passenger):
			self.manifest[seat_no] = passenger
                 self.seat_numbers[seat_no] = True

		def update_manifest(self, seat_no, passenger):
			self.manifest[seat_no] = passenger

		def remove_from_manifest(self, seat_no, passenger):
			self.manifest[seat_no] = ""
			self.seat_numbers[seat_no] = False

		def show_available_seats(self):
			for i in self.seat_numbers:
				if i == False:
					return i

class Seats(object):
	def __init__(self):
		self.booked = False
			