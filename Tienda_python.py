import random

def cantidad_stock(stock): #Definir la cantidad de stock
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

def mostrar_productos(inventario, cantidad, precio): #Mostrar productos
    for ver in range(len(inventario)):
        print("N°", ver+1," Producto:", inventario[ver]," Stock:", cantidad[ver]," Precio:", precio[ver],"$")

def valor_inventario(inventario, cantidad, precio): #Mostrar valor total de todos los productos del inventario
    valor_por_stock = 0
    valor_total = 0
    for ver in range(len(inventario)):
        valor_por_stock = precio[ver] * cantidad[ver]
        valor_total += valor_por_stock
    print("")
    print("El valor total de su stock es de:", valor_total,"$")
    print("")

#----------------Creacion de catalogos----------------------
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
    cargamento = ["Lapiz", "Goma", "Birome", "Liquipaper", "Cuaderno"]
    for llenar in range(len(cargamento)):
        productos.append(cargamento[llenar])
        cantidad_stock(stock)
#----------------------------------------------------------

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
        elif cargamento[buscar] == "Lapiz" or cargamento[buscar] == "Birome" or cargamento[buscar] == "Cuaderno":
            precios.append(25)
        elif cargamento[buscar] == "Goma" or cargamento[buscar] == "Liquipaper":
            precios.append(10)
    print("")

def compras(cargamento, su_stock, su_precios, inventario, cantidad, precio, Billetera): #Realizar compras en los catalogos
    modo_compra = True
    while modo_compra == True:
        encontrado = True
        print("")
        print("Sus opciones disponibles:")
        print("")
        print("1) Comprar")
        print("2) Volver")
        print("")
        opcion = input("Ingrese (1) o (2) para avanzar: ")
        while opcion != "1" and opcion != "2":
            opcion = input("Solo es valido el ingreso de (1) o (2): ")
            print("")
        if opcion == "1":
            mostrar_productos(cargamento, su_stock, su_precios)
            print("")
            producto = input("Escriba el nombre del producto a comprar (Primera letra en Mayusculas): ")
            print("")
            for recorrer in range(len(cargamento)):
                if producto == cargamento[recorrer] and su_stock[recorrer] > 0: #Si se encuentra el producto y su stock es mayor a 0
                    producto_cargamento = cargamento[recorrer]
                    stock_producto = int(input("Ingrese la cantidad a comprar: "))
                    while stock_producto > su_stock[recorrer] and stock_producto <= 0:
                        stock_producto = int(input("Ingrese una cantidad valida: "))
                    precio_total = su_precios[recorrer] * stock_producto
                    print("Precio total de la compra:", precio_total)
                    if Billetera[0] >= precio_total: # Si el contenido de billetera es mayor al precio total del producto
                        producto_guardado = False
                        for comprobar in range(len(inventario)):
                            if inventario[comprobar] == producto_cargamento: #Si el producto se encuentra guardado en el inventario
                                producto_inventario = comprobar
                                producto_guardado = True
                        if producto_guardado == True: #Si ya esta guardado en el inventario
                            cantidad[producto_inventario] += stock_producto
                            su_stock[recorrer] -= stock_producto
                            Billetera[0] -= precio_total
                            billetera_pago = Billetera
                            print("")
                            print("Billetera tras pago: ", billetera_pago)
                            print("")
                        else:
                            inventario.append(cargamento[recorrer])
                            cantidad.append(stock_producto)
                            precio.append(su_precios[recorrer])
                            su_stock[recorrer] -= stock_producto
                            Billetera[0] -= precio_total
                            billetera_pago = Billetera
                            print("")
                            print("Billetera tras pago: ", billetera_pago)
                            print("")
                    else:
                        print("")
                        print("Su saldo es insuficiente para realizar esta compra")
                        print("")
                    encontrado = True
                else:
                    encontrado = False
            if encontrado == False: #Si no se encuentra el producto o su stock es menor a 0
                print("")
                print("Se ha interrumpido la accion, es posible que el producto ingresado no sea valido o no cuente con stock")
                print("")
            modo_compra = True
        else: 
            print("")
            print("Volviendo al menu anterior...")
            print("")
            modo_compra = False            
    borrado_de_catalogo(cargamento, su_stock, su_precios)

def borrado_de_catalogo(cargamento, su_stock, su_precios): #Borra las listas de los catalogos tras las compras
    maximo = len(cargamento)
    for borrar in range(maximo):
        del cargamento[0]
        del su_stock[0]
        del su_precios[0]

