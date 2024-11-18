""" sistema de gestión de información para una empresa de transporte """    
def Clientes(): 
    try: 
        with open("Final2\\Maestro_clientes.txt", "a+",) as archivo: 
            archivo.seek(0) 
            contenido = archivo.readline() 

            if not contenido.strip(): 
                archivo.write("Cod. Cliente, Nombre y Apellido\n") 

            nuevo_cliente = input("¿Quieres registrar un nuevo cliente (si/no): ") 
            if nuevo_cliente.lower() == "si": 
                codigo = int(input("Ingrese el código del Cliente: ")) 
                NyACliente = input("Ingrese el nombre y apellido del Cliente: ") 
                archivo.write(",".join([str(codigo).ljust(3), str(NyACliente).ljust(30)]) + "\n") 
                print("Cliente registrado correctamente")
    except FileNotFoundError: 
        print("El archivo no pudo abrirse, se creará uno nuevo") 


def localidad():
    try:
        with open ("Final2\\Localidades.txt", "a+") as archivo:
            archivo.seek(0)
            contenido = archivo.readline()

            if not contenido.strip():
                archivo.write("Id_localidad, Descripción de la localidad\n")

            nueva_localidad = input("¿Quieres registrar una nueva localidad (si/no): ")
            if nueva_localidad.lower() == "si":
                id_localidad = input("Ingrese la id de la localidad: ")
                descripcion_local = input("Ingrese la descripción de la localidad: ")
                archivo.write(",".join([str(id_localidad).ljust(3), str(descripcion_local).ljust(25)]) + "\n")
                print("Localidad registrada")
    except FileNotFoundError:
        print("El archivo no pudo abrirse, se creará uno nuevo")

def lineas():
    try:
        with open("Final2\\lineas_colectivo.txt", "a+") as archivo:
            archivo.seek(0)
            contenido2 = archivo.readline()

            if not contenido2.strip():
                archivo.write("Codigo Linea, Descripción de la Linea, Hora Cabecera, Lunes, Martes, Miercoles, Jueves, Viernes, Sabado, Domingo\n")
            
            nueva_linea = input("¿Quieres registrar una nueva línea de Colectivo (si/no): ")
            if nueva_linea.lower() == "si":
                Cod_Linea = input("Ingrese el código de la nueva línea de colectivo: ")
                Descripcion = input("Ingrese la descripción del nuevo colectivo: ")
                hora = input("Ingrese la hora cabecera del colectivo: ")
                lunes = input("Ingrese la hora del lunes: ")
                martes = input("Ingrese la hora del martes: ")
                miercoles = input("Ingrese la hora del miércoles: ")
                jueves = input("Ingrese la hora del jueves: ")
                viernes = input("Ingrese la hora del viernes: ")
                sabado = input("Ingrese la hora del sábado: ")
                domingo = input("Ingrese la hora del domingo: ")

                archivo.write(",".join([
                    f"{Cod_Linea}".ljust(3),
                    f"{Descripcion}".ljust(15),
                    f"{hora}".ljust(10),
                    f"{lunes}".ljust(8),
                    f"{martes}".ljust(8),
                    f"{miercoles}".ljust(8),
                    f"{jueves}".ljust(8),
                    f"{viernes}".ljust(8),
                    f"{sabado}".ljust(8),
                    f"{domingo}".ljust(8)
                ]) + "\n")
                print("Nueva línea registrada.")
    
    except FileNotFoundError:
        print("El archivo no pudo abrirse, se creará uno nuevo")

def tarifas():
    try:
        with open("Final2\\tarifas_colectivo.txt", "a+") as archivo:
            archivo.seek(0)
            contenido2 = archivo.readline()

            if not contenido2.strip():
                archivo.write("Id_tarifa, Codigo de Linea, Id Localidad desde, Id localidad hasta, Precio Boleto, Hora salida \n")
            
            nueva_tarifa = input("¿Quieres registrar una nueva tarifa? (si/no): ")
            if nueva_tarifa.lower() == "si":
                Id_tarifa = input("Ingrese el id de la Tarifa: ")
                cod_linea = input("Ingrese el codigo de la linea: ")
                Id_localidad_prin = input("Ingrese la id de la localidad de partida: ")
                Id_localidad_fin = input("Ingrese la id de la localidad de destino: ")
                precio_bo = input("Ingrese el precio del boleto: ")
                hora_salida = input("Ingrese el horario de salida: ")

                archivo.write(",".join([
                    Id_tarifa.ljust(10),
                    cod_linea.ljust(15),
                    Id_localidad_prin.ljust(20),
                    Id_localidad_fin.ljust(20),
                    precio_bo.ljust(15),
                    hora_salida.ljust(15)
                ]) + "\n")
                print("Nueva tarifa registrada con éxito.")
            else:
                print("Operación cancelada.")
    except FileNotFoundError:
        print("El archivo tarifas_colectivo.txt no pudo abrirse.")

