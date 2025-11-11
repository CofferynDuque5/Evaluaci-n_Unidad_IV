suma = 0

while True:
    numero_ingresado = input("Ingrese un número entero positivo: ")
    
    if numero_ingresado.isdigit() and int(numero_ingresado) > 0:
        numero = int(numero_ingresado)
        break  
    else:
        print("El numero debe ser un entero positivo, verifique los numeros que ingreso e intente de nuevo.")

calculo = numero

while calculo > 0:
    
    digito = calculo % 10
    
    suma += digito
    
    calculo //= 10

print(f"La suma de los dígitos es: {suma}")

