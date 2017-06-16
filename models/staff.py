"""Module holds the model of the staff of the Madaraka project"""


class Staff(object):
    """class for our staff model"""

    def __init__(self, name):
        self.name = name

    def get_manifest(self, train):
        manifest_list = train.manifest
        return manifest_list


# class Train(object):

#     def __init__(self, name, seat):
#         self.name = name
#         self.seat = seat
#         self.manifest = {}

#     def add_passenger(self, passenger):
#         self.manifest[self.seat] = passenger.name


# class Pass():

#         def __init__(self, name):
#             self.name = name


# pass_1 = Pass('Lynn')
# train_1 = Train('Train_1', 'Seat_1')
# staff_1 = Staff('staff_1')

# train_1.add_passenger(pass_1)
# print(staff_1.get_manifest(train_1))

