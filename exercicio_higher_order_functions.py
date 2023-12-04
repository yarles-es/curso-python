# Crie funçõesq ue duplicam, triplicam e quadruplicam um número


def criar_multiplicador(multiplicador):
    def multiplicador_de_numero(numero):
        return numero * multiplicador

    return multiplicador_de_numero


duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

print(duplicar(2))
print(triplicar(2))
print(quadruplicar(2))


def criar_divisor(divisor):
    def divisor_de_numero(numero):
        return numero / divisor

    return divisor_de_numero


# def criar_calculador(operador, valor):
def criar_calculador(operador, valor):
    def calculador(numero):
        if operador == "+":
            return numero + valor
        elif operador == "-":
            return numero - valor
        elif operador == "*":
            if numero == 0:
                return "Multiplicação por zero não permitida"
            return numero * valor
        elif operador == "/":
            if numero == 0:
                return "Divisão por zero não permitida"
            result = numero / valor
            if result.is_integer():
                return int(result)
            return result

    return calculador


dividir_por_algo = criar_calculador("/", 2)
print(dividir_por_algo(10))

multiplicar_por_algo = criar_calculador("*", 2)
print(multiplicar_por_algo(10))

somar_com_algo = criar_calculador("+", 2)
print(somar_com_algo(10))

subtrair_com_algo = criar_calculador("-", 2)
print(subtrair_com_algo(10))
