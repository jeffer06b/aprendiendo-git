# Crear un diccionario con información ficticia de una persona
informacion_personal = {
    "nombre": "Carlos Pérez",
    "edad": 25,
    "ciudad": "Quito",
    "profesion": "Estudiante"
}

# Imprimir diccionario inicial
print("Diccionario inicial:", informacion_personal)

# 1. Acceder al valor de 'ciudad' y modificarlo
informacion_personal["ciudad"] = "Guayaquil"
print("\nCiudad modificada:", informacion_personal)

# 2. Agregar o modificar la clave 'profesion'
informacion_personal["profesion"] = "Ingeniero en Sistemas"
print("\nProfesión actualizada:", informacion_personal)

# 3. Verificar existencia de la clave 'telefono'
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0999999999"
print("\nDespués de verificar/agregar teléfono:", informacion_personal)

# 4. Eliminar la clave 'edad'
informacion_personal.pop("edad")
print("\nDespués de eliminar 'edad':", informacion_personal)

# 5. Imprimir el diccionario final
print("\nDiccionario final:", informacion_personal)