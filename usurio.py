def crear_perfil(nombre: str, edad: int, correo: str) -> dict:
    perfil = {
        "nombre": nombre,
        "edad": edad,
        "correo": correo
    }
    return perfil

def formatear_perfil(perfil: dict) -> str:
    return f"{perfil['nombre']} tiene {perfil['edad']} años y su correo es {perfil['correo']}"


if __name__ == "__main__":
    admin = crear_perfil("Pedro", 30, "jWk6f@example.com")
    print(formatear_perfil(admin))