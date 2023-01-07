# fastApi initial scaffolding

# creacion entorno virtual

Creal entorno virtaul con la libreria de preferencia, en este caso se realiza con
virtualenv

1.  clonar repositorio e ingresar a la carpeta
2.  pip3 install virtualenv
3.  dentro de la carpeta crear entorno virtual: virtualenv venv
4.  activar entorno virtual(linux): source venv/bin/activate
5.  descargar dependencias: pip3 o pip install -r requirements.txt

# correr proyecto

1. crear archivo .env como el ejemplo env.example con la constante SECRET=string o lo que quieras
2. abrir consola en la raiz de la carpeta y escribir:
   uvicorn src.main:app --reload --port 8000 --host 0.0.0.0
3. documentacion api, url asignado/docs# ej: http://127.0.0.1:8000/docs#
