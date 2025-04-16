import random

def linea_texto(): #Pone una linea para separar algunas secciones
    print("#######################################################################################")

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
        print("|| N°", ver+1," Producto:", inventario[ver]," Stock:", cantidad[ver]," Precio:", precio[ver],"$")

def valor_inventario(inventario, cantidad, precio): #Mostrar valor total de todos los productos del inventario
    valor_por_stock = 0
    valor_total = 0
    for ver in range(len(inventario)):
        valor_por_stock = precio[ver] * cantidad[ver]
        valor_total += valor_por_stock
    print("")
    print("El valor total de su stock es de:", valor_total,"$")
    print("")

def plus_de_venta(precio_total):
    precio_final = 0
    dinero_plus = 0
    print("")
    print("Calculando un posible monto extra...")
    plus = random.randint(1, 100)
    if plus <= 100 and plus >= 75:
        dinero_plus = precio_total * 0.90
    elif plus <= 74 and plus >= 50:
        dinero_plus = precio_total * 0.65
    elif plus <= 49 and plus >= 25:
        dinero_plus = precio_total * 0.35
    elif plus <= 24 and plus >= 10:
        dinero_plus = precio_total * 0.10
    else:
        dinero_plus = 0
    precio_final = precio_total + dinero_plus
    if precio_final > 0:
        print("")
        print("Se valido el monto extra, se sumara al dinero obtenido de la venta de su producto")
        print("")
    else:
        print("")
        print("No se valido el monto extra, el dinero recibido se mantiene")
        print("")
    return precio_final

def venta_stock(inventario, cantidad, precio, Billetera):
    stock_para_vender = True
    precio_vendido = 0
    while stock_para_vender == True:
        encontrado = False
        print("")
        mostrar_productos(inventario, cantidad, precio)
        print("")
        producto = input("Escriba el nombre del producto que guste vender (Primera letra en mayuscula): ")
        for ver in range(len(inventario)):
            if producto == inventario[ver] and cantidad[ver] > 0:
                precio_vendido = precio[ver]
                print("")
                cant_vender = int(input("Ingrese la cantidad que desee vender: "))
                while cant_vender > cantidad[ver] and cant_vender < 1:
                    print("")
                    cant_vender = int(input("Ingrese la cantidad que desee vender: "))
                precio_total = precio_vendido * cant_vender
                precio_final = plus_de_venta(precio_total)
                Billetera[0] += precio_final
                cantidad[ver] -= cant_vender
                dinero_tras_venta = Billetera[0]
                encontrado = True
        if encontrado == True:
            print("")
            print("¡Venta realizada con exito!")
            print("")
            print("Su inventario tras realizar la venta:")
            mostrar_productos(inventario, cantidad, precio)
            print("")
            print("Su billetera tras la venta:", dinero_tras_venta)
            print("")
        else:
            print("")
            print("El producto ingresado no cuenta con stock o no fue identificado")
            print("")
        print("¿Desea seguir vendiendo stock de su inventario?")
        print("")
        seguir = input("Ingrese (s) o (n) para continuar: ")
        while seguir != "s" and seguir != "n":
            print("")
            seguir = input("Solo son validos el ingreso de (s) o (n): ")
        if seguir == "s":
            print("")
            print("Retomando ventas...")
            print("")
            stock_para_vender = True
        else:
            print("")
            print("Volviendo al menu anterior...")
            print("")
            stock_para_vender = False
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

def compras(cargamento, su_stock, su_precios, inventario, cantidad, precio, Billetera): #Realizar compras en los catalogos
    modo_compra = True
    while modo_compra == True:
        encontrado = False
        print("")
        linea_texto()
        print("")
        print("Opciones disponibles del catalogo:")
        print("")
        print("1) Comprar un producto")
        print("s) Volver")
        print("")
        opcion = input("Ingrese (1) o (s) para avanzar: ")
        print("")
        while opcion != "1" and opcion != "s":
            opcion = input("Solo es valido el ingreso de (1) o (s): ")
            print("")
        linea_texto()
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
                    print("")
                    while stock_producto > su_stock[recorrer] and stock_producto <= 0:
                        stock_producto = int(input("Ingrese una cantidad valida: "))
                        print("")
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
                            billetera_pago = Billetera[0]
                            encontrado = True
                            print("")
                            print("Billetera tras pago: ", billetera_pago)
                            print("")
                        else: #Sino, se guarda
                            inventario.append(cargamento[recorrer])
                            cantidad.append(stock_producto)
                            precio.append(su_precios[recorrer])
                            su_stock[recorrer] -= stock_producto
                            Billetera[0] -= precio_total
                            billetera_pago = Billetera[0]
                            encontrado = True
                            print("")
                            print("Billetera tras pago: ", billetera_pago)
                            print("")
                    else:
                        print("")
                        print("Su saldo es insuficiente para realizar esta compra")
                        print("")
            if encontrado == True: #Si se logra realizar la compra
                linea_texto()
                print("")
                print("¡Se pudo realizar con exito la compra!")
            else:
                linea_texto()
                print("")
                print("No se pudo realizar la accion, posibles motivos:")
                print("-Saldo insufiente")
                print("-Nombre de producto erroneo")
                print("-Producto desconocido")
                print("-Producto con stock agotado")
                print("")
                print("Verifique su billetera o si el producto buscado esta registrado o si pertenece a otro catalogo")
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

