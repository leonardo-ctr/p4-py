# Crear un diccionario de traducción español-inglés
diccionario_traduccion = {}

# Introducir las palabras en español e inglés separadas por dos puntos
palabras = input("Introduce las palabras en español e inglés separadas por dos puntos: ")

# Dividir la entrada en pares <palabra>:<traducción>
pares = palabras.split(':')
for i in range(0, len(pares), 2):
    palabra = pares[i].strip()
    traduccion = pares[i+1].strip()
    diccionario_traduccion[palabra] = traduccion

# Pedir una frase en español para traducir
frase = input("Introduce una frase en español: ")

# Utilizar el diccionario para traducir la frase palabra por palabra
palabras_frase = frase.split()
frase_traducida = ' '.join(diccionario_traduccion.get(palabra, palabra) for palabra in palabras_frase)

print(f"Frase traducida: {frase_traducida}")