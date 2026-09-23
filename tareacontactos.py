
contacto= {}

def agregar_contacto(nombre, telefono): 
    if nombre not in contacto: 
        contacto [nombre] = telefono
        print(f"Contacto {nombre} agregado con éxito.")
    else:
        print(f"El contacto {nombre} ya existe.")

def mostrar_contactos():
    print("\n=== Lista de Contactos ===")
    if contacto:
        for nombre, telefono in contacto.items():
            print(f"Nombre: {nombre}, Teléfono: {telefono}")
    else:
        print("No hay contactos registrados.")
    print("==========================\n")

def buscar_contacto(nombre):
    if nombre in contacto:
        print(f"Contacto encontrado: Nombre: {nombre}, Teléfono: {contacto[nombre]}")
    else:
        print(f"El contacto {nombre} no existe.")

agregar_contacto("Ana", "0988876888")
agregar_contacto("Juan", "0988844888")
agregar_contacto("Raul", "0986544677")

mostrar_contactos()

buscar_contacto("Ana")
buscar_contacto("Pedro")

                 