# Support for the development of software infrastructure for the Ministry of Education

[![en](https://img.shields.io/badge/lang-es-green.svg)](https://github.com/FernandoBarrz/autores-grafo-SS/)         Spanish 👈
## About the project
> A command line app that automates the process of registering collaboration between authors' research work in the form of a graph (data structure). This app uses some input files containing researchers' names from the institute and the bibliographic information gathered from published materials and then it process it to generate a undirected weighted graph representing those collaborations.

__Project for the [Biomedical Research Institute](https://www.biomedicas.unam.mx/)__

![Undirected Weighted Graph](./config/undirected-graph.png)

---
### Built With
* Pytohn 3.6+
----

## Table of contents
Contents
1. [Get Started](#getting-started)
    * [Prerequisites](#prerequisites)
2. [Project Structure](#project-structure)
3. [Installation](#installation)
    * Optional Dependencies
5. [Usage](#usage)
6. [Contact](#contact)

----
# Getting Started


### Prerequisites
* Python 3.6+ Installed
* ...
* ...

## Project Structure 
![Project Structure](./config/project-structure.png)

### Project directories and files:
* __code/__ 
    * _Contains the main source code_
    * __utils/__
        * _Contains the packages and modules used by the program_
* __config/__
* __input/__
    * _Contains the .txt files with the authors' names and the publication's data._
* __output/__
    * _Contains a .txt file auto generated from the data. Representing the collaborations. Optionally a PDF also can be generated_
----
## Installation

1. Clone the repo
    ```sh
    git clone https://github.com/FernandoBarrz/autores-grafo-SS.git
    ```
2. Override the .txt file in the /input directory if necessary.
3. Move to the project root directory.

---
### Dependencies (_Optional_)
> En el archivo requirements.txt contiene el nombre y la versión de las dependencias necesarias para la ejecución de la aplicación
```sh
pip install -r requirements.txt
```

## Usage
1.  To use the command line app on your computer, execute the main_en.py file. 

    On a Linux/UNIX based OS:
    ```sh
    python3 main_en.py
    ```
    On Windows OS
    ```sh
    python main_en.py
    ```

---

## Contact

Fernando Barrios - [/in/fernando-barrios/](https://www.linkedin.com/in/fernando-barrios/) - fernando.barrios.dev@gmail.com

Project Link: [https://github.com/FernandoBarrz/autores-grafo-SS](https://github.com/FernandoBarrz/autores-grafo-SS)

------

## License

Distributed under the MIT License. 
