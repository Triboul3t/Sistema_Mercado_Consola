#=====_INVENTARIO_=====#
inventario = {
    "Arroz": {"Precio": 3000, "Cantidad": 12},
    "Aceite": {"Precio": 8000, "Cantidad": 14},
    "Arepa": {"Precio": 5000, "Cantidad": 24},
    "Buñuelos": {"Precio": 2000, "Cantidad": 36},
    "Panela": {"Precio": 4000, "Cantidad": 20},
    "Huevos": {"Precio": 15000, "Cantidad": 8},
    "Leche": {"Precio": 4500, "Cantidad": 18},
    "Café": {"Precio": 12000, "Cantidad": 10},
    "Pan": {"Precio": 3500, "Cantidad": 15},
    "Chocolate": {"Precio": 6000, "Cantidad": 22}
}

#=====_CONTACTOS_=====#
contactos = {
    "Juan Solo": {"Telefono": "3001234567", "Correo": "juan@correo.com"},
    "Ana Banana": {"Telefono": "3109876543", "Correo": "ana@correo.com"},
    "Elña Tico": {"Telefono": "3109712875", "Correo": "elña@correo.com"},
    "Care Monda": {"Telefono": "3109879000", "Correo": "care@correo.com"},
    "Elso Plao": {"Telefono": "3109878945", "Correo": "elso@correo.com"}
}

#=====_RESERVAS_=====#
reservas = {}

#=====_TAREAS_=====#
tareas = {}

#=====_CONVERSIONES_=====#
conversiones = {}

#=====_ASISTENCIAS_=====#
asistencias = {}

#=====_DOLAR_=====#
tasaDolar = 3120

#===========================================================================================================================================#

#=====_VERIFICACION CONTRASEÑA_=====#

def verificationPassword (passwordCorrect, intentos):
        for intento in range (intentos):
            password = input("INGRESE SU CONTRASEÑA: ")
            if password == passwordCorrect:
                return True
            else: 
                intentosRestantes = intentos - intento - 1  
                print (f"\nCONTRASREÑA INCORRECTA, LE QUEDAN {intentosRestantes} INTETOS.")
        return False
    
#=====_PEDIR OPCION_=====#
def pedirOpcion(mensaje):
    while True:
        try:
            opcion = int(input(mensaje))
            break
        except ValueError:
            print("No ingresaste una opcion valida...")
    return opcion

#===========================================================================================================================================#

#-----_SISTEMA ASISTENCIA_-----#


# 1. MARCAR ASISTENCIA
def marcarAsistencia():
    nombre = input("Nombre de la persona: ")
    nombre = nombre.title()

    presente = input(f"¿{nombre} esta presente? (S/N): ")
    presente = presente.upper()

    if presente == "S":
        asistencias[nombre] = "Presente"
        print(f"{nombre} marcado como Presente")
    elif presente == "N":
        asistencias[nombre] = "Ausente"
        print(f"{nombre} marcado como Ausente")
    else:
        print("Opcion invalida, cancelando...")

# 2. VER ASISTENTES
def verAsistentes():
    presentes = {}
    for nombre, estado in asistencias.items():
        if estado == "Presente":
            presentes[nombre] = estado

    if not presentes:
        print("No hay nadie marcado como presente")
        return

    for nombre, estado in presentes.items():
        print(f"{nombre} - {estado}")

# 3. VER AUSENTES
def verAusentes():
    ausentes = {}
    for nombre, estado in asistencias.items():
        if estado == "Ausente":
            ausentes[nombre] = estado

    if not ausentes:
        print("No hay nadie marcado como ausente")
        return

    for nombre, estado in ausentes.items():
        print(f"{nombre} - {estado}")

# 4. BUSCAR ASISTENCIA POR NOMBRE
def buscarAsistencia():
    nombre = input("Nombre de la persona: ")
    nombre = nombre.title()

    if nombre in asistencias:
        print(f"{nombre} - {asistencias[nombre]}")
    else:
        print("Esa persona no ha sido registrada")

# MENU ASISTENCIA
def sistemaAsistencia():
    while True:
        print("\n"+"#"*30)
        print("SISTEMA ASISTENCIA".center(30))
        print("#"*30)
        
        print("\n1. Marcar asistencia")
        print("2. Ver asistentes")
        print("3. Ver ausentes")
        print("4. Buscar persona")
        
        print("\n5. Volver")

        opcion = pedirOpcion("Seleccione una opcion: ")
        if opcion == 5:
            print("Regresando...")
            return
        match opcion:
            case 1:
                marcarAsistencia()
            case 2:
                verAsistentes()
            case 3:
                verAusentes()
            case 4:
                buscarAsistencia()
            case _:
                print("Opcion invalida")