def gestion_inventario(inventario, cantidad, precio, Billetera): #Menu del inventario
    modo_inventario = True
    while modo_inventario == True:
        linea_texto()
        print("")
        print("Sus opciones con su inventario son las siguientes:")
        print("")
        print("1) Ver inventario")
        print("2) Mostrar valor total de su inventario")
        print("3) Vender stock")
        print("s) Volver al menu principal")
        print("")
        opciones = input("Ingrese la opcion de su interes: ")
        print("")
        linea_texto()
        while opciones != "1" and opciones != "2" and opciones != "3" and opciones != "s":
            print("")
            opciones = input("Solo es valido el ingreso de (1) (2) (3) y (s): ")   
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
            if len(inventario) > 0:       
                valor_inventario(inventario, cantidad, precio)
                modo_inventario = True
            else:
                print("")
                print("Su inventario no tiene ningun producto guardado, realice una compra para poder obtener su valor total")
                print("")
        elif opciones == "3":
            if len(inventario) > 0:       
                venta_stock(inventario, cantidad, precio, Billetera)
                modo_inventario = True
            else:
                print("")
                print("Su inventario no tiene ningun producto guardado, realice una compra para poder hacer una venta")
                print("")
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
    while modo_tienda == True:
        linea_texto()
        print("")
        print("Catalogos disponibles para su compra:")
        print("")
        print("1) Construccion")
        print("2) Frutas")
        print("3) Escolar")
        print("s) Volver al menu anterior")
        print("")
        opcion = input("Ingrese la opcion de su interes: ")
        while opcion != "1" and opcion != "2" and opcion != "3" and opcion != "s":
            print("")
            opcion = input("Solo son validos los numeros (1), (2), (3) y (s): ")
        if opcion == "1":
            print("")
            print("Catalogo de construccion:")
            construccion(cargamento, su_stock)
            precios_unitarios(cargamento, su_precios)
            mostrar_productos(cargamento, su_stock, su_precios)
            compras(cargamento, su_stock, su_precios, inventario, cantidad, precio, Billetera)
            modo_tienda = True
        elif opcion == "2":
            print("")
            print("Catalogo de frutas:")
            frutas(cargamento, su_stock)
            precios_unitarios(cargamento, su_precios)
            mostrar_productos(cargamento, su_stock, su_precios)
            compras(cargamento, su_stock, su_precios, inventario, cantidad, precio, Billetera)
            modo_tienda = True
        elif opcion == "3":
            print("")
            print("Catalogo de escolar:")
            escolar(cargamento, su_stock)
            precios_unitarios(cargamento, su_precios)
            mostrar_productos(cargamento, su_stock, su_precios)
            compras(cargamento, su_stock, su_precios, inventario, cantidad, precio, Billetera)
            modo_tienda = True
        else:
            print("")
            print("Volviendo al menu principal...")
            print("")
            modo_tienda = False

def gestion_Billetera(Billetera): #Menu de la Billetera
    modo_billetera = True
    while modo_billetera == True:
        dinero_actual = Billetera[0]
        linea_texto()
        print("")
        print("¿Que desea realizar?")
        print("")
        print("1) Ver billetera")
        print("2) Agregar dinero")
        print("s) Volver al menu principal")
        print("")
        opciones = input("Ingrese (1) o (s) para continuar: ")
        while opciones != "1" and opciones != "2" and opciones != "s":
            print("")
            opciones = input("Solo son validos (1) o (s): ")
        if opciones == "1":
            print("")
            linea_texto()
            print("")
            print("El saldo actual de su billetera es de:", dinero_actual,"$")
            print("")
            print("Si quiere aumentarlo agregue sus propios montos o venda productos de su inventario")
            print("")
        elif opciones == "2":
            print("")
            linea_texto()
            print("")
            Dinero = int(input("Ingrese el monto inicial de su Billetera: "))
            while  Dinero < 500 or Dinero > 3000:
                print("El importe permitido para ingresar es de 500$ - 3000$")
                print("")
                Dinero = int(input("Ingrese un monto valido: "))
            Billetera[0] += Dinero
            dinero_actual = Billetera[0]
            print("")
            print("Se agregaron:", Dinero,"$ a su billetera")
            print("Su billetera cuenta con:", dinero_actual,"$")
            print("")
        else:
            print("")
            print("Volviendo al menu principal...")
            modo_billetera = False

def main(): #Ejecuta el menu principal del programa
    inventario = []
    cantidad = []
    precio = []
    Billetera = [0]
    programa = True
    linea_texto()
    print("")
    print("¡Bienvenido al programa de la tienda!")
    print("Sientase libre de probar nuestros servicios")
    print("")
    while programa == True:
        programa = False
        linea_texto()
        print("")
        print("Opciones para cliente:")
        print("")
        print("1) Gestionar Billetera")
        print("2) Ver productos")
        print("3) Opciones de inventario")
        print("s) Salir del programa")
        print("")
        opciones = input("Coloque el numero de la opcion a realizar: ")
        while opciones != "1" and opciones != "2" and opciones != "3" and opciones != "s":
            print("")
            opciones = input("Solo (1) (2) (3) y (s) son validos: ")
        if opciones == "1":
            print("")
            gestion_Billetera(Billetera)
            print("")
            programa = True
        elif opciones == "2":
            print("")            
            tienda(inventario, cantidad, precio, Billetera)
            print("")
            programa = True
        elif opciones == "3":
            print("")
            gestion_inventario(inventario, cantidad, precio, Billetera)
            print("")
            programa = True
        else:
            print("")
            linea_texto()
            print("")
            print("Entendido, saliendo de la tienda...")
            print("")
            print("¡Hasta la proxima!")
            print("")
            linea_texto()
            print("")
            programa = False

main()