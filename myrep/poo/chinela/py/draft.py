class Chinela:
    def __init__(self):
        self.__tamanho: int = 0

    def getTamanho(self):
        return self.__tamanho
    
    def setTamnho(self, valor: int):
        if valor > 50 or valor < 20:
            print("Tamanho não existe")
            return 
        if valor % 2 == 1:
            print("Falha, Não existem tamanhos ímpares")
            return
        self.__tamanho = valor
    
def main():
    chinela = Chinela()

    while chinela.getTamanho() == 0:
        print("Digite seu tamano de chinela")
        tamanho = int(input())
        chinela.setTamnho(tamanho)

    print("Parabéns, você comprou uma chinela tamanho", chinela.getTamanho())

main()