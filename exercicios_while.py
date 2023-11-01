name = input("digite seu nome: ")

if not name:
    print("campo vazio")
else:
    caractere = 1
    length_nome = len(name)
    new_name = ""
    while caractere <= length_nome:
        if caractere == 1 or caractere == length_nome:
            if caractere == 1:
                new_name += name[caractere - 1].upper()
            else:
                new_name += f"{name[caractere - 1]}"
        else:
            new_name += f"*{name[caractere - 1]}"

        caractere += 1
    print(new_name)
