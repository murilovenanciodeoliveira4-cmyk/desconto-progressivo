# desconto-progressivo
Sistema de desconto progressivo desenvolvido em Python.


# Sistema de Desconto Progressivo

## Descrição

Este projeto foi desenvolvido em Python para implementar um sistema de desconto progressivo para uma loja online.

O programa solicita ao usuário o valor total da compra e verifica automaticamente qual desconto deve ser aplicado:

- Compras abaixo de R$ 200,00 recebem 5% de desconto.
- Compras de R$ 200,00 até R$ 299,99 recebem 10% de desconto.
- Compras a partir de R$ 300,00 recebem 15% de desconto.

Após identificar o percentual de desconto, o programa calcula o valor do desconto e o valor final que o cliente deverá pagar.

## Como testar

Para verificar se o programa está funcionando corretamente, devem ser realizados três testes:

### Teste 1
Valor da compra: R$ 150,00

Resultado esperado:
- Desconto: 5%
- Valor do desconto: R$ 7,50
- Total a pagar: R$ 142,50

### Teste 2
Valor da compra: R$ 250,00

Resultado esperado:
- Desconto: 10%
- Valor do desconto: R$ 25,00
- Total a pagar: R$ 225,00

### Teste 3
Valor da compra: R$ 350,00

Resultado esperado:
- Desconto: 15%
- Valor do desconto: R$ 52,50
- Total a pagar: R$ 297,50

Esses testes permitem verificar se todas as condições de desconto foram implementadas corretamente.

## Tecnologias utilizadas

- Python
- Visual Studio Code
- GitHub
