import json
def crear_perfil(nombre: str, edad: int, correo: str) -> dict:
    perfil = {
        "nombre": nombre,
        "edad": edad,
        "correo": correo
    }
    return perfil

def formatear_perfil(perfil: dict) -> str:
    return json.dumps(perfil, indent=2, ensure_ascii=False)


if __name__ == "__main__":
    admin = crear_perfil("Pedro", 30, "jWk6f@example.com")
    print(formatear_perfil(admin))