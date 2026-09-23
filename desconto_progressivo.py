"""Calcula o valor estimado da conta de agua e classifica o consumo."""


TARIFA_RESIDENCIAL = 4.50
TARIFA_COMERCIAL = 8.00


def classificar_consumo(tipo, consumo):
    if tipo == "comercial":
        return "Tarifa comercial"

    if tipo == "apartamento" and consumo < 10:
        return "Consumo economico"

    if consumo <= 25:
        return "Consumo moderado"

    return "Consumo excessivo"


def pedir_tipo():
    tipos_validos = ("casa", "apartamento", "comercial")

    while True:
        tipo = input(
            "Digite o tipo de imovel (casa, apartamento ou comercial): "
        ).strip().lower()

        if tipo in tipos_validos:
            return tipo

        print("Tipo invalido. Digite casa, apartamento ou comercial.")


def pedir_consumo():
    while True:
        entrada = input("Digite o consumo mensal em m3: ").strip()

        try:
            consumo = float(entrada.replace(",", "."))
        except ValueError:
            print("Digite apenas um numero, por exemplo: 12,5.")
            continue

        if consumo >= 0:
            return consumo

        print("O consumo nao pode ser negativo.")


def main():
    print("SISTEMA DE CONSUMO DE AGUA")

    tipo = pedir_tipo()
    consumo = pedir_consumo()
    classificacao = classificar_consumo(tipo, consumo)
    tarifa = TARIFA_COMERCIAL if tipo == "comercial" else TARIFA_RESIDENCIAL
    valor_total = consumo * tarifa

    print("\n----- RESULTADO -----")
    print(f"Tipo de imovel: {tipo}")
    print(f"Consumo mensal: {consumo:.2f} m3")
    print(f"Tarifa por m3: R$ {tarifa:.2f}")
    print(f"Valor estimado: R$ {valor_total:.2f}")
    print(f"Classificacao: {classificacao}")


if __name__ == "__main__":
    main()
