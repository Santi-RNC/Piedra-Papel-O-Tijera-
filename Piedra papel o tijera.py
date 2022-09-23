from random import randint
 
choice = ["piedra","papel","tijera"]
def main():
    computadora = choice[randint(0,2)]
 
    print("Bienvenido al juego piedra, papel o tijera\n")
    jugador = input("Tu eleccion: ").lower()
    print("La computadora eligio: " + computadora)
 
    if jugador == computadora:
        print("EMPATE")
    elif jugador == "piedra" and computadora == "papel":
        print("computadora gano")
    elif jugador == "piedra" and computadora == "tijera":
        print("jugador gano")
    elif jugador == "papel" and computadora == "piedra":
        print("jugador gano")
    elif jugador == "papel" and computadora == "tijera":
        print("computadora gano")
    elif jugador == "tijera" and computadora  == "piedra":
        print("computadora gano")
    elif jugador == "tijera" and computadora == "papel":
        print("jugador gano")
    elif jugador == "end":
        StopIteration
 
    main()
 
main()
