def calculadora(a = int(input("Informe seu número: ")), b = int(input("Informe outo número: ")), operacao = input("Informe a operação: ")):
    match operacao:
        case "soma":
            return a + b
        case "subtracao" | "subtração":
            return a - b
        case "multiplicacao" | "mutiplicação":
            return a * b
        case "divisao" | "divisão":
            return a / b
        case _:
            return "Operação inválida"
        
def testa_calculadora():
    print(calculadora())

testa_calculadora()
