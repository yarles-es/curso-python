# desempacotamento:
list_names = ["João", "Maria", "José", "Ana"]
nome1, nome2, nome3, nome4 = list_names
print(nome1, nome2, nome3, nome4)

# desempacotamento com tuplas:
tuple_names = ("João", "Maria", "José", "Ana")
nome1, nome2, nome3, nome4 = tuple_names
print(nome1, nome2, nome3, nome4)

# desempacotamento com dicionários:
dict_names = {"nome1": "João", "nome2": "Maria", "nome3": "José", "nome4": "Ana"}
nome1, nome2, nome3, nome4 = dict_names.values()
print(nome1, nome2, nome3, nome4)

# usando resto:
list_names = ["João", "Maria", "José", "Ana"]
nome1, *resto = list_names
print(nome1, resto)

# usando resto que não é utilizado:
list_names = ["João", "Maria", "José", "Ana"]
nome1, *_ = list_names
print(nome1)
