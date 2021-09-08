
def main():
    edad = int(input("Ingresa tu edad: "))
    id= str(input("Tienes identificación oficial?(s/n): "))
    if edad<=0:
        print("Respuesta incorrecta")
    elif edad>=18 and id=="s":
        print("Tramite de licencia concedido")
    elif id=="n" or edad<18:
        print("No cumples los requisitos")
    elif id!="s" or id!="n":
        print("Respuesta incorrecta")
    
    #Aquí empieza tu programa...

if __name__ == '__main__':
    main()
