
def main():
    edad = int(input("Ingresa tu edad: "))
    if edad<=0:
        print("Respuesta incorrecta")
    elif edad<18:
        print("No cumples requisitos")
    else:   
        id= str(input("¿Tienes identificación oficial? (s/n): "))
        if id!="s" and id!="n":
            print("Respuesta incorrecta")
        elif edad>=18 and id=="s":
            print("Trámite de licencia concedido")
        elif id=="n":
            print("No cumples requisitos")

    #Aquí empieza tu programa...

if __name__ == '__main__':
    main()
