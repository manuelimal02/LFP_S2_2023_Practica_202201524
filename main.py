from inventario_DAO import inventario_DAO
manejador_lista = inventario_DAO()

def menu_principal():
    print("--------------------------------------------------")
    print("Menú Principal – Sistema de Inventario            ")
    print("--------------------------------------------------")
    print("1. Cargar Inventario Inicial                      ")
    print("2. Cargar Instrucciones de Movimiento             ")
    print("3. Crear Informe de Inventario                    ")
    print("4. Salir                                          ")
    print("--------------------------------------------------")
    opcion = input("Ingrese Una Opción: ")
    if opcion == "1":
        cargar_inventario_inicial()
    elif  opcion == "2":
        cargar_instrucciones_movimiento()
    elif opcion == "3":
        crear_informe_inventario()
    elif opcion == "4":
        salir()
    else:
        print("--------------------------------------------------")
        print("OPCIÓN NO VÁLIDA")
        menu_principal()

def cargar_inventario_inicial():
    print("--------------------------------------------------")
    print("CARGAR INVENTARIO INICIAL")
    print("--------------------------------------------------")
    print("Ingrese la ruta del inventario a cargar:")
    ruta = input()
    print(" ")
    try:
        with open(ruta, "r") as archivo:
            for linea in archivo:
                palabras = linea.strip().replace("crear_producto ", "").split(';')
                manejador_lista.agregar_producto(palabras[0], palabras[1], palabras[2], palabras[3])
    except FileNotFoundError:
        print("El archivo no existe.")
        
    print("--------------------------------------")         
    print("¿Desea realizar otra operación?")
    print("1. Sí")
    print("2. No")
    print("--------------------------------------")
    opcion = input("Ingrese Una Opción: ")
    if opcion=="1":
        menu_principal()
    elif opcion=="2":
        salir()  
    else:
        print("--------------------------------------------------")
        print("OPCIÓN NO VALIDA")
        menu_principal()


def cargar_instrucciones_movimiento():
    print("--------------------------------------------------")
    print("CARGAR INSTRUCCIONES DE MOVIMIENTO")
    print("--------------------------------------------------")
    print("Ingrese la ruta de las instrucciones a cargar:")
    ruta = input()
    print(" ")
    try:
        with open(ruta, "r") as archivo:
            for linea in archivo:
                palabras = linea.strip().split(' ')
                instruccion = palabras[0]
                datos_producto = palabras[1].split(';')
                if instruccion == "agregar_stock":
                    manejador_lista.agregar_stock(datos_producto [0], datos_producto[2], int(datos_producto[1]))
                elif instruccion == "vender_producto":
                    manejador_lista.vender_producto(datos_producto [0], datos_producto[2], int(datos_producto[1]))
    except FileNotFoundError:
        print("El archivo no existe.")
        
    print("--------------------------------------")         
    print("¿Desea realizar otra operación?")
    print("1. Sí")
    print("2. No")
    print("--------------------------------------")
    opcion = input("Ingrese Una Opción: ")
    if opcion=="1":
        menu_principal()
    elif opcion=="2":
        salir()  
    else:
        print("--------------------------------------------------")
        print("OPCIÓN NO VALIDA")
        menu_principal()

def crear_informe_inventario():
    print("--------------------------------------------------")
    print("CREAR INFORME DE INVENTARIO")
    print("--------------------------------------------------")
    print("Ingrese el nombre del informe inventario a crear:")
    nombre = input()
    print(" ")
    manejador_lista.crear_informe(nombre +".txt")
    print("--------------------------------------")         
    print("¿Desea realizar otra operación?")
    print("1. Sí")
    print("2. No")
    print("--------------------------------------")
    opcion = input("Ingrese Una Opción: ")
    if opcion=="1":
        menu_principal()
    elif opcion=="2":
        salir()  
    else:
        print("--------------------------------------------------")
        print("OPCIÓN NO VALIDA")
        menu_principal()

def salir():
    print("--------------------------------------------------")
    print("PROGRAMA FINALIZADO, GRACIAS")


if __name__=="__main__":
    print("--------------------------------------------------")
    print("Práctica 1 – Lenguajes Formales Y De Programación ")
    print("202201524 – Carlos Manuel Lima y Lima             ")
    menu_principal()  

