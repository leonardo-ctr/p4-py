print(" ")#define una linea en blanco
print("2- Hacer un diccionario de traducción español-inglés, se van a introducir las palabras en español e inglés separadas por dos puntos, y cada par <palabra>:<traducción> separados por comas. El programa debe crear un diccionario con las palabras y sus traducciones. Después pedirá una frase en español y utilizará el diccionario para traducirla palabra a palabra. Si una palabra no está en el diccionario debe dejarla sin traducir.")
print(" ")#define una linea en blanco
print(" Roman De la Cruz.3-w,1211")
print(" ")#define una linea en blanco
diccionario_traduccion = {}
print(" ")#define una linea en blanco
#solicita las palabras
palabras = input("Introduce las palabras en español e inglés separadas por dos puntos: ")
print(" ")#define una linea en blanco
# separa las palabras
pares = palabras.split(':')
for i in range(0, len(pares), 2):
    palabra = pares[i].strip()
    traduccion = pares[i+1].strip()
    diccionario_traduccion[palabra] = traduccion
print(" ")#define una linea en blanco
#solicita la frase en espalol
frase = input("Introduce una frase en español: ")
print(" ")#define una linea en blanco
# hace el diccionario para la traduccion
palabras_frase = frase.split()
frase_traducida = ' '.join(diccionario_traduccion.get(palabra, palabra) for palabra in palabras_frase)
#imprime la frase
print(f"Frase traducida: {frase_traducida}")
print(" ")#define una linea en blanco
