def determina_tipo_triangulo(l1,l2,l3):
    if l1 - l2 > l3 or l1 + l2 < l3:
        return "Não é um triangulo"
    if l1 == l2 == l3:
        return "É um triangulo equilátero!"
    if l1 == l2 != l3 or l1 != l2 == l3 or l1 == l3 != l2:
        return "É um triangulo isósceles"
    if l1 != l2 != l3:
        return "É um triangulo escaleno"
    
def main():
    print(determina_tipo_triangulo(4,4,4))
    print(determina_tipo_triangulo(4,4,2))
    print(determina_tipo_triangulo(3,4,5))
    print(determina_tipo_triangulo(1,1,4))

main()
    