#===========================================================================================================================================#

#-----_SISTEMA CONTACTOS_-----#

# 1. AGREGAR CONTACTO
def agregarContacto():
    nombre = input("Nombre del contacto: ")
    nombre = nombre.title() #Title funciona como el capitalize pero pone la mayuscula en strings que sean dos palabras (Juan Solo)
    
    if nombre in contactos:
        reemplazar = input(f"¿{nombre} ya existe. Desea reemplazarlo? (S/N): ")
        reemplazar = reemplazar.upper()
        if reemplazar == "N":
            print("Cancelando...")
            return
        elif reemplazar != "S":
            print("Opción inválida, cancelando...")
            return

    telefono = input("Teléfono: ")
    correo = input("Correo: ")
    contactos[nombre] = {"Telefono": telefono, "Correo": correo}
    print(f"\n{nombre} agregado a contactos")

# 2. ELIMINAR CONTACTO
def eliminarContacto():
    nombre = input("Nombre del contacto que desea eliminar: ")
    nombre = nombre.title()
    if nombre not in contactos:
        print("La persona no se encuentra en los contactos")
        return  
    while True:
        confirmar = input(f"\n¿Seguro que quiere eliminar {nombre}? (S/N)")
        confirmar = confirmar.upper()
        if confirmar == "S":
            del contactos[nombre]
            print(f"\n{nombre} eliminado de contactos...")
            break
        elif confirmar == "N":
            print("\nCancelando...")
            return
        else:
            print("No seleccionaste una opcion valida")
# 3. MODIFICAR NUMERO 
def cambiarNumero():
    contacto = input("Ingrese el nombre del contacto: ")
    contacto = contacto.title()
    if contacto not in contactos:
        print("El nombre no se encuentra en los contactos")
        return
    while True:
        try:
            nuevoNumero = int(input("Ingrese el numero nuevo: "))
            nuevoNumero = str(nuevoNumero)
            if nuevoNumero == contactos[contacto]["Telefono"]:
                print("El nuevo numero es el mismo al antiguo")
                return
            else:
                break
        except ValueError:
            print("No ingresaste un valor valido")
    contactos[contacto]["Telefono"] = nuevoNumero

# 4. MODIFICAR CORREO
def cambiarCorreo():
    contacto = input("Ingrese el nombre del contacto: ")
    contacto = contacto.title()
    if contacto not in contactos:
        print("\nEl nombre no se encuentra en los contactos")
        return
    
    while True:
        nuevoCorreo = input("Ingrese el nuevo correo del contacto: ")
        if nuevoCorreo == contactos[contacto]["Correo"]:
            print("\nEl nuevo correo es el mismo al antiguo")
            continue
        elif "@" not in nuevoCorreo:
            print("\nNo agregaste un correo valido")
            continue
        else:
            break
    contactos[contacto]["Correo"] = nuevoCorreo

#5. BUSCAR CONTACTO

def buscarContacto():
    contacto = input("Ingrese el nombre del contacto: ")
    contacto = contacto.title()
    if contacto in contactos:
        print(f'{contacto} - Telefono: {contactos[contacto]["Telefono"]} - Correo: {contactos[contacto]["Correo"]}')
    else:
        print("\nEl nombre no se encuentra en los contactos")    

# 6. VISUALIZAR CONTACTOS            
def visualizarContactos():
    for nombre, datos in contactos.items():
        print (f'\n{nombre} - Telefono:{datos["Telefono"]} - Correo:{datos["Correo"]}')

# MENU CONTACTOS
def sistemaContactos():
    while True:
        print("\n"+"#"*30)
        print("SISTEMA CONTACTOS".center(30))
        print("#"*30)
        print("\n1. Agregar contacto")
        print("2. Eliminar contacto")
        print("3. Modificar numero contacto")
        print("4. Modificar correo contacto")
        print("5. Buscar contacto")
        print("6. Visualizar contactos")
        print("\n7. Volver")

        opcion = pedirOpcion("\nSeleccione una opcion: ")
        if opcion == 7:
            print("Regresando...")
            return
        else:
            match opcion:
                case 1:
                    agregarContacto()
                case 2:
                    eliminarContacto()
                case 3:
                    cambiarNumero()
                case 4:
                    cambiarCorreo()
                case 5:
                    buscarContacto()
                case 6:
                    visualizarContactos()
                case _:
                    print("Opcion invalida...")       

