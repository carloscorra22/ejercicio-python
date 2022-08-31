pi=3.14

def areaTriangulo(base, altura):
    return (base * altura) // 2


def areaCirculo(radio):

    return pi * (radio ** 2)

resultado = areaTriangulo(3, 5)

resultado2 = areaCirculo(5)
print("El area del triangulo es:", resultado)
print("el area del circulo es:", resultado2)
