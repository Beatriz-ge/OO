# Código Fonte

Este é um projeto simples que demonstra a programação orientada a objetos para calcular áreas de diferentes formas geométricas, como círculos, quadrados e triângulos. O projeto é composto por dois arquivos principais:

1. **formas.py**: Este arquivo contém a definição das classes que representam as formas geométricas e suas operações. As classes são organizadas da seguinte forma:

   - `FormaGeometrica` (classe abstrata base): Define um método abstrato `calcular_area()` e fornece um método `get_tipo()` para obter o tipo da forma geométrica.
   - `Circulo`, `Quadrado` e `Triangulo` (subclasses): Herdam de `FormaGeometrica` e implementam o método `calcular_area()` específico para cada forma. Cada uma dessas classes também possui métodos para obter informações adicionais, como o raio, lado, base e altura.

2. **main.py**: Este é o arquivo principal que utiliza as classes definidas em `formas.py` para criar instâncias de formas geométricas e realizar operações com elas. As operações incluem a exibição das medidas de todas as formas, encontrar a forma com a maior área, encontrar a forma com a menor área e contar a quantidade de lados de cada forma.

## Linguagem Usada

O projeto foi desenvolvido em Python, uma linguagem de programação de alto nível amplamente utilizada devido à sua simplicidade e legibilidade. A programação orientada a objetos é uma técnica importante em Python, e este projeto demonstra como criar classes abstratas, herdar métodos e usar polimorfismo para lidar com diferentes tipos de formas geométricas.

## Programação Orientada a Objetos

Este projeto em Python demonstra de forma prática os princípios da Programação Orientada a Objetos (POO), incorporando os conceitos fundamentais de classe, herança, encapsulamento e polimorfismo.

A POO é uma metodologia de programação que se baseia na criação de objetos para representar entidades do mundo real e organizar o código em classes. Nesse projeto, aplicamos os seguintes conceitos de POO:

**- Classe:** Uma classe é um modelo ou um plano para criar objetos. Ela define os atributos (dados) e métodos (comportamentos) que os objetos da classe terão. No projeto, temos três classes principais:

1. `FormaGeometrica`: Uma classe abstrata que define um método abstrato `calcular_area()` e possui um método `get_tipo()` para obter o tipo da forma geométrica.

2. `Circulo`, `Quadrado` e `Triangulo`: São subclasses que herdam de `FormaGeometrica` e implementam o método `calcular_area()` para calcular a área de cada forma específica.

**- Herança:** A herança é um conceito que permite criar uma nova classe (subclasse) com base em uma classe existente (superclasse). Isso promove a reutilização de código e a especialização de comportamentos. No projeto, as classes `Circulo`, `Quadrado` e `Triangulo` herdam da classe abstrata `FormaGeometrica`, o que significa que elas têm acesso aos métodos e atributos da classe mãe. Isso facilita a criação de formas geométricas específicas enquanto compartilha a funcionalidade comum.

**- Encapsulamento:** Encapsulamento é o conceito de esconder detalhes de implementação e proteger os atributos de uma classe, permitindo o acesso controlado por meio de métodos. No projeto, os atributos das formas geométricas, como `_raio`, `_lado`, `_base` e `_altura`, são definidos como atributos protegidos, que podem ser acessados somente por métodos da própria classe. Isso garante que os dados das formas sejam manipulados de maneira segura e consistente.

**- Polimorfismo:** O polimorfismo permite que objetos de diferentes classes sejam tratados de maneira uniforme, desde que compartilhem uma interface comum. No projeto, o polimorfismo é aplicado ao encontrar a forma com a maior e a menor área. Usamos a função `max()` e `min()` com uma função lambda que chama o método `calcular_area()` de cada forma geométrica. Isso demonstra como objetos de diferentes classes podem ser comparados e manipulados de forma polimórfica.