def novedad_ventas():
    try:
        with open("Final2\\novedad_ventas.txt", "a+") as archivo:
            archivo.seek(0)
            contenido2 = archivo.readline()

            if not contenido2.strip():
                archivo.write("Id Ventas, Cod. Cliente, Cod. de Línea, Id localidad desde, Id localidad hasta, Precio Boleto, Hora Salida, fecha (dia/mes/año), Cantidad de Pasaje comprado, Registro Siguiente por Cliente, Registro Anterior por Cliente \n")
            
            nueva_tarifa = input("¿Quieres registrar una nueva Venta? (si/no): ")
            if nueva_tarifa.lower() == "si":
                Id_ventas = input("Ingrese el id de Ventas: ")
                cod_cliente = input("Ingrese el código de Cliente: ")
                cod_linea = input("Ingrese el código de la línea: ")
                Id_localidad_prin = input("Ingrese la id de la localidad de partida: ")
                Id_localidad_fin = input("Ingrese la id de la localidad de destino: ")
                precio_bo = input("Ingrese el precio del boleto: ")
                hora_salida = input("Ingrese el horario de salida: ")
                fecha = input("Ingrese la fecha (formato: dia/mes/año): ")
                cant_pasaje = input("Ingrese la cantidad de pasajes comprados: ")
                reg_siguiente = input("Ingrese el registro siguiente por Cliente (o para ninguno): ")
                reg_anterior = input("Ingrese el registro anterior por Cliente (o para ninguno): ")

                archivo.write(",".join([
                    Id_ventas.ljust(10),
                    cod_cliente.ljust(10),
                    cod_linea.ljust(15),
                    Id_localidad_prin.ljust(20),
                    Id_localidad_fin.ljust(20),
                    precio_bo.ljust(15),
                    hora_salida.ljust(15),
                    fecha.ljust(15),
                    cant_pasaje.ljust(10),
                    reg_siguiente.ljust(10),
                    reg_anterior.ljust(10)
                ]) + "\n")
                print("Nueva Venta registrada con éxito.")
            else:
                print("Operación cancelada.")
    except FileNotFoundError:
        print("El archivo novedad_ventas.txt no pudo abrirse.")


