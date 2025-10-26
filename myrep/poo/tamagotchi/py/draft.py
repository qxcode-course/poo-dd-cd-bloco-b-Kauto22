class Tamagotchi:
    def __init__(self, energyMax: int, cleanMax: int):
        self.__energyMax = energyMax
        self.__cleanMax = cleanMax
        self.__energy: int = energyMax
        self.__clean: int = cleanMax
        self.__age: int = 0
        self.__alive: bool = True

    def getEnergyMax(self):
        return self.__energyMax
    def getCleanMax(self):
        return self.__cleanMax
    def getEnergy(self):
        return self.__energy
    def getClean(self):
        return self.__clean
    def getAge(self):
        return self.__age
    def getAlive(self):
        return self.__alive

    def setEnergy(self, value: int):
        if value <= 0:
            self.__energy = 0
            self.__alive = False
            print("fail: pet morreu de fraqueza")
        elif value > self.__energyMax:
            self.__energy = self.__energyMax
        else:
            self.__energy = value

    def setClean(self, value: int):
        if value <= 0:
            self.__clean = 0
            self.__alive = False
            print("fail: pet morreu de sujeira")
        elif value > self.__cleanMax:
            self.__clean = self.__cleanMax
        else:
            self.__clean = value
    
    def setAge(self, value: int):
        self.__age = value
        
    def __str__(self):
        return (f"E:{self.__energy}/{self.__energyMax}, L:{self.__clean}/{self.__cleanMax}, I:{self.__age}")
    
class Game:
    def __init__(self, tamagotchi: Tamagotchi):
        self.__tamagotchi = tamagotchi

    def play(self):
        pet = self.__tamagotchi
        if not pet.getAlive():
            print("fail: pet esta morto")
            return
        pet.setEnergy(pet.getEnergy() - 2)
        pet.setClean(pet.getClean() - 3)
        pet.setAge(pet.getAge() + 1)

    def sleep(self):
        pet = self.__tamagotchi
        if not pet.getAlive():
            print("fail: pet esta morto")
            return
        if pet.getEnergy() <= pet.getEnergyMax() - 5: 
            pet.setAge(pet.getAge() + (pet.getEnergyMax() - pet.getEnergy()))
            pet.setEnergy(pet.getEnergyMax())
            return
        print("fail: nao esta com sono")

    def shower(self):
        pet = self.__tamagotchi
        if not pet.getAlive():
            print("fail: pet esta morto")
            return
        pet.setEnergy(pet.getEnergy() - 3)
        pet.setClean(pet.getCleanMax())
        pet.setAge(pet.getAge() + 2)

    def __str__(self):
        return str(self.__tamagotchi)

def main():
    tamagotchi = None
    game = None
    while True:
        line = input()
        print("$" + line)
        args = line.split(" ")

        if args[0] == "end":
            break

        elif args[0] == "init":
            tamagotchi = Tamagotchi(int(args[1]), int(args[2]))
            game = Game(tamagotchi)

        elif args[0] == "show":
            print(game)
        
        elif args[0] == "play":
            game.play()

        elif args[0] == "sleep":
            game.sleep()

        elif args[0] == "shower":
            game.shower()

        else:
            print("fail: comando invalido")

main()