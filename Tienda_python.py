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
    Manzana = "Manzana"
    Pera = "Pera"
    Banana = "Banana"
    Sandia = "Sandia"
    Naranja = "Naranja"
    cargamento = [Manzana, Pera, Banana, Sandia, Naranja]
    for llenar in range(len(cargamento)):
        productos.append(cargamento[llenar])
        cantidad_stock(stock)

def escolar(productos, stock):
    Lapiz = "Lapiz"
    Goma = "Goma"
    Birome = "Birome"
    Liquipaper = "Liquipaper"
    Hoja_de_papel = "Hoja de papel"
    cargamento = [Lapiz, Goma, Birome, Liquipaper, Hoja_de_papel]
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
    print("¿Que desea hacer ahora?")
    print("1) Comprar")
    print("2) Volver")
    print("")
    hacer_compra = False
    opcion = int(input("Colocar el numero de su opcion: "))
    while opcion != 1 and opcion != 2:
        opcion = int(input("Solo son validos los numeros 1 y 2: "))
    print("")
    if opcion == 1:
        hacer_compra = True
    else: 
        print("Ok, se le regresara al menu anterior")
#######################################################################
    while hacer_compra == True:
        hacer_compra = False
        producto = input("Escriba el nombre del producto a comprar: ")
        for recorrer in range(len(cargamento)):
            if producto == cargamento[recorrer] and Billetera[0] >= su_precios[recorrer]:    
                Billetera[0] -= su_precios[recorrer]
                print("Billetera tras pago: ", Billetera)
                inventario.append(cargamento[recorrer])
                cantidad.append(su_stock[recorrer])
                precio.append(su_precios[recorrer])
                hacer_compra = True
        else:
            print("No es posible realizar la accion")
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

def tienda(inventario, cantidad, precio, Billetera):
    cargamento = []
    su_stock = []
    su_precios = []
    print("Bienvenido a la seccion de la tienda, aqui podra varios productos dependiendo del catalogo.")
    print("Los catalogos disponibles son los siguientes:")
    print("1) Construccion")
    print("2) Frutas")
    print("3) Escolar")
    print("")
    print("En caso de querer salir, precione 4")
    print("")
    tienda = False
    opcion = int(input("Coloque el numero del catalogo que resulte de su interes: "))
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

def Dinero_Billetera():
    Billetera = []
    Dinero = int(input("Ingrese el monto inicial de su Billetera: "))
    while Dinero < 500:
        print("El importe minimo permitido es de 500$")
        Dinero = int(input("Ingrese un monto valido: "))
    Billetera.append(Dinero)
    return Billetera

def main():
    inventario = []
    cantidad = []
    precio = []
    Billetera = Dinero_Billetera()
    interactuar = False
    print("Bienvenido al mercado ¿Que desea hacer?")
    print("")
    print("Opciones:")
    print("1) Tienda")
    print("2) Salir")
    print("")
    opciones = input("Coloque el numero de la opcion a realizar: ")
    while opciones != "1" and opciones != "2":
        opciones = input("Solo (1) y (2) son validos: ")
    if opciones == "1":
        interactuar = True
    else:
        interactuar = False
    while interactuar == True:
        interactuar = False
        print("")
        tienda(inventario, cantidad, precio, Billetera)
        print("Desea ver su inventario?")
        mostrar_productos(inventario, cantidad, precio)
        print("Su billetera:", Billetera)
        retomar = input("Coloque el numero de la opcion a realizar: ")
        while opciones != "1" and opciones != "2":
            retomar = input("Solo (1) y (2) son validos: ")
        if retomar == "1":
            interactuar = True
        else:
            print("Entendido, saliendo del mercado...")
    print("")
    print("¡Hasta la proxima!")

main()