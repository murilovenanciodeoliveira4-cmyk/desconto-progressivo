# Sistema de Desconto Progressivo
# Atividade de recuperação - Python

# Solicita ao usuário o valor total da compra
valor_compra = float(input("Digite o valor total da compra: R$ "))

# Verifica a faixa de desconto de acordo com o valor da compra
if valor_compra < 200:
    percentual_desconto = 5
elif valor_compra < 300:
    percentual_desconto = 10
else:
    percentual_desconto = 15

# Calcula o valor do desconto
valor_desconto = valor_compra * percentual_desconto / 100

# Calcula o valor final que o cliente deverá pagar
valor_final = valor_compra - valor_desconto

# Exibe o resumo da compra
print("\n----- RESUMO DA COMPRA -----")
print(f"Valor da compra: R$ {valor_compra:.2f}")
print(f"Desconto aplicado: {percentual_desconto}%")
print(f"Valor do desconto: R$ {valor_desconto:.2f}")
print(f"Total a pagar: R$ {valor_final:.2f}")
