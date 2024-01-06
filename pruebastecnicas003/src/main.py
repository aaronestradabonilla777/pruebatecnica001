

def texto_a_leet(texto):
    # Diccionario para la transformación de caracteres
    leet_dict = {
        'a': '4',
        'b': '8',
        'c': '<',
        'd': '|)',
        'e': '3',
        'f': '|=',
        'g': '6',
        'h': '#',
        'i': '1',
        'j': '_|',
        'k': '|<',
        'l': '|_',
        'm': '|\\/|',
        'n': '|\\|',
        'o': '0',
        'p': '|D',
        'q': '(,)',
        'r': '|2',
        's': '5',
        't': '7',
        'u': '|_|',
        'v': '\\/',
        'w': '\\/\\/',
        'x': '><',
        'y': '`/',
        'z': '2'
    }

    # Transformar el texto a leet
    texto_leet = ""
    for char in texto:
        if char.lower() in leet_dict:
            texto_leet += leet_dict[char.lower()]
        else:
            texto_leet += char

    return texto_leet

# Prueba del programa
texto = "Hola Mundo"
print(texto_a_leet(texto))
