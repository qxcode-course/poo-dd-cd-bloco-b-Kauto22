class Bateria:
    def __init__(self, capacidade: int):
        self.__capacidade = capacidade
        self.__carga = capacidade

    def getCarga(self):
        return self.__carga

    def getCapacidade(self):
        return self.__capacidade

    def usar(self, minutos: int):
        if self.__carga >= minutos:
            self.__carga -= minutos
            return minutos
        usados = self.__carga
        self.__carga = 0
        return usados

    def carregar(self, potencia: int, minutos: int):
        self.__carga += potencia * minutos
        if self.__carga > self.__capacidade:
            self.__carga = self.__capacidade

    def __str__(self):
        return f"{self.__carga}/{self.__capacidade}"


class Carregador:
    def __init__(self, potencia: int):
        self.__potencia = potencia

    def getPotencia(self):
        return self.__potencia

    def __str__(self):
        return f"{self.__potencia}W"


class Notebook:
    def __init__(self):
        self.__ligado = False
        self.__bateria: Bateria | None = None
        self.__carregador: Carregador | None = None
        self.__tempo_ligado = 0

    def turn_on(self):
        if self.__ligado:
            return
        if (self.__bateria and self.__bateria.getCarga() > 0) or self.__carregador:
            self.__ligado = True
        else:
            print("fail: não foi possível ligar")

    def turn_off(self):
        self.__ligado = False

    def use(self, minutos: int):
        if not self.__ligado:
            print("fail: desligado")
            return

        while minutos > 0:
            if self.__bateria and self.__bateria.getCarga() > 0:
                if self.__carregador:
                    self.__bateria.carregar(self.__carregador.getPotencia(), 1)
                usados = self.__bateria.usar(1)
                self.__tempo_ligado += usados
                minutos -= usados
                if self.__bateria.getCarga() == 0 and minutos > 0 and not self.__carregador:
                    print("fail: descarregou")
                    self.__ligado = False
                    break
            elif self.__carregador:
                self.__tempo_ligado += minutos
                minutos = 0
            else:
                print("fail: descarregou")
                self.__ligado = False
                break

    def setBateria(self, bateria: Bateria):
        self.__bateria = bateria

    def rmBateria(self):
        if self.__bateria:
            temp = self.__bateria
            print(f"Removido {self.__bateria}")
            self.__bateria = None
            if not self.__carregador:
                self.__ligado = False
            return temp
        else:
            print("fail: Sem bateria")
            return None

    def setCharger(self, carregador: Carregador):
        if self.__carregador:
            print("fail: carregador já conectado")
        else:
            self.__carregador = carregador

    def rmCharger(self):
        if self.__carregador:
            temp = self.__carregador
            print(f"Removido {self.__carregador}")
            self.__carregador = None
            if not (self.__bateria and self.__bateria.getCarga() > 0):
                self.__ligado = False
            return temp
        else:
            print("fail: Sem carregador")
            return None

    def show(self):
        estado = f"Notebook: {'ligado por ' + str(self.__tempo_ligado) + ' min' if self.__ligado else 'desligado'}"
        if self.__carregador:
            estado += f", Carregador {self.__carregador}"
        if self.__bateria:
            estado += f", Bateria {self.__bateria}"
        print(estado)


def main():
    notebook = Notebook()
    bateria = None
    carregador = None

    while True:
        line = input()
        print("$" + line)
        args = line.split(" ")

        if args[0] == "end":
            break
        elif args[0] == "show":
            notebook.show()
        elif args[0] == "turn_on":
            notebook.turn_on()
        elif args[0] == "turn_off":
            notebook.turn_off()
        elif args[0] == "use":
            notebook.use(int(args[1]))
        elif args[0] == "set_battery":
            bateria = Bateria(int(args[1]))
            notebook.setBateria(bateria)
        elif args[0] == "rm_battery":
            notebook.rmBateria()
        elif args[0] == "set_charger":
            carregador = Carregador(int(args[1]))
            notebook.setCharger(carregador)
        elif args[0] == "rm_charger":
            notebook.rmCharger()
        else:
            print("fail: comando invalido")


main()
