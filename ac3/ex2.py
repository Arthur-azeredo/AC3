def dia_semana(num):
    match num:
        case 1:
            return "Domingo"
        case 2:
            return "Segunda"
        case 3:
            return "Terca"
        case 4:
            return "Quarta"
        case 5:
            return "Quinta"
        case 6:
            return "Sexta"
        case 7:
            return "sabado"
        case _:
            return ""
        
def testa_dia_semana():
    print(dia_semana(1))
    print(dia_semana(2))
    print(dia_semana(3))
    print(dia_semana(4))
    print(dia_semana(5))
    print(dia_semana(6))
    print(dia_semana(7))
    print(dia_semana(10))

testa_dia_semana()

