import random

#Funcion para definir la cantidad de stock
def cantidad_stock(stock):
    cantidad = random.randint(1, 100)
    
    if cantidad <= 100 and cantidad >= 76:
        stock.append(100)
    elif cantidad <= 75 and cantidad >= 51:
        stock.append(75)
    elif cantidad <= 50 and cantidad >= 26:
        stock.append(50)
    else:
        stock.append(25)
    return stock

#Funcion para mostrar los productos
def mostrar_productos(inventario, cantidad, precio):
    for ver in range(len(inventario)):
        print("N°", ver+1," Producto:", inventario[ver]," Stock:", cantidad[ver]," Precio:", precio[ver],"$")

#Funciones para traer los catalogos##################################################################################################
def construccion(productos, stock):
    cargamento = ["Madera", "Concreto", "Cemento", "Tuberia", "Ladrillo"]
    for llenar in range(len(cargamento)):
        productos.append(cargamento[llenar])
        cantidad_stock(stock)

def frutas(productos, stock):
    cargamento = ["Manzana", "Pera", "Banana", "Sandia", "Naranja"]
    for llenar in range(len(cargamento)):
        productos.append(cargamento[llenar])
        cantidad_stock(stock)

def escolar(productos, stock):
    cargamento = ["Lapiz", "Goma", "Birome", "Liquipaper", "Hoja_de_papel"]
    for llenar in range(len(cargamento)):
        productos.append(cargamento[llenar])
        cantidad_stock(stock)

def precios_unitarios(cargamento, precios):
    for buscar in range(len(cargamento)):
        if cargamento[buscar] == "Concreto" or cargamento[buscar] == "Cemento" or cargamento[buscar] == "Madera":
            precios.append(150)
        elif cargamento[buscar] == "Tuberia" or cargamento[buscar] == "Ladrillo":
            precios.append(100)
        elif cargamento[buscar] == "Manzana" or cargamento[buscar] == "Pera" or cargamento[buscar] == "Naranja":
            precios.append(75)
        elif cargamento[buscar] == "Banana" or cargamento[buscar] == "Sandia":
            precios.append(50)
        elif cargamento[buscar] == "Lapiz" or cargamento[buscar] == "Birome" or cargamento[buscar] == "Hoja de papel":
            precios.append(25)
        elif cargamento[buscar] == "Goma" or cargamento[buscar] == "Liquipaper":
            precios.append(10)
    print("")

#Funcion para realizar compras en los catalogos########################################################################################

def compras(cargamento, su_stock, su_precios, inventario, cantidad, precio, Billetera):
    print("Sus opciones disponibles:")
    print("")
    print("1) Comprar")
    print("2) Volver")
    print("")
    hacer_compra = False
    comprobante = False
    opcion = int(input("Ingrese (1) o (2) para avanzar: "))
    while opcion != 1 and opcion != 2:
        opcion = int(input("Solo es valido el ingreso de (1) y (2): "))
    print("")
    if opcion == 1:
        hacer_compra = True
    else: 
        print("Ok, se le regresara al menu anterior")
    while hacer_compra == True:
        hacer_compra = False
        mostrar_productos(cargamento, su_stock, su_precios)
        print("")
        producto = input("Escriba el nombre del producto a comprar (Primera letra en Mayusculas): ")
        print("")
        #Recorre la lista en busca del producto
        for recorrer in range(len(cargamento)):
            #Si lo encuentra permite la compra
###Arreglar la condicion para que se realice correctamente la compra
            if producto == cargamento[recorrer]:
                comprobante = True
                stock_producto = int(input("Ingrese la cantidad a comprar: "))
                while stock_producto > su_stock[recorrer] or stock_producto <= 0:
                    stock_producto = int(input("Ingrese una cantidad valida: "))
                precio_total = su_precios[recorrer] * stock_producto
                print("Precio total de la compra:", precio_total)
                if Billetera[0] > precio_total:
                    Billetera[0] -= precio_total
                    su_stock[recorrer] -= stock_producto
                    inventario.append(cargamento[recorrer])
                    cantidad.append(su_stock[recorrer])
                    precio.append(su_precios[recorrer])
                    hacer_compra = True
                else:
                    print("Su saldo es insuficiente para realizar esta compra")
                    print("")
            else:
                comprobante = False
                hacer_compra = True
        if comprobante == False:
            print("No se pudo realizar la accion, posibles causas:")
            print("-Saldo insuficiente.")
            print("-Nombre de producto no valido.")
            print("")
        else:
            print("¡La compra se realizado con exito!")
            print("")
        
            hacer_compra = True
        print("¿Desea seguir comprando?")
        opcion = int(input("Marque (1) para continuar o (2) para salir: "))
        while opcion != 1 and opcion != 2:
            opcion = int(input("Solo son validos los numeros 1 y 2: "))
            print("")
        if opcion == 1:
            hacer_compra = True
        else: 
            print("Ok, se le regresara al menu anterior")
            hacer_compra = False  
    print("")
    print("Billetera tras pago: ", Billetera)
    print("Se regresara a la fase anterior")

def borrado_de_catalogo(cargamento, su_stock, su_precios):
    cargamento.clear()
    su_stock.clear()
    su_precios.clear()

