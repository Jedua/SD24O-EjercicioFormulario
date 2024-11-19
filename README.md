# SD24O-EjercicioFormulario

Tarea 2 **FastAPI** que permite registrar usuarios mediante un formulario HTML. las fotografías se guardan en el sistema de archivos, organizadas según si el usuario es VIP o no.

---

## Características

- **Formulario HTML** para registrar usuarios con los campos:
  - Nombre
  - Dirección
  - Fotografía
  - Checkbox para indicar si es VIP
- **API REST** para:
  - Crear usuarios mediante solicitudes JSON.
  - Obtener todos los usuarios registrados.
- **PostgreSQL** como base de datos para almacenar los datos de los usuarios ver. 2.
- **Sistema de archivos** para guardar las fotografías en carpetas específicas:
  - `fotos-usuarios-vip`: Fotografías de usuarios VIP.
  - `fotos-usuarios`: Fotografías de usuarios no VIP.

---

## Requisitos

- **Python 3.8 o superior**
- **PostgreSQL** instalado y configurado
- Paquetes de Python:
  - `fastapi`
  - `uvicorn`
  - `sqlalchemy`
  - `psycopg2-binary`

---

## Instalación

1. Clona este repositorio:
   ```bash
   git clone https://github.com/Jedua/SD24O-EjercicioFormulario.git
   cd SD24O-EjercicioFormulario
