import httpx

RANDOMUSER_URL = "https://randomuser.me/api/?results=10"


def fetch_personas():
    """
    Obtiene 10 personas de randomuser.me y las transforma al formato requerido.
    Retorna una lista de diccionarios con:
    - nombre
    - genero
    - ubicacion
    - email
    - fecha_nacimiento
    - fotografia
    """
    response = httpx.get(RANDOMUSER_URL, timeout=10.0)
    response.raise_for_status()
    data = response.json()

    personas = []
    for result in data.get("results", []):
        nombre = f"{result['name']['first']} {result['name']['last']}"
        genero = result.get("gender", "")
        ubicacion = (
            f"{result['location']['city']}, {result['location']['country']}"
        )
        email = result.get("email", "")
        fecha_nacimiento = result.get("dob", {}).get("date", "")
        fotografia = result.get("picture", {}).get("large", "")

        personas.append(
            {
                "nombre": nombre,
                "genero": genero,
                "ubicacion": ubicacion,
                "email": email,
                "fecha_nacimiento": fecha_nacimiento,
                "fotografia": fotografia,
            }
        )

    return personas