#Funcion que permite visualizar los productos de la tienda
def tienda(inventario, cantidad, precio, Billetera):
    cargamento = []
    su_stock = []
    su_precios = []
    print("Bienvenido a la tienda, aqui podra visualizar los productos disponibles por catalogo:")
    print("Sus opciones disponibles:")
    print("")
    print("1) Construccion")
    print("2) Frutas")
    print("3) Escolar")
    print("")
    print("4) Volver al menu anterior")
    print("")
    tienda = False
    opcion = int(input("Coloque el numero de la opcion de su interes: "))
    print("")
    while opcion != 1 and opcion != 2 and opcion != 3 and opcion != 4:
        opcion = int(input("Solo son validos los numeros (1), (2), (3) y (4): "))
    if opcion == 1 or opcion == 2 or opcion == 3:
        tienda = True
    else:
        tienda = False
    while tienda == True:
        tienda = False
        if opcion == 1:
            print("Catalogo de construccion:")
            construccion(cargamento, su_stock)
            precios_unitarios(cargamento, su_precios)
            mostrar_productos(cargamento, su_stock, su_precios)
            compras(cargamento, su_stock, su_precios, inventario, cantidad, precio, Billetera)
            borrado_de_catalogo(cargamento, su_stock, su_precios)
            print("Billetera tras pago: ", Billetera)
            tienda = True
            print("")

        elif opcion == 2:
            print("Catalogo de frutas:")
            frutas(cargamento, su_stock)
            precios_unitarios(cargamento, su_precios)
            mostrar_productos(cargamento, su_stock, su_precios)
            compras(cargamento, su_stock, su_precios, inventario, cantidad, precio, Billetera)
            borrado_de_catalogo(cargamento, su_stock, su_precios)
            tienda = True
            print("")

        else:
            print("Catalogo de escolar:")
            escolar(cargamento, su_stock)
            precios_unitarios(cargamento, su_precios)
            mostrar_productos(cargamento, su_stock, su_precios)
            compras(cargamento, su_stock, su_precios, inventario, cantidad, precio, Billetera)
            borrado_de_catalogo(cargamento, su_stock, su_precios)
            tienda = True
            print("")
        print("")
        print("¿Quiere ver otros catalogos?")
        print("1) Construccion")
        print("2) Frutas")
        print("3) Escolar")
        print("")
        print("En caso de querer salir, precione 4")
        print("")
        opcion = int(input("Coloque el numero del catalogo que resulte de su interes: "))
        print("")
        while opcion != 1 and opcion != 2 and opcion != 3 and opcion != 4:
            opcion = int(input("Solo son validos los numeros (1), (2), (3) y (4): "))
        if opcion == 1 or opcion == 2 or opcion == 3:
            tienda = True
        else:
            tienda = False
            print("Saliendo...")          
    print("Se le regresara al menu principal")
    print("")

#Funcion para gestionar la Billetera del usuario
def Dinero_Billetera(Billetera):
    dinero_actual = Billetera[0]
    print("Actualmente su Billetera cuenta con:", dinero_actual,"$")
    print("¿Desea hacer una recarga de ingresos a su billetera?")
    print("1) Agregar dinero")
    print("2) Volver al menu anterior")
    print("")
    opciones = input("Ingrese (1) o (2) para continuar: ")
    while opciones != "1" and opciones != "2":
        opciones = input("Solo son validos (1) o (2): ")
    if opciones == "1":
        print("")
        Dinero = int(input("Ingrese el monto inicial de su Billetera: "))
        while Dinero < 500:
            print("El importe minimo permitido es de 500$")
            Dinero = int(input("Ingrese un monto valido: "))
        Billetera.append(Dinero)
        for mostrar in range(len(Billetera)):
            print("Su billetera cuenta con:", Billetera[mostrar],"$")
            print("")
    else:
        print("Volviendo al menu anterior...")
        print("")

#Funcion que representa el menu principal del programa
def main():
    inventario = []
    cantidad = []
    precio = []
    Billetera = [0]
    programa = True
    print("Bienvenido al mercado ¿Que desea hacer?")
    while programa == True:
        programa = False
        print("")
        print("Opciones para cliente:")
        print("")
        print("1) Gestionar Billetera")
        print("2) Ver productos")
        print("3) Ver inventario")
        print("4) Salir del programa")
        print("")
        #Cambiar para que se mantenga el bucle de las opciones
        opciones = input("Coloque el numero de la opcion a realizar: ")

        while opciones != "1" and opciones != "2" and opciones != "3" and opciones != "4":
            opciones = input("Solo (1) (2) (3) y (4) son validos: ")

        if opciones == "1":
            Dinero_Billetera(Billetera)
            print("")
            programa = True

        elif opciones == "2":            
            tienda(inventario, cantidad, precio, Billetera)
            print("")
            programa = True
   
        elif opciones == "3":
            if len(inventario) > 0:
                mostrar_productos(inventario, cantidad, precio)
                print("")
            else:
                print("Su inventario no tiene ningun producto guardado, realice una compra para poder visualizarlo")
                print("")
            programa = True
        
        else:
            print("Entendido, saliendo de la tienda...")
            programa = False
    print("")
    print("¡Hasta la proxima!")

main()