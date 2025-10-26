class Roupa:
    def __init__(self):
        self.__tamanho: str = ""

    def getTamanho(self) -> str:
        return self.__tamanho

    def setTamanho(self, valor: str) -> bool:
        if valor not in ["PP", "P", "M", "G", "GG", "XG"]:
            print("fail: Valor inválido, tente PP, P, M, G, GG ou XG")
            return False
        self.__tamanho = valor
        return True

    def show(self):
        print(f"size: ({self.__tamanho})")


def main():
    roupa = Roupa()

    while True:
        line = input()
        print("$" + line)
        args = line.split()

        if args[0] == "end":
            break

        elif args[0] == "show":
            roupa.show()

        elif args[0] == "size":
            if len(args) < 2:
                print("fail: faltou o tamanho (PP, P, M, G, GG, XG)")
                continue
            roupa.setTamanho(args[1].upper())

        else:
            print("fail: comando invalido")


main()
