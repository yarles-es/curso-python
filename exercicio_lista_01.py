lista = ["Maria", "joão", "josé"]
indices = range(len(lista))

# usando 2 variaveis, sendo uma para pegar o range dos indices e outra para pegar o item da lista;
for indice in indices:
    print(f"O item {lista[indice]} está na posição {indice}")

# maneira com enumerate;
for index, item in enumerate(lista):
    print(f"O item {item} está na posição {index}")
