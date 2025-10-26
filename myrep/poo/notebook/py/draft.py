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
        else:
            usados = self.__carga
            self.__carga = 0
            return usados

    def carregar(self, potencia: int, minutos: int):
        self.__carga += potencia * minutos
        if self.__carga > self.__capacidade:
            self.__carga = self.__capacidade

    def __str__(self):
        return f"({self.__carga}/{self.__capacidade})"


class Carregador:
    def __init__(self, potencia: int):
        self.__potencia = potencia

    def getPotencia(self):
        return self.__potencia

    def __str__(self):
        return f"(Potência {self.__potencia})"


class Notebook:
    def __init__(self):
        self.__ligado = False
        self.__bateria: Bateria | None = None
        self.__carregador: Carregador | None = None
        self.__minutos_usados = 0

    def ligar(self):
        if self.__ligado:
            return
        if (self.__bateria and self.__bateria.getCarga() > 0) or self.__carregador:
            self.__ligado = True
            print("notebook ligado")
        else:
            print("não foi possível ligar")

    def desligar(self):
        if self.__ligado:
            self.__ligado = False
            print("notebook desligado")

    def usar(self, minutos: int):
        if not self.__ligado:
            print("erro: notebook desligado")
            return

        while minutos > 0:
            if self.__bateria and self.__bateria.getCarga() > 0 and self.__carregador:
                self.__bateria.carregar(self.__carregador.getPotencia(), 1)
                self.__minutos_usados += 1
                minutos -= 1
            elif self.__bateria and self.__bateria.getCarga() > 0:
                usados = self.__bateria.usar(1)
                self.__minutos_usados += usados
                minutos -= usados
                if usados == 0:
                    print(f"usado {self.__minutos_usados} minutos, notebook descarregou")
                    self.__ligado = False
                    break
            elif self.__carregador:
                self.__minutos_usados += minutos
                minutos = 0
            else:
                print("erro: notebook desligado")
                self.__ligado = False
                break

    def setBateria(self, bateria: Bateria):
        self.__bateria = bateria

    def rmBateria(self):
        if self.__bateria:
            temp = self.__bateria
            print(f"bateria removida")
            self.__bateria = None
            return temp
        else:
            print("fail: sem bateria")
            return None

    def setCarregador(self, carregador: Carregador):
        if self.__carregador:
            print("fail: carregador já conectado")
        else:
            self.__carregador = carregador

    def rmCarregador(self):
        if self.__carregador:
            temp = self.__carregador
            print(f"carregador removido")
            self.__carregador = None
            return temp
        else:
            print("fail: sem carregador")
            return None

    def mostrar(self):
        status = "Ligado" if self.__ligado else "Desligado"
        parts = [f"Status: {status}"]
        parts.append(f"Bateria: {self.__bateria}" if self.__bateria else "Bateria: Nenhuma")
        parts.append(f"Carregador: {self.__carregador}" if self.__carregador else "Carregador: Desconectado")
        print(", ".join(parts))