#===========================================================================================================================================#

#-----_SISTEMA INVENTARIO_-----#

# 1. AGREGAR PRODUCTO
def agregarProducto():
    nombre = input("Nombre del producto: ")
    nombre = nombre.capitalize()
    while True:
        if nombre in inventario:
            reemplazar = input(f"¿Esta seguro que quiere reemplazar {nombre}? (S/N)")
            reemplazar = reemplazar.upper()
            if reemplazar == "S":
                print("\nContinuando...")
                break
            elif reemplazar == "N":
                print("\nCancelando...")
                return
            else:
                print("No agregaste una opcion valida")
        else:
            break
    while True:
        try:
            precio = int(input("\nPrecio del producto: "))
            cantidad = int(input("\nCantidad del producto: "))
            break
        except ValueError:
            print("No ingresaste un dato valido")
    inventario[nombre] = {"Precio": precio, "Cantidad": cantidad}
    print(f"\n{nombre} agregado al inventario")
    
# 2. ELIMINAR PRODUCTO
def eliminarProducto():
    nombre = input("\nNombre del producto que desea eliminar: ")
    nombre = nombre.capitalize()
    if nombre not in inventario:
        print("El producto no se encuentra en el inventario")
        return  
    while True:
        confirmar = input(f"\n¿Seguro que quiere eliminar {nombre}? (S/N)")
        confirmar = confirmar.upper()
        if confirmar == "S":
            del inventario[nombre]
            print(f"\n{nombre} eliminado del inventario...")
            break
        elif confirmar == "N":
            print("\nCancelando...")
            return
        else:
            print("No seleccionaste una opcion valida")

# 3. CAMBIAR PRECIO
def cambiarPrecio():
    producto = input("\nIngrese el nombre del producto: ")
    producto = producto.capitalize()
    if producto not in inventario:
        print("El producto no se encuentra en el inventario")
        return
    while True:
        try:
            nuevoPrecio = int(input("\nIngrese el precio del nuevo producto: "))
            if nuevoPrecio == inventario[producto]["Precio"]:
                print("El nuevo precio es el mismo al antiguo")
                return
            else:
                break
        except ValueError:
            print("No ingresaste un valor valido")
    
    inventario[producto]["Precio"] = nuevoPrecio

# 4. BUSCAR PRODUCTO
def buscarProducto():
    producto = input("\nIngrese el nombre del producto: ")
    producto = producto.capitalize()
    if producto in inventario:
        print(f'\n{producto} - Precio: {inventario[producto]["Precio"]} - Cantidad: {inventario[producto]["Cantidad"]}')
    else:
        print("\nEl producto no se encuentra en el inventario")

# 5. VISUALIZAR INVENTARIO            
def visualizarInventario():
    for producto, datos in inventario.items():
        print (f'\n{producto} - Precio:{datos["Precio"]} - Cantidad:{datos["Cantidad"]}')

# MENU INVENTARIO 
def sistemaInventario():
    while True:
        print("\n"+"#"*30)
        print("SISTEMA INVENTARIO".center(30))
        print("#"*30)
        print("\n1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Cambiar precio")
        print("4. Buscar producto")
        print("5. Visualizar inventario")
        print("\n6. Volver")

        opcion = pedirOpcion("\nSeleccione una opcion: ")
        if opcion == 6:
            print("Regresando...")
            return
        else:
            match opcion:
                case 1:
                    agregarProducto()
                case 2:
                    eliminarProducto()
                case 3:
                    cambiarPrecio()
                case 4:
                    buscarProducto()
                case 5:
                    visualizarInventario()
                case _:
                    print("Opcion invalida...")

#===========================================================================================================================================#
            
#-----_SISTEMA RESERVA_-----#
# 1. AGREGAR RESERVA
def agregarReserva():
    cliente = input("Nombre del cliente: ")
    cliente = cliente.capitalize()
    fecha = input("Fecha de la reserva (DD/MM/AAAA): ")
    hora = input("Hora de la reserva (HH:MM): ")

    idReserva = len(reservas) + 1
    reservas[idReserva] = {"Cliente": cliente, "Fecha": fecha, "Hora": hora}

    print(f"\nReserva #{idReserva} agregada para {cliente} el {fecha} a las {hora}")

