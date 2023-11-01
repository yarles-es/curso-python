# s - string
# d e i - inteiros
# f - float
# x e X - hexadecimal(ABCDEF123456789)

nome = "Yarles de Andrade Espirito santo"
preco = 1500
varivavel = "%s, o preço é R$ %.2f" % (nome, preco)
print(varivavel)

# mostra os 8 caracteres do hexadecimal
# é mais comom hexadecimal de 4 e 8 caracteres
print("O hexadecimal de %d é %08X" % (preco, preco))
