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
* PIP 3 installed
    * Installing pip for Python 3
        * To install pip for Python 3 on Ubuntu 20.04 run the following commands as root or sudo user in your terminal:
            ```bash
                sudo apt update
                sudo apt install python3-pip
            ```
    * Or, use a virtual environment with __venv__
        ```bash
            python3 -m venv <project-name>
        ```
        ```bash
            source <project-name>/bin/activate
            python3 -m pip install --upgrade pip
        ```
* Graphviz (Python library to work with graphs) source code
    * Linux Distros:
        ```bash 
            sudo apt-get install graphviz
        ```
    * On MacOS X
        ```bash
            sudo apt-get install graphviz
        ```

<>
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
    ```bash
    git clone https://github.com/FernandoBarrz/autores-grafo-SS.git
    ```
2. Override the .txt file in the /input directory if necessary.
3. Move to the project root directory.
4. To install the dependencies:
    ```bash
        pip install -r requiremens.txt
    ```


---
### Dependencies (_Optional_)
> The requirements.txt file contains the required dependencies' version and name to run the app.
```bash
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
    py main_en.py
    ```

---

## Contact

Fernando Barrios - [/in/fernando-barrios/](https://www.linkedin.com/in/fernando-barrios/) - fernando.barrios.dev@gmail.com

Project Link: [https://github.com/FernandoBarrz/autores-grafo-SS](https://github.com/FernandoBarrz/autores-grafo-SS)

------

## License

Distributed under the MIT License. 
