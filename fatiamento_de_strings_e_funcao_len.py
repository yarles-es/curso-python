"""
Fatiamento de strings
 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p] [::]
Obs.: a função len retorna a qtd 
de caracteres da str
"""
variavel = "Olá mundo"
print(variavel[4:8])  # [i:f] indice inicial e final especificados
print(variavel[4:])  # [i:] indice inicial especificado
print(variavel[:4])  # [:f] indice final especificado
print(variavel[-8:-2])  # [-i:-f] indice inicial e final especificados negativos
print(variavel[0:9:2])  # [i:f:p] indice inicial, final e passo especificados
print(
    variavel[::-1]
)  # [-i:-f:-p] indice inicial, final e passo especificados negativos

# exercicios
nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")

if not nome or not idade:
    print("Desculpe, você deixou campos vazios")
else:
    print(f"Seu nome é {nome}")
    print(f"Seu nome invertido é {nome[::-1]}")
    print(f"Seu nome {' ' in nome and 'tem espaços' or 'não tem espaços'}")
    print(f"Seu nome tem {len(nome)} letras")
    print(f"Ultima letra do seu nome é {nome[- 1]}")
