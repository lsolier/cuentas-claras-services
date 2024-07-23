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
export FLASK_APP=src/app.py FLASK_ENV=development TESTING=False FLASK_DEBUG=1 FLASK_APP_NAME=cuentas_claras_services
gunicorn --bind 0.0.0.0:9005 manage:app --log-level debug --reload
```
