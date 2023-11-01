# nome = "Yarles de Andrade Espirito santo"
# altura = 1.80
# peso = 80
# imc = peso / altura**2

# linha_1 = f"Nome: {nome}"
# linha_2 = f"Altura: {altura}"
# linha_3 = f"Peso: {peso}"
# linha_4 = f"IMC: {imc:.2f}"

# print(linha_1)
# print(linha_2)
# print(linha_3)
# print(linha_4)

# frase_inteira = f"{linha_1}\n{linha_2}\n{linha_3}\n{linha_4}"
# print(frase_inteira)

# frase_inteira_2_decimais = f"{linha_1}\n{linha_2}\n{linha_3}\n{linha_4:}"
# print(frase_inteira_2_decimais)

# # multiplos fStrings:
# print("multiplos Fstrings\n" f"{linha_1}\n" f"{linha_2}\n" f"{linha_3}\n" f"{linha_4}")

# # função format:
# a = "Valor A"
# b = "Valor B"
# c = "Valor C"
# numero_1 = 1.00
# # por ordem de parametros:
# str_1 = "b={}, a={}, c={}, numero_1={:.2f}"
# # por ordem de indices:
# str_2 = "b={1}, a={0}, c={2}, numero_1={3:.2f}"
# # por ordem de indices:
# str_3 = "b={letra_b}, a={letra_a}, c={letra_c}, numero_1={numero_1}"

# formato_1 = str_1.format(a, b, c, numero_1)
# formato_2 = str_2.format(b, a, c, numero_1)
# formato_3 = str_3.format(letra_a=a, letra_b=b, letra_c=c, numero_1=numero_1)

# print(formato_1, "\nordem de parametros\n")
# print(formato_2, "\nordem de indices\n")
# print(formato_3, "\nordem de indices nomeados\n")


# formatação com fStrings:

# .<numero_de_casas_decimais>f
# x e X - hexadecimal(ABCDEF123456789)
# (caracteres) (><^) (quantidade) (tipo - s, d, i, f, x, X)
# > - Esquerda
# < - Direita
# = - força o numero a aparecer antes dos zeros
# ^ - Centro
# sinal - + ou -
# ex.: 0> -100,.1f
# Conversion flags - !r !s !a

variavel = "ABC"
print(f"{variavel}")
print(f"{variavel:0>10}")  # 10 caracteres, preenchendo com 0 a esquerda
print(f"{variavel:,<10}")  # 10 caracteres, preenchendo com , a direita
print(f"{variavel:,^10}")  # 10 caracteres, preenchendo com , a esquerda e direita
print(f"{1000.4854:.2f}")  # 2 casas decimais
print(f"{1000.4854:+.2f}")  # 2 casas decimais, sinal de +
print(f"{-1000.4854:-.2f}")  # 2 casas decimais, sinal de -
print(f"{1000.4854:0=+10.2f}")  # zeros a esquerda, 2 casas decimais, sinal de +
print(f"O hexadecimal de 1000 é {1000:08X}")  # hexadecimal
