import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from service import fetch_personas

app = FastAPI(
    title="API Personas",
    description="Servicio que genera una lista de 10 personas usando randomuser.me",
    version="1.0.0",
)

# Configuracion CORS para permitir llamadas desde el frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/personas", response_class=JSONResponse)
def get_personas():
    """
    Endpoint que retorna una lista de 10 personas
    con nombre, genero, ubicacion, email, fecha de nacimiento y fotografia.
    """
    personas = fetch_personas()
    return {"personas": personas}


@app.get("/")
def root():
    return {
        "mensaje": "Bienvenido a la API de Personas",
        "docs": "/docs",
        "endpoint": "/api/personas",
    }


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=False)
