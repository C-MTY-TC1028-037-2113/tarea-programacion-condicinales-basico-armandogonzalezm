def main():
    #escribe tu código abajo de esta línea
    peso = float(input("Peso en kg: "))
    altura= float(input("Altura en m: "))

    bmi=peso/altura**2

    if bmi<20 and bmi>0:
        print ("PESO BAJO")
    elif bmi>=20 and bmi<25:
        print("NORMAL")
    elif bmi>=25 and bmi<30:
        print("SOBREPESO")
    elif bmi>=30 and bmi<40:
        print("OBESIDAD")
    elif bmi <=40:
        print("OBESIDAD MORIBUNDA")
    elif bmi<=0:
        print("Revisa tus datos, alguno de ellos es erróneo")

if __name__=='__main__':
    main()