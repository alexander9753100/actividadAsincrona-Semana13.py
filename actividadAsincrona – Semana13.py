#saludo de bienvenida
 
print("BIENVENIDO A NUESTRO CODIGO\n")

# Lista de integrantes del grupo

integrantes = [
    {"nombre": "Xiomara", "apellido": "Cisneros", "sexo": "f", "edad": 18, "departamento": "Chalatenango", "municipio": "nueva concepcion", "direccion": "av.rio lempa calle el progreso"},
    {"nombre": "Bryan", "apellido": "Pineda", "sexo": "M", "edad": 19, "departamento": "chalatenango", "municipio": "nueva concepcion", "direccion": "av.rio lempa calle el progreso"},
    {"nombre": "Jesus", "apellido": "landaverde", "sexo": "M", "edad": 18, "departamento": "chalatenango", "municipio": "cabezera de chalatenango", "direccion": "barrios las flores chalatenango"},
    {"nombre": "Luis", "apellido": "Ábrego", "sexo": "M", "edad": 17, "departamento": "Chalatenango", "municipio": " Nueva Trinidad", "direccion": "Carretera principal hacia arcatao"},
    {"nombre": "Wendy", "apellido": "Ayala", "sexo": "F", "edad": 18, "departamento": "Chalatenango", "municipio": "Nueva concepción", "direccion": "trespuertas"},
    {"nombre": "Eduardo", "apellido": " Sales", "sexo": "M", "edad": 19, "departamento": "Chalatenango", "municipio": " Dulce Nombre de María", "direccion": " Calle central contiguo a alcaldía municipal"}
]

# Función que muestra el menú y devuelve el integrante seleccionado

def seleccionar_integrante(integrantes):
    print("\nSeleccione un integrante:\n")
    for integrante in integrantes:
        print(f"{integrante['nombre']}")
    while True:
        seleccion = input("\nIngrese el nombre del integrante: ")
        for integrante in integrantes:
            if seleccion.lower() == integrante['nombre'].lower():
                return integrante
        print("\nIntegrante no encontrado. Por favor, ingrese un nombre válido.")

# Función que muestra los detalles de un integrante

def mostrar_detalles(integrante):
    print("\nNombre: " + integrante['nombre'])
    print("Apellido: " + integrante['apellido'])
    print("Sexo: " + integrante['sexo'])
    print("Edad: " + str(integrante['edad']))
    print("Departamento: " + integrante['departamento'])
    print("Municipio: " + integrante['municipio'])
    print("Dirección: " + integrante['direccion'])

# Función principal

def main():
    while True:
        respuesta = input("\n¿Desea seleccionar un integrante? (si/no): ")
        if respuesta.lower() == 'si':
            integrante_seleccionado = seleccionar_integrante(integrantes)
            mostrar_detalles(integrante_seleccionado)
        else:
            break

if __name__ == '__main__':
    main()
print("\nGRACIAS POR TU TIEMPO\n")