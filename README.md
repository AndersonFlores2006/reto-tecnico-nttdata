# API de Personas

Servicio que genera una lista de 10 personas usando la API de randomuser.me.

## Tecnologias

- **Backend**: FastAPI (Python). Lo elegi porque es rapido, moderno y genera documentacion automatica en `/docs`.
- **HTTP Client**: httpx (para llamar a randomuser.me).
- **Frontend**: HTML5 + CSS3 + JavaScript vanilla. Una sola pagina que consume la API con `fetch()`.

> Todo el codigo de logica de negocio fue escrito manualmente. Lo unico del framework es la estructura base de FastAPI (instanciacion, decoradores, middleware CORS).

## Estructura

```
backend/
  main.py        # Servidor FastAPI
  service.py     # Llama a randomuser.me y transforma los datos
  requirements.txt
frontend/
  index.html     # Pagina unica
  app.js         # Fetch y renderizado de tarjetas
  styles.css     # Estilos responsive con CSS Grid
```

## Instalacion

1. Crear entorno virtual e instalar dependencias:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r backend/requirements.txt
```

2. Ejecutar el backend:

```bash
cd backend
python main.py
```

El servidor se levanta en `http://localhost:8000`.

- Endpoint: `GET /api/personas`
- Docs interactivas: `http://localhost:8000/docs`

3. Abrir el frontend:

Solo abrir `frontend/index.html` en el navegador (doble click) o usar Live Server en VS Code.

> El backend debe estar corriendo para que el frontend cargue los datos.

## Respuesta de la API

```json
{
  "personas": [
    {
      "nombre": "John Doe",
      "genero": "male",
      "ubicacion": "New York, USA",
      "email": "john.doe@example.com",
      "fecha_nacimiento": "1990-05-21T10:30:00.000Z",
      "fotografia": "https://randomuser.me/api/portraits/men/1.jpg"
    }
  ]
}
```

## Notas

- CORS esta habilitado para permitir que el frontend se comunique con el backend aunque corran en puertos distintos.
- El frontend formatea la fecha a espanol y usa un layout responsive (grid en desktop, una columna en movil).


ANDERSON FLORES