# 2. ELIMINAR RESERVA
def eliminarReserva():
    while True:
        try:
            id = int(input("\nID de la reserva que desea eliminar: "))
            break
        except ValueError:
            print("No seleccionaste un valor valido")
    if id not in reservas:
        print("La reserva no se encuentra agendado")
        return  
    while True:
        confirmar = input(f"¿Seguro que quiere eliminar {id}? (S/N)")
        confirmar = confirmar.upper()
        if confirmar == "S":
            del reservas[id]
            print(f"\n{id} eliminado de las reservas...")
            break
        elif confirmar == "N":
            print("\nCancelando...")
            return
        else:
            print("No seleccionaste una opcion valida")

#3. VISUALIZAR RESERVAS

def visualizarReservas():
    for reserva, datos in reservas.items():
        print (f'\nID: {reserva} - Cliente:{datos["Cliente"]} - Fecha:{datos["Fecha"]} - Hora:{datos["Hora"]}')

# MENU RESERVA
def sistemaReservas():
    while True:
        print("\n"+"#"*30)
        print("SISTEMA RESERVAS".center(30))
        print("#"*30)
        print("\n1. Agregar Reserva")
        print("2. Eliminar Reserva")
        print("3. Visualizar Reservas")
        print("\n4. Volver")

        opcion = pedirOpcion("\nSeleccione una opcion: ")
        if opcion == 4:
            print("Regresando...")
            return
        else:
            match opcion:
                case 1:
                    agregarReserva()
                case 2:
                    eliminarReserva()
                case 3:
                    visualizarReservas()
                case _:
                    print("Opcion invalida")
                    
#===========================================================================================================================================#
            
#-----_SISTEMA TAREAS_-----#
# 1. AGREGAR TAREA
def agregarTarea():
    descripcion = input("Descripcion de la tarea: ")
    
    print("\n"+"_"*30)
    print("ASIGNAR TAREAS".center(30))
    print("_"*30)
    
    print("\n¿Para qué rol es esta tarea?")
    print("1. Cajero")
    print("2. Logística")
    print("3. Domiciliario")
    rolAsignado = pedirOpcion("\nSeleccione el rol: ")
    
    match rolAsignado:
        case 1:
            rol = "Cajero"
        case 2:
            rol = "Logistica"
        case 3:
            rol = "Domiciliario"
        case _: 
            print("Rol invalido, cancelando...")
            return
    
    idTarea = len(tareas) + 1
    tareas[idTarea] = {"Descripcion": descripcion, "Rol": rol, "Completada": False}
    print(f"\nTarea #{idTarea} asiganada a {rol}")
    
# 2. ELIMINAR TAREA
def eliminarTarea():
    while True:
        try:
            id = int(input("\nID de la tarea que desea eliminar: "))
            break
        except ValueError:
            print("\nNo seleccionaste un valor valido")
    if id not in tareas:
        print("\nLa tarea con ese id no esta asignada")
        return  
    while True:
        confirmar = input(f"\n¿Seguro que quiere eliminar la tarea #{id}? (S/N)")
        confirmar = confirmar.upper()
        if confirmar == "S":
            del tareas[id]
            print(f"\n{id} eliminado de las tareas...")
            break
        elif confirmar == "N":
            print("\nCancelando...")
            return
        else:
            print("No seleccionaste una opcion valida")

# 3. Visualizar Tareas
def visualizarTareas():
    for tarea, datos in tareas.items():
        if datos["Completada"] == True:
            estado = "Completada"
        else: 
            estado = "Pendiente"
        print(f'\nID: {tarea} - Descripcion: {datos["Descripcion"]} - Rol: {datos["Rol"]} - Completado: {estado}')

# 4. VISUALIZAR TAREAS ROL
def tareasRol(rol):
    tareasDelRol = {} # Es una "canasta" donde vas a ir guardando solo las tareas que le pertenezcan a este rol específico.
    for id, datos in tareas.items():
        if datos["Rol"] == rol:
            tareasDelRol[id] = datos

    if not tareasDelRol:
        print("No tiene tareas asignadas")
        return

    for id, datos in tareasDelRol.items():
        if datos["Completada"]:
            estado = "Completada"
        else:
            estado = "Pendiente"
        print(f"ID: {id} - Descripcion: {datos['Descripcion']} - Estado: {estado}")

    marcar = input("\n¿Desea marcar alguna tarea como completada? (S/N): ")
    marcar = marcar.upper()
    if marcar != "S":
        return

    while True:
        try:
            idTarea = int(input("ID de la tarea a marcar como completada: "))
            break
        except ValueError:
            print("\nNo ingresaste un valor valido")

    if idTarea not in tareasDelRol:
        print("\nEsa tarea no le pertenece o no existe")
        return

    tareas[idTarea]["Completada"] = True
    print("\nTarea marcada como completada")
    
    
