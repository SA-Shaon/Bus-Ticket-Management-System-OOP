"""
    Bus Ticket Reservation System
    User --> 
        UserName
        Password

    Admin -->
        Driver
        No
        Form
        To
    UserList
    Bus_schedule
"""


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password


class Bus:
    def __init__(self, coach, driver, arrival, departure, from_des, to):
        self.coach = coach
        self.driver = driver
        self.arrival = arrival
        self.departure = departure
        self.from_des = from_des
        self.to = to
        self.seat = ["Empty" for i in range(20)]


class Bus_Company:  # Bus install for admin
    total_bus = 5
    total_bus_list = []  # Dummy Database

    def install(self):
        bus_no = int(input("Enter Bus No : "))
        flag = 1
        for bus in self.total_bus_list:
            if bus_no == bus['coach']:
                print("Bus already installed")
                flag = 0
                break
        if flag:
            bus_driver = input("Enter Bus Driver Name : ")
            bus_arriaval = input("Enter Bus Arrival Time : ")
            bus_departure = input("Enter Bus Departure Time : ")
            bus_from = input("Enter Bus Start From : ")
            bus_to = input("Enter Bus Destination To : ")
            self.new_bus = Bus(bus_no, bus_driver, bus_arriaval,
                               bus_departure, bus_from, bus_to)
            self.total_bus_list.append(vars(self.new_bus))
            print("Bus installed Successfully\n")


class BusCounter(Bus_Company):
    user_list = []  # user database
    bus_seat = 20

    def revervation(self):
        bus_no = int(input("Enter Bus Number : "))
        for bus in self.total_bus_list:
            if bus_no == bus['coach']:
                passenger = input("Enter Your name : ")
                seat_no = int(input("Enter Your Seat Number : "))
                if seat_no - 1 > self.bus_seat:  # maximum seat checking
                    print("Only 20 seats are available")
                elif bus['seat'][seat_no-1] != "Empty":  # not empty kina
                    print("Seat Already Booked")
                else:  # oi seat e oi user ke bosiye dicchi
                    bus['seat'][seat_no-1] = passenger
            else:
                print("No Bus Available")


bus = Bus_Company()
bus.install()
print(bus.total_bus_list)