def gestion_inventario(inventario, cantidad, precio): #Menu del inventario
    modo_inventario = True
    while modo_inventario == True:
        print("")
        print("Sus opciones con su inventario son las siguientes:")
        print("")
        print("1) Ver inventario")
        print("2) Mostrar valor total de su inventario")
        print("3) Volver al menu principal")
        print("")
        opciones = input("Ingrese el numero de la opcion de su interes: ")
        while opciones != "1" and opciones != "2" and opciones != "3":
            opciones = input("Solo es valido el ingreso de (1) (2) y (3): ")
        if opciones == "1":
            if len(inventario) > 0:       
                print("")
                print("Su inventario actual contiene los siguientes productos:")
                print("")
                mostrar_productos(inventario, cantidad, precio)
            else:
                print("")
                print("Su inventario no tiene ningun producto guardado, realice una compra para poder visualizarlo")
                print("")
            modo_inventario = True
        elif opciones == "2":
            valor_inventario(inventario, cantidad, precio)
            modo_inventario = True
        else:
            print("")
            print("Regresando al menu principal...")
            print("")
            modo_inventario = False

#Funcion que permite visualizar los productos de la tienda
def tienda(inventario, cantidad, precio, Billetera): #Menu de la tienda
    cargamento = []
    su_stock = []
    su_precios = []
    modo_tienda = True
    print("Bienvenido a la tienda, aqui podra visualizar los productos disponibles por catalogo")
    while modo_tienda == True:
        print("Catalogos disponibles:")
        print("")
        print("1) Construccion")
        print("2) Frutas")
        print("3) Escolar")
        print("4) Volver al menu anterior")
        print("")
        opcion = input("Coloque el numero de la opcion de su interes: ")
        while opcion != "1" and opcion != "2" and opcion != "3" and opcion != "4":
            opcion = input("Solo son validos los numeros (1), (2), (3) y (4): ")
            print("")
        if opcion == "1":
            print("")
            print("Catalogo de construccion:")
            construccion(cargamento, su_stock)
            precios_unitarios(cargamento, su_precios)
            mostrar_productos(cargamento, su_stock, su_precios)
            compras(cargamento, su_stock, su_precios, inventario, cantidad, precio, Billetera)
            print("")
            modo_tienda = True
        elif opcion == "2":
            print("")
            print("Catalogo de frutas:")
            frutas(cargamento, su_stock)
            precios_unitarios(cargamento, su_precios)
            mostrar_productos(cargamento, su_stock, su_precios)
            compras(cargamento, su_stock, su_precios, inventario, cantidad, precio, Billetera)
            print("")
            modo_tienda = True
        elif opcion == "3":
            print("")
            print("Catalogo de escolar:")
            escolar(cargamento, su_stock)
            precios_unitarios(cargamento, su_precios)
            mostrar_productos(cargamento, su_stock, su_precios)
            compras(cargamento, su_stock, su_precios, inventario, cantidad, precio, Billetera)
            print("")
            modo_tienda = True
        else:
            print("")
            print("Volviendo al menu principal...")
            print("")
            modo_tienda = False

def Dinero_Billetera(Billetera): #Menu de la Billetera
    modo_billetera = True
    while modo_billetera == True:
        dinero_actual = Billetera[0]
        print("Saldo actual de su billetera:", dinero_actual,"$")
        print("¿Que desea realizar?")
        print("")
        print("1) Agregar dinero")
        print("2) Volver al menu principal")
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
            Billetera[0] += Dinero
            print("")
            print("Se agregaron:", Billetera[0]," a su Billetera")
            for mostrar in range(len(Billetera)):
                print("Su billetera cuenta con:", Billetera[mostrar],"$")
                print("")
        else:
            print("")
            print("Volviendo al menu principal...")
            print("")
            modo_billetera = False

def main(): #Ejecuta el menu principal del programa

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
        print("3) Opciones de inventario")
        print("4) Salir del programa")
        print("")
        opciones = input("Coloque el numero de la opcion a realizar: ")
        while opciones != "1" and opciones != "2" and opciones != "3" and opciones != "4":
            opciones = input("Solo (1) (2) (3) y (4) son validos: ")
        if opciones == "1":
            print("")
            Dinero_Billetera(Billetera)
            print("")
            programa = True
        elif opciones == "2":
            print("")            
            tienda(inventario, cantidad, precio, Billetera)
            print("")
            programa = True
        elif opciones == "3":
            gestion_inventario(inventario, cantidad, precio)
            programa = True
        else:
            print("")
            print("Entendido, saliendo de la tienda...")
            print("")
            print("¡Hasta la proxima!")
            programa = False

main()