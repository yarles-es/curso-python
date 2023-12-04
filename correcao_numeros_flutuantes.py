numero_1 = 0.1
numero_2 = 0.7
soma = numero_1 + numero_2

print(soma)  # 0.7999999999999999

# round() - arredonda o número
print(round(soma, 2))  # 0.8

# quando nescessario para numeros extensos, usar o decimal
from decimal import Decimal

numero_1 = Decimal("0.1")
numero_2 = Decimal("0.7")
soma = numero_1 + numero_2
print(soma)  # 0.8
