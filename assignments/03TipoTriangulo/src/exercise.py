def main():
    lado1 = int(input("Ingresa la medida del lado 1:"))
    lado2 = int(input("Ingresa la medida del lado 2:"))
    lado3 = int(input("Ingresa la medida del lado 3:"))
    if lado1==lado2 and lado2==lado3 and lado3==lado1:
        print("ES UN TRIANGULO EQUILATERO")
    elif (lado1==lado2 or lado2==lado3 or lado3==lado1) and (lado1!=lado3 or lado3!=lado2 or lado1!=lado2):
        print("ES UN ISOSCELES")
    elif (lado1!=lado2 and lado2!=lado3 and lado3!=lado1) and ((lado1**2==lado2**2+lado3**2)or(lado2==lado3**2+lado1**2)or(lado3==lado2**2+lado1**2)):
        print("ES UN TRIANGULO ESCALENO")
    elif (lado1>(lado2+lado3))or(lado3>(lado1+lado2))or(lado2>(lado1+lado3)):
        print('NO ES UN TRIANGULO')
   


    
    #Escribe aquí tu código...


if __name__=='__main__':
    main()