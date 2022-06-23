print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')


print("Bienvenido a la isla del tesoro.")
print("Tu misión es encontrar el tesoro.") 

opcion1 = input("Estás enfrente de dos caminos, ¿Qué camino quieres elegir? Escribe 'Derecha' o 'Izquierda'\n")
opcion1_lower = opcion1.lower()


if opcion1_lower == "izquierda":
  opcion2 = input("Has llegado a un lago. Hay una isla en medio del lago. Escriba 'esperar' para esperar un barco. Escriba 'nadar' para cruzar nadando.\n")
  opcion2_lower = opcion2.lower()

  if opcion2_lower == "esperar":
    opcion3 = input("Llegas a la isla ileso. Hay una casa con 3 puertas. Una roja, una amarilla y una azul. ¿Qué color eliges? \n")
    opcion3_lower = opcion3.lower()

    if opcion3_lower == "amarilla":
        print("¡Encontraste el tesoro! ¡Has ganado!")
    elif opcion3_lower == "azul":
        print("Has sido devorado por una bestia")
    elif opcion3_lower == "roja":
        print("Te has quemado debido a un incendio")
    else:
        print("Juego terminado")

  else:
    print("Has sido atacado por un tiburon, juego terminado")

else:
  print("Has caido a un oyo, juego terminado.")