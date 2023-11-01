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