# MENU TAREAS
def sistemaTareas():
    while True:
        print("\n"+"#"*30)
        print("SISTEMA TAREAS".center(30))
        print("#"*30)
        print("\n1. Agregar Tarea")
        print("2. Eliminar Tarea")
        print("3. Visualizar Tareas")
        print("\n4. Volver")

        opcion = pedirOpcion("\nSeleccione una opcion: ")
        if opcion == 4:
            print("Regresando...")
            return
        else:
            match opcion:
                case 1:
                    agregarTarea()
                case 2:
                    eliminarTarea()
                case 3:
                    visualizarTareas()
                case _:
                    print("\nOpcion invalida")

#===========================================================================================================================================#

#-----_SISTEMA CONVERSIONES_-----#

# HISTORIAL CONVERSIONES
def historialConversiones():
    if not conversiones:
        print("El historial esta vacio...")
    for conversion, datos in conversiones.items():
        print(f'\nID: {conversion} - Tipo: {datos["Tipo"]} - Detalle: {datos["Detalle"]}')
    

# CONVERSOR DE PESO
def conversorPeso():
    print("\n1. Kilogramos a Libras")
    print("2. Libras a Kilogramos")
    opcion = pedirOpcion("\nSeleccione una opcion: ")
    while True:
        try:
            valor = float(input("Ingrese el valor: "))
            break
        except ValueError:
            print("No ingresaste un valor valido")
    match opcion:
        case 1:
            resultado = (valor * 2.2046)
            resultado = round(resultado, 2)
            detalle = f"{valor} Kg -> {resultado} Lbs"
        case 2:
            resultado = (valor / 2.2046) 
            resultado = round(resultado, 2)
            detalle = f"{valor} Lbs -> {resultado} Kg"
        case _:
            print("Opcion invalida")
            return
    print(f"\nResultado: {detalle}")
    idConversion = len(conversiones) + 1
    conversiones[idConversion] = {"Tipo": "Peso", "Detalle": detalle}

# CONVERSOR DE DISTANCIA
def conversorDistancia():
    print("\n1. Kilometros a Millas")
    print("2. Millas a Kilometros")
    opcion = pedirOpcion("\nSeleccione una opcion: ")
    while True: 
        try:
            valor = float(input("Ingrese el valor: "))
            break
        except ValueError:
            print("No ingresaste un valor valido")
    match opcion:
        case 1: 
            resultado = (valor * 0.621371)
            resultado = round(resultado, 2)
            detalle = f"{valor} Km -> {resultado} Mi"
        case 2:
            resultado = (valor / 0.621371)
            resultado = round(resultado, 2)
            detalle = f"{valor} Mi -> {resultado} Km"
        case _:
            print("Opcion invalida")
            return
    print(f"\nResultado: {detalle}")
    idConversion = len(conversiones) + 1
    conversiones[idConversion] = {"Tipo": "Distancia", "Detalle": detalle} 
    
# CONVERSOR DE MONEDA
def conversorMoneda():
    print("\n1. COP a USD")
    print("2. USD a COP")
    opcion = pedirOpcion("\nSeleccione una opcion: ")

    while True:
        try:
            valor = float(input("Ingrese el valor: "))
            break
        except ValueError:
            print("No ingresaste un valor valido")

    match opcion:
        case 1:
            resultado = valor / tasaDolar
            resultado = round(resultado, 2)
            detalle = f"${valor} COP -> ${resultado} USD"
        case 2:
            resultado = valor * tasaDolar
            resultado = round(resultado, 2)
            detalle = f"${valor} USD -> ${resultado} COP"
        case _:
            print("Opcion invalida")
            return

    print(f"\nResultado: {detalle}")
    idConversion = len(conversiones) + 1
    conversiones[idConversion] = {"Tipo": "Moneda", "Detalle": detalle}
    
