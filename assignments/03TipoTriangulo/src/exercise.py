def main():
    x = int(input("Ingresa la medida del lado 1: "))
    y = int(input("Ingresa la medida del lado 2: "))
    z = int(input("Ingresa la medida del lado 3: "))
    if x+y>z and y+z>x and z+x>y and x>0 and y>0 and z>0:
        if x==z and y==x and z==y:
            print("ES UN TRIANGULO EQUILATERO")
        elif (x==y and x!=z) or (z==x and z!=y) or (z==y and x!=z):
            print("ES UN TRIANGULO ISOSCELES")
        elif (x!=y and x!=z and z!=y):
            print("ES UN TRIANGULO ESCALENO")
    else:
        print("NO ES TRIANGULO")
        
   


    
    #Escribe aquí tu código...


if __name__=='__main__':
    main()