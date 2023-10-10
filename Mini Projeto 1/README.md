# **PSEUDOCÓDIGO**

Este pseudocódigo implementa um sistema para interação do usuário com 3 objetos de formas bidimensionais, sendo eles: círculo, quadrado e triângulo. O código utiliza conceitos de classes, herança e encapsulamento aprendidos em sala de aula. Ou seja, o objetivo do pseudocódigo é ser orientado a objeto.

## **ESTRUTURA DAS CLASSES**

As classes do pseudocódigo estão divididas em 4, sendo a classe FormaGeometrica, a classe mãe e as outras 3 classes referentes a cada forma geométrica específica, as classes filhas.

Abaixo segue a explicação da função de cada classe:

### **- Classe FormaGeometrica:**
A classe FormaGeometrica é a classe base que serve como um modelo genérico para representar formas geométricas. Ela possui um atributo privado _tipo, que armazena uma descrição da forma, e um método construtor __init__ que recebe um parâmetro 'tipo' e define o atributo _tipo com esse valor. Além disso, a classe FormaGeometrica declara um método abstrato calcularArea(), que deve ser implementado nas classes filhas, e um método de acesso getTipo() para obter o valor do atributo _tipo.

### **- Classe Circulo (Herda de FormaGeometrica):**
A classe Circulo é uma subclasse da classe FormaGeometrica e representa um círculo. Ela possui um atributo privado _raio, que armazena o raio do círculo. O método construtor __init__ recebe um parâmetro 'raio' e define o atributo _raio com esse valor. A classe Circulo implementa o método calcularArea(), que calcula a área do círculo usando a fórmula p * raio^2. Além disso, ela fornece um método de acesso getRaio() para obter o valor do atributo _raio.

### **- Classe Quadrado (Herda de FormaGeometrica):**
A classe Quadrado é outra subclasse da classe FormaGeometrica e representa um quadrado. Ela possui um atributo privado _lado, que armazena o comprimento do lado do quadrado. O método construtor __init__ recebe um parâmetro 'lado' e define o atributo _lado com esse valor. A classe Quadrado implementa o método calcularArea(), que calcula a área do quadrado usando a fórmula lado^2. Ela também fornece um método de acesso getLado() para obter o valor do atributo _lado.

### **- Classe Triangulo (Herda de FormaGeometrica):**
A classe Triangulo é uma terceira subclasse da classe FormaGeometrica e representa um triângulo. Ela possui atributos privados _base e _altura, que armazenam a base e a altura do triângulo, respectivamente. O método construtor __init__ recebe dois parâmetros, 'base' e 'altura', e define os atributos _base e _altura com esses valores. A classe Triangulo implementa o método calcularArea(), que calcula a área do triângulo usando a fórmula 0.5 * base * altura. Além disso, ela fornece métodos de acesso getBase() e getAltura() para obter os valores dos atributos _base e _altura.

## **FUNÇÃO PRINCIPAL**

A função principal do código realiza as seguintes ações:

1. Cria uma lista vazia chamada 'formas'.
2. Cria objetos para representar um círculo, quadrado e triângulo com medidas proporcionais definidas, usando os construtores das classes.
3. Adiciona os objetos à lista 'formas'.
4. Entra em um loop enquanto verdadeiro.
5. Exibe um menu de opções para o usuário, permitindo que ele escolha entre diferentes operações relacionadas às formas geométricas.
6. Lê a opção do usuário, com base na opção selecionada, realiza uma das operações a seguir:
   - Exibe as medidas de todos os elementos.
   - Encontra o elemento de maior área e exibe seu tipo.
   - Encontra o elemento de menor área e exibe seu tipo.
   - Exibe a quantidade de lados de cada elemento.
   - Encerra o programa.

## **Herança e Encapsulamento**

O conceito de herança é aplicado nas classes Circulo, Quadrado e Triangulo, que herdam os atributos e métodos da classe base FormaGeometrica. Isso permite que as subclasses compartilhem características comuns e, ao mesmo tempo, implementem seus próprios métodos específicos.

O encapsulamento é utilizado para proteger os atributos privados _tipo, _raio, _lado, _base e _altura, garantindo que eles só possam ser acessados através dos métodos de acesso apropriados (getTipo, getRaio, getLado, getBase e getAltura). Isso promove o princípio da encapsulação, ocultando os detalhes de implementação dos atributos e fornecendo uma interface controlada para acessá-los.
