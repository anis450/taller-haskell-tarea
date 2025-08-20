def sucesor(n):
    return n + 1

def antecesor(n):
    return n - 1

def sumar(a, b):
    return a + b

def restar(a, b):
    resultado = a
    for _ in range(b):
        resultado = antecesor(resultado)
    return resultado

def multiplicar(a, b):
    resultado = 0
    for _ in range(b):
        resultado = sumar(resultado, a)
    return resultado

def dividir(a, b):
    if b == 0:
        raise ValueError("No se puede dividir entre 0")
    cociente = 0
    acumulado = a
    while acumulado >= b:
        acumulado = restar(acumulado, b)
        cociente = sucesor(cociente)
    return cociente

def potencia(x, y):
    resultado = 1
    for _ in range(y):
        resultado = multiplicar(resultado, x)
    return resultado

def raiz_cuadrada(n):
    if n < 0:
        raise ValueError("No se puede raíz cuadrada de negativos")
    candidato = 0
    while multiplicar(candidato, candidato) <= n:
        candidato = sucesor(candidato)
    return antecesor(candidato)

if __name__ == "__main__":
    print("Suma 5+3 =", sumar(5,3))
    print("Resta 10-4 =", restar(10,4))
    print("Multiplicación 6*4 =", multiplicar(6,4))
    print("División 20/4 =", dividir(20,4))
    print("Potencia 2^5 =", potencia(2,5))
    print("Raíz √25 =", raiz_cuadrada(25))