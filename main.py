from funciones import * #Cuando se usa import * se esta importando TODAS las funciones que estan en el archivo sin necesidad de estar llamandolas una por una ;p

passwordAdmin = "Caremonda"
passwordCajero = "1245"
passwordLogistica = "Nose"
passwordDomiciliario = "EsRappi"
intentos = 3 

while True:
    print ("\n" + "=" * 30)  
    print ("SELECCIONE SU ROL".center(30))
    print ("="*30)
    print("\n1. ADMINISTRADOR")
    print("2. CAJERO")
    print("3. LOGISTICA")
    print("4. DOMICILIARIO")
    print("\n5. SALIR")
    while True:
        try:
            seleccion = int(input("\nINGRESE SU ROL: "))
            break
        except ValueError:
                print("Ingrese una opción válida: ")
                
    if seleccion == 5: 
         exit("Tenga buen día...")
    else: 
         match seleccion:
              case 1: #ADMIN
                if verificationPassword (passwordAdmin, intentos):
                    print("\nBienvenido, ADMIN")
                    menuAdmin()                            
              case 2: #CAJERO
                 if verificationPassword (passwordCajero, intentos):
                    print("\nBienvenido, CAJERO")
                    menuCajero()  
              case 3: #LOGISTICA
                if verificationPassword (passwordLogistica, intentos):
                    print("\nBienvenido, LOGISTICA")
                    menuLogistica()
              case 4: #DOMICILIARIO
                 if verificationPassword (passwordDomiciliario, intentos):
                    print("\nBienvenido, DOMICILIARIO")
                    menuDomiciliario()