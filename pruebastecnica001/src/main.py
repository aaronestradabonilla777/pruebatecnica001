#PRUEBA TECNICA 1

#def detect es una funcion que recibe una lista de numeros, un numero y un minimo de repeticiones y devuelve True si el numero se repite al menos min_rep veces en la lista, False en caso contrario.
def detect(list, num, min_rep):
    cont = list.count(num)
    return cont >= min_rep

list = [4, 5, 2, 4, 5, 9, 9, 4, 4]

num = 4
min_rep=4

print(detect (list, num, min_rep))

#PRUEBA TECNICA 2
#def MD es una funcion que recibe una lista de numeros y devuelve la diferencia entre el mayor y el menor de ellos.
def MD(list):
    return max(list) - min(list)

list = [28, 16, 28, 11, 14, 26, 23, 25, 17, 3, 22, 23, 23, 10 ]
print(MD(list))


#PRUEBA TECNICA 3
# metodDif es una funcion que recibe una lista de numeros y devuelve True si la diferencia entre cada numero es constante, False en caso contrario.
def metodDif(list):

    dif = list[1] - list[0]

    for i in range(2, len(list)):
        if list[i] - list[i-1] != dif:
            return False
    return True


print(metodDif([194, 54, 23, 7, 3, 6, 8]))  # False

print(metodDif([ 1, 8 ]))  #True

print(metodDif([ -2.3, -1.1, 0.1, 1.3, 2.5, 3.7 ]))  # False

#PRueba