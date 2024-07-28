# Grupo 28
Repositorio del proyecto legado a modernizar.

## Ejecución local

### Requisitos

- Pyhton 3.10

### Configurar Python e instalar dependencias
```bash
python3 -m venv venv
source venv/bin/activate
pip3 install --upgrade pip
pip3 install -r requirements.txt
```
### Ejecución de aplicación

Ejecución desde consola: 
```bash
export DEV_DATABASE_URL=postgresql://postgres:postgres@localhost:5435/cuentas-claras
export FLASK_APP=src/app.py FLASK_ENV=development TESTING=False FLASK_DEBUG=1 FLASK_APP_NAME=cuentas_claras_services
gunicorn --bind 0.0.0.0:8000 manage:app --log-level debug --reload
```
## Ejecución en contenedor

**Importante** no modificar la variable PORT para que coincida con la planificada en el despliegue

```bash
docker build -t cuentas-claras-services:1.0.0 .
docker run -e PORT=9005 -e DEV_DATABASE_URL=postgresql://postgres:postgres@localhost:5435/cuentas-claras -p 8000:8000 --name cuentas-claras-services cuentas-claras-services:1.0.0
```

## Ejecución de base datos en container
```bash
docker run --name cuentas-claras-db -e POSTGRES_PASSWORD=postgres -e POSTGRES_DB=cuentas-claras -p 5435:5432 -d postgres
```
