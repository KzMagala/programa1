
number = 40

print('¿Sabrías decirme una suma que de como resultado 40?, tienes 3 intentos.')

first_number = int(input('Primer numero: ' ))

second_number = int(input('Segundo numero: ' ))

result = first_number + second_number

print('La suma de {} y {} es {}'.format(first_number, second_number, result))


if result < number:
    print('Eso no es correcto, te has quedado corto')
if result > number:
    print('Eso no es correcto, te has pasado')
if result == number:
    print('¡Enhorabuena, sabes sumar!')

else: print('Va, es fácil, te quedan 2 intentos.')

first_number = int(input('Primer numero: ' ))

second_number = int(input('Segundo numero: ' ))

result = first_number + second_number

print('La suma de {} y {} es {}'.format(first_number, second_number, result))


if result < number:
    print('Eso no es correcto, te has quedado corto')
if result > number:
    print('Eso no es correcto, te has pasado')
if result == number:
    print('¡Enhorabuena, sabes sumar!')

else: print('Si que te cuesta, te queda 1 intento.')

first_number = int(input('Primer numero: ' ))

second_number = int(input('Segundo numero: ' ))

result = first_number + second_number

print('La suma de {} y {} es {}'.format(first_number, second_number, result))


if result < number:
    print('Eso no es correcto, te has quedado corto')
if result > number:
    print('Eso no es correcto, te has pasado')
if result == number:
    print('¡Enhorabuena, sabes sumar! (aunque te ha costado un poco...)')

else: print('Lo sentimos, tiene que retomar la ESO')
