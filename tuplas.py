# Tipo Tupla - Uma lista imutável

# tupla sem parenteses
tupla = "Maria", "João", "José"
print(tupla)
print(tupla[1])

# todos metodos de lista que não alteram a lista, funcionam com tuplas

# tupla especificando parenteses
tupla = ("Maria", "João", "José")
print(tupla)
print(tupla[1])

# conversão de lista para tupla
lista = ["Maria", "João", "José"]
tupla = tuple(lista)
print(tupla)

# conversão de tupla para lista
tupla = "Maria", "João", "José"
lista = list(tupla)
print(lista)
