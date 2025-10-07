class Camisa:
    def __init__(self):
        self.__tamanho: str = ""

    def getTamanho(self) -> str:
        return self.__tamanho
    
    def setTamanho(self, valor: str):
        if valor != "PP" and valor != "P" and valor != "M" and valor != "G" and valor != "GG" and valor != "XG":
            print("Tamanho inválido")
        else:
            self.__tamanho = valor


def main():
    camisa = Camisa()

    while camisa.getTamanho() == "":
        print("Digite seu tamanho de roupa")
        tamanho = input().upper()
        if camisa.setTamanho(tamanho) == True:
            break

    print("Parabéns, você comprou uma roupa tamanho", camisa.getTamanho())

main()

