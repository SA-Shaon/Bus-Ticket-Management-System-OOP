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
            print("\nBus installed Successfully\n")


class BusCounter(Bus_Company):
    user_list = []  # user database
    bus_seat = 20

    def reservation(self):
        bus_no = int(input("Enter Bus Number : "))
        flag = 1
        for bus in self.total_bus_list:
            if bus_no == bus['coach']:
                flag = 0
                passenger = input("Enter Your name : ")
                seat_no = int(input("Enter Your Seat Number : "))
                if seat_no - 1 > self.bus_seat:  # maximum seat checking
                    print("Only 20 seats are available")
                elif bus['seat'][seat_no-1] != "Empty":  # not empty kina
                    print("Seat Already Booked")
                else:  # oi seat e oi user ke bosiye dicchi
                    bus['seat'][seat_no-1] = passenger
                    print(f"\nSeat no-{seat_no} successfully booked")
        if flag == 1:
            print("No Bus Available")

    def showBusInfo(self):
        bus_no = int(input('Enter Bus No : '))
        for bus in self.total_bus_list:
            if bus['coach'] == bus_no:
                print('*'*50)
                print()
                print(f"{' '*10} {'#'*10} BUS INFO {'#'*10}")
                print(f"Bus Number : {bus_no} \t\t Driver : {bus['driver']}")
                print(
                    f"Arrival : {bus['arrival']} \t\t\t Departure : {bus['departure']}")
                print(f"From : {bus['from_des']} \t\t\t To : {bus['to']}")
                print()
                a = 1
                for i in range(5):
                    for j in range(2):
                        print(f"{a}. {bus['seat'][a-1]}", end="\t")
                        a += 1
                    print("\t", end="")
                    for j in range(2):
                        print(f"{a}. {bus['seat'][a-1]}", end="\t")
                        a += 1
                    print()

    def get_users(self):
        return self.user_list

    def create_accout(self):
        name = input("Enter your name : ")
        flag = 0
        for user in self.get_users():
            if user['username'] == name:
                print("Username already exists")
                flag = 1
                break
        if flag == 0:
            password = input("Enter your passwoard : ")
            self.new_user = User(name, password)
            self.user_list.append(vars(self.new_user))
            print("\nAccount Created successfully\n")

    def available_buses(self):
        if len(self.total_bus_list) == 0:
            print("\nNO Bus Available\n")
        else:
            for bus in self.total_bus_list:
                print('*'*50)
                print()
                print(f"{' '*10} {'#'*10} BUS INFO {bus['coach']} {'#'*10}")
                print(
                    f"Bus Number : {bus['coach']} \t\t Driver : {bus['driver']}")
                print(
                    f"Arrival : {bus['arrival']} \t\t\t Departure : {bus['departure']}")
                print(f"From : {bus['from_des']} \t\t\t To : {bus['to']}")
                print()
                a = 1
                for i in range(5):
                    for j in range(2):
                        print(f"{a}. {bus['seat'][a-1]}", end="\t")
                        a += 1
                    print("\t", end="")
                    for j in range(2):
                        print(f"{a}. {bus['seat'][a-1]}", end="\t")
                        a += 1
                    print()


"""
    1.Create an account -> 
    2.Login to  your account -> authentic user
                                -> Available buses
                                -> Reservation
                                -> Show bus info

                             -> Administrator
                                -> Install Buses
                                -> See available buses
                                -> See total userList

    3.exit
"""
while True:
    counter = BusCounter()
    print("1. Create An Account \n2. Login To your Account \n3.EXIT")
    user_input = int(input("Enter your choice : "))
    if user_input == 3:
        break
    elif user_input == 1:
        counter.create_accout()
    elif user_input == 2:
        name = input("Enter your name : ")
        password = input("Enter your password : ")
        isAdmin = False
        flag = 0
        if name == "admin" and password == "123":
            isAdmin = True
        if isAdmin == False:
            for user in counter.get_users():
                if user['username'] == name and user['password'] == password:
                    flag = 1
                    break
            if flag == 1:
                while True:
                    print(
                        "1. Available Buses \n2. Show Bus Info \n3. Reservation \n4.EXIT")
                    a = int(input("Enter Your Choice : "))
                    if a == 4:
                        break
                    elif a == 1:
                        counter.available_buses()
                    elif a == 2:
                        counter.showBusInfo()
                    elif a == 3:
                        counter.reservation()
            else:
                print("\nDon't have account? Create an Account.\n")
        else:
            while True:
                print("Hello Admin, Welcome back")
                print(
                    "1. Install Bus \n2. Available Buses \n3. Show Bus \n4. Show User List \n5. Exit")
                a = int(input("Enter Your Choice : "))
                if a == 5:
                    break
                elif a == 1:
                    counter.install()
                elif a == 2:
                    counter.available_buses()
                elif a == 3:
                    counter.showBusInfo()
                elif a == 4:
                    print(counter.get_users())

# Successfully Complete my project