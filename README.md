# Proyecto – Primer Corte

Materia: Paradigmas de Programación  
Lenguajes: Python y Haskell  

## Descripción
Este proyecto implementa operaciones matemáticas básicas en dos paradigmas distintos de programación:  
- Imperativo (Python)  
- Funcional (Haskell)  

Las funciones incluyen suma, resta usando antecesor, multiplicación, división, potencia y raíz cuadrada.  

## Funcionalidades

### Python
- sucesor(n) → retorna n+1  
- antecesor(n) → retorna n-1  
- sumar(a, b) → suma dos enteros  
- restar(a, b) → aplica antecesor de a, b veces  
- multiplicar(a, b) → suma repetida  
- dividir(a, b) → división entera  
- potencia(x, y) → potencia con multiplicación  
- raiz_cuadrada(n) → raíz cuadrada entera  

### Haskell
- sucesor n = n + 1  
- antecesor n = n - 1  
- sumar a b = a + b  
- restar a b → resta recursiva  
- multiplicar a b → suma recursiva  
- dividir a b → división por restas sucesivas  
- potencia x y → potencia recursiva  
- raizCuadrada n → raíz cuadrada entera por búsqueda  

## Ejecución

### Python
```bash
python proyecto.py
```

### Haskell
```bash
ghc proyecto.hs -o proyecto
./proyecto
```

## Ejemplo de salida
```
Suma 5+3 = 8
Resta 10-4 = 6
Multiplicación 6*4 = 24
División 20/4 = 5
Potencia 2^5 = 32
Raíz √25 = 5
```