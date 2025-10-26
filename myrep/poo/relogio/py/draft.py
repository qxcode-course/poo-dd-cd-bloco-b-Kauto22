class Watch:
    def __init__(self, hour: int = 0, minute: int = 0, second: int = 0):
        self.__hour: int = 0
        self.__minute: int = 0
        self.__second: int = 0
        self.setHour(hour)
        self.setMinute(minute)
        self.setSecond(second)

    def __str__(self):
        return(f"{self.__hour:02d}:{self.__minute:02d}:{self.__second:02d}")
    
    def getHour(self):
        return self.__hour
    
    def getMinute(self):
        return self.__minute
    
    def getSecond(self):
        return self.__second
    
    def setHour(self, value: int):
        if 0 <= value <= 23:
            self.__hour = value
        else:
            print("fail: hora invalida")

    def setMinute(self, value: int):
        if 0 <= value <= 59:
            self.__minute = value
        else:
            print("fail: minuto invalido")


    def setSecond(self, value: int):
        if 0 <= value <= 59:
            self.__second = value
        else: 
            print("fail: segundo invalido")

    def nextSecond(self):
        self.__second += 1
        if self.__second > 59:
            self.__second = 0
            self.__minute += 1
        if self.__minute > 59:
            self.__minute = 0
            self.__hour += 1
        if self.__hour > 23:
            self.__hour = 0

def main():
    watch = Watch()
    while True:
        line = input()
        print("$" + line)
        args = line.split(" ")

        if args[0] == "end":
            break
        
        elif args[0] == "show":
            print(watch)

        elif args[0] == "set":
            h, m, s = map(int, args[1:])
            watch.setHour(h)
            watch.setMinute(m)
            watch.setSecond(s)

        elif args[0] == "next":
            watch.nextSecond()

        elif args[0] == "init":
            h, m, s = map(int, args[1:])
            watch = Watch(h, m, s)
        else:
            print("fail: comando invalido")

main()
    