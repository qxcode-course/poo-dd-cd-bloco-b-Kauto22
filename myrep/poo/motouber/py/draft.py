class Driver():
    def __init__(self, drivername: str, drivermoney: int):
        self.__drivername = drivername
        self.__drivermoney = drivermoney

    def getDriverName(self):
        return self.__drivername
    def getDriverMoney(self):
        return self.__drivermoney
        
    def setDriverName(self, value: str):
        self.__drivername = value
    def setDriverMoney(self, value: int):    
        self.__drivermoney = value

class Passenger():
    def __init__(self, passengername: str, passengermoney: int):
        self.__passengername = passengername
        self.__passengermoney = passengermoney

    def getPassengerName(self):
        return self.__passengername
    def getPassengerMoney(self):
        return self.__passengermoney
        
    def setPassengerName(self, value: str):
        self.__passengername = value
    def setPassengerMoney(self, value: int):    
        self.__passengermoney = value

class Moto():
    def __init__(self):
        self.__driver: Driver | None = None
        self.__passenger: Passenger | None = None
        self.__cost: int = 0
    
    def __str__(self):
        driver_str = f"{self.__driver.getDriverName()}:{self.__driver.getDriverMoney()}"if self.__driver else "None"
        passenger_str = f"{self.__passenger.getPassengerName()}:{self.__passenger.getPassengerMoney()}" if self.__passenger else "None"
        return f"Cost: {self.__cost}, Driver: {driver_str}, Passenger: {passenger_str}"

    def getDriver(self):
        return self.__driver
    def getPassenger(self):
        return self.__passenger
    def getCost(self):
        return self.__cost
    
    def setDriver(self, driver: Driver):
        self.__driver = driver
    def setPassenger(self, passenger: Passenger):
        if self.__driver is None:
            print("fail: no driver")
            return
        self.__passenger = passenger

    def enter(self, p: Passenger):
        if self.__driver is None:
            print("fail: no driver")
            return
        self.__passenger = p

    def drive(self, km: int):
        if self.__driver is None or self.__passenger is None:
            print("fail: cannot drive")
            return
        self.__cost += km
    
    def leavePassenger(self):
        if self.__passenger is None:
            print("fail: no Passenger")
            return
        payment = min(self.__passenger.getPassengerMoney(), self.__cost)
        self.__passenger.setPassengerMoney(self.__passenger.getPassengerMoney() - payment)
        self.__driver.setDriverMoney(self.__driver.getDriverMoney() + self.__cost)


        if payment < self.__cost:
            print("fail: Passenger does not have enough money")
            
        print(f"{self.__passenger.getPassengerName()}:{self.__passenger.getPassengerMoney()} left")
        self.__passenger = None
        self.__cost = 0
        
def main():
    moto = Moto()
    while True:
        line = input()
        print("$" + line)
        args = line.split(" ")

        if args[0] == "end":
            break
        elif args[0] == "show":
            print(moto)

        elif args[0] == "setDriver":
            moto.setDriver(Driver(args[1], int(args[2])))

        elif args[0] == "setPass":
            moto.setPassenger(Passenger(args[1], int(args[2])))
        
        elif args[0] == "drive":
            moto.drive(int(args[1]))

        elif args[0] == "leavePass":
            moto.leavePassenger()


        else:
            print("fail: comando invalido")

main()

    
        