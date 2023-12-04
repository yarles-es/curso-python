# enumerate - enumerate interáveis (índices)

lista = ["Maria", "joão", "josé"]

lista_enumerada = enumerate(lista)

for item in lista_enumerada:
    print(item)

# apos o for, o enumerate é esvaziado, por isso não imprime nada
for item in lista_enumerada:
    print(item)


# para imprimir novamente, é necessário criar novamente o enumerate
lista_enumerada = enumerate(lista)
for item in lista_enumerada:
    print(item)

# maneira mais facil de acessar enumerate diretamente no for
for index, item in enumerate(lista):
    print(f"O item {item} está na posição {index}")

# transformar enumerate em lista
lista_enumerada = list(enumerate(lista))
print(lista_enumerada)
