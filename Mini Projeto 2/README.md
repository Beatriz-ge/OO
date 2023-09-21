# Código Fonte 

### Descrição

Este projeto em é uma demonstração simples da programação orientada a objetos (POO). Ele permite calcular áreas de diferentes formas geométricas, como círculos, quadrados e triângulos, com base em medidas proporcionais definidas pelo usuário.

### Linguagem

O projeto é desenvolvido em Python, uma linguagem de programação de alto nível amplamente utilizada para desenvolvimento de software.

### Estrutura do Projeto

O projeto está estruturado em dois arquivos principais:

- `formas.py`: Este arquivo contém as definições das classes relacionadas às formas geométricas, incluindo `FormaGeometrica`, `Circulo`, `Quadrado` e `Triangulo`. Ele demonstra conceitos de herança e polimorfismo da POO, onde cada classe filha herda características da classe pai `FormaGeometrica` e implementa seu próprio método `calcularArea()` para calcular a área específica da forma.

- `main.py`: Este arquivo contém a função principal `main()`, que é responsável por interagir com o usuário e coordenar as operações com as instâncias das classes definidas em `formas.py`. Aqui, conceitos de encapsulamento são demonstrados ao acessar atributos privados das classes usando métodos de acesso (`getTipo`, `getRaio`, `getLado`, `getBase`, `getAltura`).

