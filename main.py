from fastapi import FastAPI, Form, File, UploadFile
from fastapi.responses import HTMLResponse
from pathlib import Path
import os

app = FastAPI()


BASE_DIR = Path(__file__).parent  # Carpeta donde está el script main.py
VIP_DIR = BASE_DIR / "fotos-usuarios-vip"
NON_VIP_DIR = BASE_DIR / "fotos-usuarios"

VIP_DIR.mkdir(parents=True, exist_ok=True)
NON_VIP_DIR.mkdir(parents=True, exist_ok=True)

@app.get("/", response_class=HTMLResponse)
async def formulario():
    with open(BASE_DIR / "index.html", "r") as file: 
        return HTMLResponse(content=file.read())

# Registro de usuarios
@app.post("/registro")
async def registrar_usuario(
    nombre: str = Form(...),
    direccion: str = Form(...),
    fotografia: UploadFile = File(...),
    vip: bool = Form(False)
):
    # Seleccionar el directorio según el estado VIP
    directorio_destino = VIP_DIR if vip else NON_VIP_DIR

    # Guardar la fotografía en el directorio correspondiente
    file_path = directorio_destino / fotografia.filename
    with open(file_path, "wb") as f:
        f.write(await fotografia.read())

    # Imprimir datos en la terminal
    print(f"Nombre: {nombre}")
    print(f"Dirección: {direccion}")
    print(f"VIP: {'Sí' if vip else 'No'}")
    print(f"Fotografía guardada en: {file_path}")

    return {"mensaje": "Usuario registrado exitosamente"}