# MENU CONVERSOR
def sistemaConversion():
    while True:
        print("\n"+"#"*30)
        print("SISTEMA CONVERSION".center(30))
        print("#"*30)
        
        print("\n1. Conversor de Peso")
        print("2. Conversor de Distancia")
        print("3. Conversor de Moneda")
        print("4. Ver Historial de conversiones")
        
        print("\n5. Volver")
        
        opcion = pedirOpcion("\nSeleccione una opcion: ")
        if opcion == 5:
            print("Regresando...")
            return 
        match opcion:
            case 1:
                conversorPeso()
            case 2:
                conversorDistancia()
            case 3:
                conversorMoneda()
            case 4:
                historialConversiones()
            case _:
                print("Opcion invalida")

#===========================================================================================================================================#

#/////// MENUS ///////#

# ADMIN
def menuAdmin ():
    while True:
        print("\n"+"-"*30)
        print("="*30)
        print("MENU ADMIN".center(30))
        print("="*30)
        print("-"*30)
    
        print("\n1. Sistema Inventario") 
        print("2. Sistema Contactos") 
        print("3. Sistema Asistencia")
        print("4. Sistema Reservas") 
        print("5. Sistema Conversiones") 
        print("6. Sistema Tareas")
        
        print("\n7. Salir")
        
        seleccionAdmin = pedirOpcion("\nSeleccione una opcion: ")
        if seleccionAdmin == 7:
                    return("Saliendo...")
        else:
            match seleccionAdmin:
                case 1:
                    sistemaInventario()
                case 2:
                    sistemaContactos()
                case 3:
                    sistemaAsistencia()
                case 4:
                    sistemaReservas()
                case 5:
                    sistemaConversion()
                case 6:
                    sistemaTareas()
                case _:
                    print("Opcion invalida...")

# CAJERO
def menuCajero():
    while True:
        print("\n"+"-"*30)
        print("="*30)
        print("MENU CAJERO".center(30))
        print("="*30)
        print("-"*30)
    
        print("\n1. Ver Inventario")
        print("2. Buscar Producto")
        print("3. Conversor Unidades") 
        print("4. Asistencia") #Solo marcar asistencia y registrarse
        print("5. Tareas Asignadas") #Ver tareas asignadas
    
        print("\n6. Salir")
        
        seleccionCajero = pedirOpcion("\nSeleccione una opcion: ")
        if seleccionCajero == 6:
                    return("Saliendo...")
        else:
            match seleccionCajero:
                case 1:
                    visualizarInventario()
                case 2:
                    buscarProducto()
                case 3:
                    sistemaConversion()
                case 4:
                    marcarAsistencia()
                case 5:
                    tareasRol("Cajero")
                case _:
                    print("Opcion invalida...")
                    
# LOGISTICA
def menuLogistica():
    while True:
        print("\n"+"-"*30)
        print("="*30)
        print("MENU LOGISTICA".center(30))
        print("="*30)
        print("-"*30)
    
        print("\n1. Sistema Inventario") #Completo
        print("2. Conversor Unidades") 
        print("3. Asistencia") 
        print("4. Tareas Asignadas") 
    
        print("\n5. Salir")
        
        seleccionLogistica = pedirOpcion("\nSeleccione una opcion: ")
        if seleccionLogistica == 5:
                    return("Saliendo...")
        else:
            match seleccionLogistica:
                case 1:
                    sistemaInventario()
                case 2:
                    sistemaConversion()
                case 3:
                    marcarAsistencia()
                case 4:
                    tareasRol("Logistica")
                case _:
                    print("Opcion invalida...")

# DOMICILIARIO
def menuDomiciliario():
    while True:
        print("\n"+"-"*30)
        print("="*30)
        print("MENU DOMICILIARIO".center(30))
        print("="*30)
        print("-"*30)
    
        print("\n1. Ver Inventario")
        print("2. Buscar Producto")
        print("3. Conversor Unidades") 
        print("4. Asistencia") #Solo marcar asistencia y registrarse
        print("5. Tareas Asignadas") #Ver tareas asignadas
    
        print("\n6. Salir")
        
        seleccionDomi = pedirOpcion("\nSeleccione una opcion: ")
        if seleccionDomi == 6:
                    return("Saliendo...")
        else:
            match seleccionDomi:
                case 1:
                    visualizarInventario()
                case 2:
                    buscarProducto()
                case 3:
                    sistemaConversion()
                case 4:
                    marcarAsistencia()
                case 5:
                    tareasRol("Domiciliario")
                case _:
                    print("Opcion invalida...")