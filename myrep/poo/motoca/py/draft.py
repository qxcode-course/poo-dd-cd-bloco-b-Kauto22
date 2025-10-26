
class Pessoa:
    def __init__(self, name: str, age: int):
        self.__name = name
        self.__age = age

    def getName(self):
        return self.__name
    def getAge(self):
        return self.__age
    
    def setName(self, value: str):
        self.__name = value
    def setAge(self, value: int):
        self.__age = value
    
    
    def __str__(self):
        return (f"{self.__name}:{self.__age}")

class Moto:
    def __init__(self, power: int):
        self.__power = power
        self.__time = 0
        self.__person: Pessoa | None = None
    
    def __str__(self):
        if self.__person is None:
            person_str = "(empty)"
        else: 
            person_str = f"({self.__person})"
        return (f"power:{self.__power}, time:{self.__time}, person:{person_str}")
    
    def getPower(self):
        return self.__power
    
    def getTime(self):
        return self.__time
    
    def getPerson(self):
        return self.__person
    
    def insertPerson(self, person: Pessoa) -> bool:
        if self.__person != None:
            print("fail: busy motorcycle")
            return False
        self.__person = person
        return True
        
    def remove(self) -> Pessoa | None:
        if self.__person == None:
            print("fail: empty motorcycle")
            return None
        else:
            aux: Pessoa = self.__person
            self.__person = None
            return aux
        
    def buyTime(self, time: int):
        self.__time += time

    def drive(self, time: int):
        if self.__time == 0:
            print("fail: buy time first")
            return
        if self.__person == None:
            print("fail: empty motorcycle")
            return
        if self.__person.getAge() > 10:
            print("fail: too old to drive")
            return
        if time > self.__time:
            print(f"fail: time finished after {self.__time} minutes")
            self.__time = 0
            return
        self.__time -= time

    def honk(self):
        print("P" + ("e" * self.__power) + "m")
    
        
        
def main():
    moto = Moto(1)
    while True:
        line = input()
        print("$" + line)
        args = line.split(" ")

        if args[0] == "end":
            break

        elif args[0] == "init":
            moto = Moto(int(args[1]))
        
        elif args[0] == "show":
            print(moto)
        
        elif args[0] == "enter":
            moto.insertPerson(Pessoa(args[1], int (args[2])))
        
        elif args[0] == "leave":
            p = moto.remove()
            if p is not None:
                print(p)

        elif args[0] == "buy":
            moto.buyTime(int(args[1]))

        elif args[0] == "drive":
            (moto.drive(int(args[1])))

        elif args[0] == "honk":
            moto.honk()

        else:
            print("fail: comando invalido")

main()
    