def pantalla_carga():
    while True:
        codigo_linea = input("Código de línea: ")

        
        try:
            with open("Final2\\lineas_colectivo.txt", "r") as archivo_lineas:
                encontrado = False
                for linea in archivo_lineas:
                    partes = linea.strip().split(",")
                    if partes[0].strip() == codigo_linea:
                        descripcion_linea = partes[1].strip()
                        hora_cabecera = partes[2].strip()
                        encontrado = True
                        break
                if not encontrado:
                    print(f"No se encontró información para el código {codigo_linea} en lineas_colectivo.txt")
                    return
        except FileNotFoundError:
            print("El archivo lineas_colectivo.txt no existe.")
            return

        
        codigo_cliente = input("Código de cliente: ")

        
        try:
            with open("Final2\\Maestro_clientes.txt", "r") as archivo_clientes:
                encontrado = False
                for linea in archivo_clientes:
                    partes = linea.strip().split(",")
                    if partes[0].strip() == codigo_cliente:
                        nombre_apellido_cliente = partes[1].strip()
                        encontrado = True
                        break
                if not encontrado:
                    print(f"No se encontró información para el código {codigo_cliente} en Maestro_clientes.txt")
                    return
        except FileNotFoundError:
            print("El archivo Maestro_clientes.txt no existe.")
            return

        
        localidad_desde = input("Localidad desde (Id): ")
        
        localidad_hasta = input("Localidad hasta (Id): ")

        
        try:
            with open("Final2\\Localidades.txt", "r") as archivo_localidades:
                descripcion_localidad_desde = None
                descripcion_localidad_hasta = None
                for linea in archivo_localidades:
                    partes = linea.strip().split(",")
                    if partes[0].strip() == localidad_desde:
                        descripcion_localidad_desde = partes[1].strip()
                    elif partes[0].strip() == localidad_hasta:
                        descripcion_localidad_hasta = partes[1].strip()
                    if descripcion_localidad_desde and descripcion_localidad_hasta:
                        break
                if descripcion_localidad_desde is None:
                    print(f"No se encontró la localidad con ID {localidad_desde}")
                    return
                if descripcion_localidad_hasta is None:
                    print(f"No se encontró la localidad con ID {localidad_hasta}")
                    return
        except FileNotFoundError:
            print("El archivo Localidades.txt no existe.")
            return

        
        hora_salida = None
        try:
            with open("Final2\\lineas_colectivo.txt", "r") as archivo_lineas:
                for linea in archivo_lineas:
                    partes = linea.strip().split(",")
                    if partes[0].strip() == codigo_linea:
                        hora_salida = partes[2].strip()
                        break
                if hora_salida is None:
                    print(f"No se encontró la hora de salida para la línea con código {codigo_linea}")
                    return
        except FileNotFoundError:
            print("El archivo lineas_colectivo.txt no existe.")
            return

        
        precio_boleto = None
        try:
            with open("Final2\\tarifas_colectivo.txt", "r") as archivo_tarifas:
                for linea in archivo_tarifas:
                    partes = linea.strip().split(",")
                    if partes[1].strip() == codigo_linea and partes[2].strip() == localidad_desde and partes[3].strip() == localidad_hasta:
                        precio_boleto = partes[4].strip()
                        break
                if precio_boleto is None:
                    print(f"No se encontró el precio del boleto para la línea {codigo_linea} y las localidades desde {localidad_desde} hasta {localidad_hasta}")
                    return
        except FileNotFoundError:
            print("El archivo tarifas_colectivo.txt no existe.")
            return

        
        fecha_pasaje = input("Fecha del pasaje (dd/mm/yyyy): ")

        
        cantidad_pasajes = input("Cantidad de pasajes: ")

        
        importe_total = float(precio_boleto) * int(cantidad_pasajes)

        
        print(f"Código de cliente: {codigo_cliente} Nombre y apellido: {nombre_apellido_cliente}")
        print(f"Localidad desde: {localidad_desde} Descripción localidad: {descripcion_localidad_desde}")
        print(f"Localidad hasta: {localidad_hasta} Descripción localidad: {descripcion_localidad_hasta}")
        print(f"Hora salida: {hora_salida}")
        print(f"Precio Boleto: {precio_boleto}")
        print(f"Fecha del pasaje: {fecha_pasaje} Cantidad de pasajes: {cantidad_pasajes}")
        print(f"Importe total: {importe_total}")

    
        opcion = input("\nIngrese 'g' para grabar, 'c' para cancelar y 's' para salir: ")
        if opcion.lower() == 'g':
            with open("Final2\\archivo_salida.txt", "a+") as archivo:
                archivo.write(f"Código de cliente: {codigo_cliente}, Nombre y apellido: {nombre_apellido_cliente}\n")
                archivo.write(f"Localidad desde: {localidad_desde}, Descripción localidad: {descripcion_localidad_desde}\n")
                archivo.write(f"Localidad hasta: {localidad_hasta}, Descripción localidad: {descripcion_localidad_hasta}\n")
                archivo.write(f"Hora salida: {hora_salida}\n")
                archivo.write(f"Precio Boleto: {precio_boleto}\n")
                archivo.write(f"Fecha del pasaje: {fecha_pasaje}, Cantidad de pasajes: {cantidad_pasajes}\n")
                archivo.write(f"Importe total: {importe_total}\n\n")
            print("Datos grabados exitosamente en archivo_salida.txt.")
        elif opcion.lower() == 's':
            print("Saliendo de la función pantalla_carga.")
            break  
        else:
            print("Operación cancelada.")

################Bloque principal#############

while True:
    print("\nMenú de opciones:")
    print("1. Cargar pantalla")
    print("2. Consultar clientes")
    print("3. Consultar localidades")
    print("4. Consultar líneas de colectivo")
    print("5. Consultar tarifas")
    print("6. Registrar novedad de ventas")
    print("0. Salir")

    opcion = input("Seleccione una opción (0-6): ")

    if opcion == '1':
        pantalla_carga()
    elif opcion == '2':
        Clientes()
    elif opcion == '3':
        localidad()
    elif opcion == '4':
        lineas()
    elif opcion == '5':
        tarifas()
    elif opcion == '6':
        novedad_ventas()
    elif opcion == '0':
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida. Intente nuevamente.")