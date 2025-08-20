sucesor :: Int -> Int
sucesor n = n + 1

antecesor :: Int -> Int
antecesor n = n - 1

sumar :: Int -> Int -> Int
sumar a b = a + b

restar :: Int -> Int -> Int
restar a 0 = a
restar a b = restar (antecesor a) (antecesor b)

multiplicar :: Int -> Int -> Int
multiplicar a 0 = 0
multiplicar a b = a + multiplicar a (antecesor b)

dividir :: Int -> Int -> Int
dividir a b
    | b == 0 = error "No se puede dividir entre 0"
    | a < b = 0
    | otherwise = sucesor (dividir (a - b) b)

potencia :: Int -> Int -> Int
potencia x 0 = 1
potencia x y = x * potencia x (antecesor y)

raizCuadrada :: Int -> Int
raizCuadrada n = buscar 0
  where
    buscar c
      | c * c > n = antecesor c
      | otherwise = buscar (sucesor c)

main = do
    print (sumar 5 3)
    print (restar 10 4)
    print (multiplicar 6 4)
    print (dividir 20 4)
    print (potencia 2 5)
    print (raizCuadrada 25))