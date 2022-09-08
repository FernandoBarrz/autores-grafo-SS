# Apoyo para el desarrollo de infraestructura de software para la Secretaría de Enseñanza


_Proyecto para el [Instituto de Investigaciones Biomédicas](https://www.biomedicas.unam.mx/)_

![Undirected Weighted Graph](./config/undirected-graph.png)

---
## Tabla de contenidos
1. [Comenzando](#comenzando)
    * [Pre-requisitos](#pre-requisitos)
2. [Estructura del proyecto](#estructura)
3. [Guía de Instalación](#guía-de-Instalación)
    * [Dependencias](#instalación-de-dependencias)
5. [Ejecutando el programa](#ejecutando-el-programa)

----
# Comenzando

## Pre-requisitos
* Python 3.6+
* PIP 3 instalado
    * Para instalar pip para Python3:
        ```bash
        sudo apt update
        sudo apt install python3-pip
        ```

## Estructura
![Estructura del proyecto](./config/project-structure.png)

Carpetas del proyecto:
* __code/__ 
    * _Contiene el código fuente principal del proyecto_
    * __/graph__
        * _Contiene las definiciones de clases que se utilizan para crear la representación del grafó como estructura de datos (Graph class, Edge class, Vertex class)_
    * __/utils__
        * _Contiene los paquetes y modulos de ayuda que utiliza el programa_
* __input/__
    * Contiene el archivo .txt con los datos que representan las publicaciones del instituto.
* __output/__
    * Contiene la imagen que representa al grafó de forma gráfica (se debe instalar las librerias adicionales) 

## Guía de Instalación
### Instalación

1. Clonar el repositorio o descarga el archivo en formato .zip
    ```sh
    git clone https://github.com/FernandoBarrz/autores-grafo-SS.git
    ```
* Cambiar de directorio al la carpeta principal raíz (root directory)
    ```bash
    cd autores-grafo-ss/
    ```
* Reemplaza el archivo _.txt_ en la carpeta __/input__ (Si es necesario)


---
### Instalación de dependencias (Opcional)
> En el archivo requirements.txt contiene el nombre y la versión de las dependencias necesarias para la generación de la imágen del grafó generado por el programa.

* Estando ubicado en el directorio raíz, escribe
    ```sh
    pip install -r requirements.txt

    ```
* __Graphviz__ (Biblioteca de Python para trabajar con grafos)
        * Linux Distros:
            ```bash 
                sudo apt-get install graphviz
            ```
        * En MacOS X
            ```bash
                brew install graphviz
            ```
## Ejecutando el programa

1.  Para ejecutar la aplicación, se debe escribir lo siguiente en la terminal de linea de comandos. 

    En un sistema operativo basado en Linux/UNIX:
    ```sh
    python3 main.py
    ```
    En Windows OS
    ```sh
    py main.py
    ```
### Ejemplo de uso
![Example usage](./config/image-1.png)
![Example usage 2](./config/image-4.png)

------
## Contacto


Fernando Barrios - [/in/fernando-barrios/](https://www.linkedin.com/in/fernando-barrios/) - fernando.barrios.dev@gmail.com

------

## License

Distributed under the MIT License. 


