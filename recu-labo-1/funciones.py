import json
import csv


servicios = []


def cargar_archivo():
    global servicios
    ruta_archivo = r'C:\Users\mi pc\Desktop\nuevo p\datos.json'  
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as f:
            servicios = json.load(f)
        print(f'Se han cargado {len(servicios)} servicios del archivo {ruta_archivo}.')
    except FileNotFoundError:
        print(f'El archivo {ruta_archivo} no se encontró.')

# Esta funcion hace que la lista tenga una forma mas ordenada
def imprimir_lista():
    if servicios:
        print("{:<12} {:<30} {:<15} {:<15} {:<10} {:<20}".format(
            "ID Servicio", "Descripción", "Tipo", "Precio Unitario", "Cantidad", "Cliente"
        ))
        for servicio in servicios:
            print("{:<12} {:<30} {:<15} {:<15} {:<10} {:<20}".format(
                servicio['id_servicio'], servicio['descripcion'], servicio['tipo'],
                servicio['precioUnitario'], servicio['cantidad'], servicio['cliente']
            ))
    else:
        print("No hay servicios cargados.")


asignar_incremento = lambda servicio: {**servicio, 'precioUnitario': str(float(servicio['precioUnitario']) * 1.1)}

#  Esta funcion filtra por tipo y guarda la informacion en un nuevo archivo JSON
def filtrar_por_tipo(tipo):
    servicios_filtrados = [servicio for servicio in servicios if servicio['tipo'].lower() == tipo.lower()]
    nombre_archivo_salida = f'servicios_{tipo.lower()}.json'
    with open(nombre_archivo_salida, 'w', encoding='utf-8') as f:
        json.dump(servicios_filtrados, f, indent=4, ensure_ascii=False)
    print(f'Se han guardado {len(servicios_filtrados)} servicios del tipo "{tipo}" en el archivo {nombre_archivo_salida}.')

# Esta funcion muestra los servicios por cliente de manera ascendente
def mostrar_servicios_ordenados():
    servicios_ordenados = sorted(servicios, key=lambda x: x['cliente'])
    print("{:<20} {:<12} {:<30} {:<15} {:<15} {:<10}".format(
        "Cliente", "ID Servicio", "Descripción", "Tipo", "Precio Unitario", "Cantidad"
    ))
    for servicio in servicios_ordenados:
        print("{:<20} {:<12} {:<30} {:<15} {:<15} {:<10}".format(
            servicio['cliente'], servicio['id_servicio'], servicio['descripcion'], servicio['tipo'],
            servicio['precioUnitario'], servicio['cantidad']
        ))


def guardar_servicios_csv():
    nombre_archivo_csv = 'servicios_ordenados.csv'
    try:
        with open(nombre_archivo_csv, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            # Escribir encabezados
            writer.writerow(['Cliente', 'ID Servicio', 'Descripción', 'Tipo', 'Precio Unitario', 'Cantidad'])
            # Escribir cada servicio
            for servicio in servicios:
                writer.writerow([servicio['cliente'], servicio['id_servicio'], servicio['descripcion'],
                                 servicio['tipo'], servicio['precioUnitario'], servicio['cantidad']])
        print(f'Se ha guardado el listado de servicios ordenados por cliente en el archivo {nombre_archivo_csv}.')
    except IOError:
        print(f'Error al guardar el archivo {nombre_archivo_csv}.')


def main():
    while True:
        print("\n----- Menú Principal -----")
        print("1) Cargar archivo")
        print("2) Imprimir lista")
        print("3) Asignar incremento")
        print("4) Filtrar por tipo")
        print("5) Mostrar servicios ordenados por cliente")
        print("6) Guardar servicios en CSV")
        print("7) Salir")

        opcion = input("\nIngrese el número de opción deseada: ")

        if opcion == '1':
            cargar_archivo()
        elif opcion == '2':
            imprimir_lista()
        elif opcion == '3':
            global servicios
            servicios = list(map(asignar_incremento, servicios))
            print("Se ha aplicado un incremento del 10% al precio unitario de todos los servicios.")
        elif opcion == '4':
            tipo = input("Ingrese el tipo de servicio a filtrar: ")
            filtrar_por_tipo(tipo)
        elif opcion == '5':
            mostrar_servicios_ordenados()
        elif opcion == '6':
            guardar_servicios_csv()
        elif opcion == '7':
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, ingrese un número del 1 al 7.")

# Ejecutar el programa
if __name__ == "__main__":
    main()
