
#def fizz_buzz(): es una funcion que imprime los numeros del 1 al 100,
#pero para los multiplos de 3 imprime fizz, para los multiplos de 5 imprime buzz y para los multiplos de 3 y 5 imprime fizzbuzz
def fizz_buzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("fizzbuzz")
        elif i % 3 == 0:
            print("fizz")
        elif i % 5 == 0:
            print("buzz")
        else:
            print(i)

fizz_buzz()