class Lead:
    def __init__(self, thickness: float, hardness: str, size: int):
        self.__thickness = thickness
        self.__hardness = hardness
        self.__size = size

    def getThickness(self):
        return self.__thickness
    def getHardness(self):
        return self.__hardness
    def getSize(self):
        return self.__size
    
    def setSize(self, value: int):
        self.__size = value

    def usagePerSheet(self) -> int:
        gasto = {"1B": 1, "2B": 2, "3B": 3, "4B": 4, "6B": 6}
        return gasto[self.__hardness]
    
        
    def __str__(self):
        return (f"[{self.__thickness}:{self.__hardness}:{self.__size}]")
    
class Pencil:
    def __init__(self, thickness: float):
        self.__thickness = thickness
        self.__tip: Lead | None = None

    def getLead(self):
        return self.__tip
    def setLead(self, value: Lead):
        self.__tip = value

    def hasGrafite(self) -> bool:
        if self.__tip != None:
            return True
        
    def __str__(self):
        if self.__tip == None:
            return(f"calibre: {self.__thickness}, grafite: null")
        return (f"calibre: {self.__thickness}, grafite: {self.__tip}")
    
    def insert(self, grafite: Lead):
        if self.__tip is not None:
            print("fail: ja existe grafite")
            return
        if grafite.getThickness() != self.__thickness:
            print("fail: calibre incompativel")
            return
        self.__tip = grafite

    def remove(self):
        if self.__tip == None:
            print("fail: nao existe grafite")
            return
        self.__tip = None
    
    def writePage(self):
        if self.__tip is None:
            print("fail: nao existe grafite")
            return
        
        gasto = self.__tip.usagePerSheet()
        size = self.__tip.getSize()

        if size <= 10:
            print("fail: tamanho insuficiente")
            return
        if size - gasto < 10:
            self.__tip.setSize(10)
            print("fail: folha incompleta")
            return
        self.__tip.setSize(size - gasto)

        
def main():
    pencil: Pencil | None = None
    while True:
        line = input()
        print("$" + line)
        args = line.split(" ")

        if args[0] == "end":
            break
        
        elif args[0] == "init":
            pencil = Pencil(float(args[1]))

        elif args[0] == "show":
            print(pencil)

        elif args[0] == "insert":
            grafite = Lead(float(args[1]), args[2], int(args[3]))
            pencil.insert(grafite)
        
        elif args[0] == "write":
            pencil.writePage()

        elif args[0] == "remove":
            pencil.remove()

        else:
            print("fail: comando invalido")

main()