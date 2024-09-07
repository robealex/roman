import re
import os


#agregamos una lista de los numeros romanos, como diccionario
letrasromanas = {
    'I': 1, 
    'V': 5, 
    'X': 10, 
    'L': 50, 
    'C': 100, 
    'D': 500, 
    'M': 1000
}

#hay q cambiar de el numero romano a el numero entero
#se lee el 
def rom_ent(num_romano):
    total = 0
    num_ante = 0
    for char in reversed(num_romano):
        #lee el numero de la letra romana
        # siel numero  mayor que el anterior se suma si no se resta 
        # por q iv<v<vi por q esos valores al estar antes o despues
        #cambian la salida
        numero_leido = letrasromanas.get(char, 0)
        if numero_leido >= num_ante:
            total += numero_leido
        else:
            total -= numero_leido
        num_ante = numero_leido
    return total

# 
def compara(valor):
    # Encontrar las letras que corresponden a números romanos
    letrasroma = ''.join([char for char in valor.upper() if char in letrasromanas])
    if letrasroma:
        return rom_ent(letrasroma)
    return 0  # Si no hay letras de números romanos, devolver 0

#No dice q si nos dara la lista o lo agregemos, asi q opte por q me las de el usuario :D
#se añanede salir para q salgas del ciclo
lista_palabras = []
print("Ingresa las palabras que desees (escribe 'salir' para terminar):")
while True:
    valor = input("Palabra: ")
    if valor.lower() == 'salir':#para salir le ponemos salir
        break
    lista_palabras.append(valor)#aqui se guardan las palabras en la lista
    
    
#Nada mas para q no se vea repetido la lista de palabraslozas
def clear_screen():
    if os.name == 'nt':
        os.system('cls')  #
    else:
        os.system('clear')  
clear_screen()

#Si se quiere acomodar de mayor a menor:
#   lista_palabras.sort(key=compara, reverse=True)
#pero no supe si era necesario esto

#el print de salida
print("\nLista de palabras:")
for valor in lista_palabras:
    print(f"{valor} = {compara(valor)}")
    


