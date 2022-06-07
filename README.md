[![Django CI](https://github.com/arm98sub/plataformaComercial/actions/workflows/django.yml/badge.svg?branch=main)](https://github.com/arm98sub/plataformaComercial/actions/workflows/django.yml)


# Plataforma Digital Comercial

Este reposotirio corresponde al desarrollo de una aplicacion web, que tiene como motivo realzar o mejorar las ventas del estado de Zacatecas, por medio de ventas por internet.
Dicha plataforma contara con un sistema de registro, tanto para vendedores como para usuarios que solamente quieran realizar una compra. :)

## Instalacion 
Para usar este programa, solo deberas contar con Python 3.9 y de la misma manera con su instalador de paquetes(PIP) y con git.
En caso de no contar con estos:

1. Si cuentas con Windows:
    - Descarga Python del siguiente link: [Python](https://www.python.org/downloads/)
        - Instala el archivo descargado, incluyendo "Python" en la path del sistema.
            - **En caso de Windows** pip ya vienen instalado.
    - Para instalar **git** solo ingresa al siguiente link: [Git](https://git-scm.com/downloads)
        - Descarga el archivo exe, ejecutalo y sigue los pasoso indicados por el instalador.
2. Estando en una distribucion Linux derivada de Debian:
    - Solo necesitas ejecutar los siguientes comandos:
    ```
    apt update 
    apt install python3 git python3-pip
    ```
3. Clonar el repositorio y realizar la instalacion de las dependencias.
    - Usando https:
    ```
    git clone https://github.com/arm98sub/plataformaComercial.git
    cd plataformaComercial
    ```
    - Usando SSH:
    ``` 
    git clone git@github.com:arm98sub/plataformaComercial.git
    cd plataformaComercial
    ```
    - Una vez clonado y estando en la carpeta del proyecto:
    ```
    pip install -r requirements.txt
    ```

## Tareas
### Usuario
- [x] Creacion de modelos para usuario y vendedor.
- [x] Creacion de modelos para categorias y productos.
- [x] Cambios a la interfaz
- [x] CRUD de usuarios.
- [x] CRUD productos.
- [ ] Despliegue en servidor.

### Administrador
- [x] Ver la lista de Usuarios
- [x] Ver la lista de productos


## Autores

- César Emmanuel Salatiel Reyes Gaytan
- Erick Alexandro Pinales Gonzalez
