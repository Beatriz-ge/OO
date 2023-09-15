DESCRI��O DO MINIPROJETO 1
(PSEUDOC�DIGO)

      Este pseudoc�digo implementa um sistema para intera��o do usu�rio com 3 objetos de formas bidimensionais, sendo eles: c�rculo, quadrado e tri�ngulo. O c�digo utiliza conceitos de classes, heran�a e encapsulamento aprendidos em sala de aula. Ou seja, o objetivo do pseudoc�digo � ser orientado a objeto.

ESTRUTURA DAS CLASSES

      As classes do pseudoc�digo est�o divididas em 4, sendo a classe FormaGeometrica, a classe m�e e as outras 3 classes referentes a cada forma geom�trica espec�fica, as classes filhas.
      
Abaixo segue a explica��o da fun��o de cada classe:

- Classe FormaGeometrica:
A classe FormaGeometrica � a classe base que serve como um modelo gen�rico para representar formas geom�tricas. Ela possui um atributo privado _tipo, que armazena uma descri��o da forma, e um m�todo construtor __init__ que recebe um par�metro 'tipo' e define o atributo _tipo com esse valor. Al�m disso, a classe FormaGeometrica declara um m�todo abstrato calcularArea(), que deve ser implementado nas classes filhas, e um m�todo de acesso getTipo() para obter o valor do atributo _tipo.

- Classe Circulo (Herda de FormaGeometrica):
A classe Circulo � uma subclasse da classe FormaGeometrica e representa um c�rculo. Ela possui um atributo privado _raio, que armazena o raio do c�rculo. O m�todo construtor __init__ recebe um par�metro 'raio' e define o atributo _raio com esse valor. A classe Circulo implementa o m�todo calcularArea(), que calcula a �rea do c�rculo usando a f�rmula p * raio^2. Al�m disso, ela fornece um m�todo de acesso getRaio() para obter o valor do atributo _raio.

- Classe Quadrado (Herda de FormaGeometrica):
A classe Quadrado � outra subclasse da classe FormaGeometrica e representa um quadrado. Ela possui um atributo privado _lado, que armazena o comprimento do lado do quadrado. O m�todo construtor __init__ recebe um par�metro 'lado' e define o atributo _lado com esse valor. A classe Quadrado implementa o m�todo calcularArea(), que calcula a �rea do quadrado usando a f�rmula lado^2. Ela tamb�m fornece um m�todo de acesso getLado() para obter o valor do atributo _lado.

- Classe Triangulo (Herda de FormaGeometrica):
A classe Triangulo � uma terceira subclasse da classe FormaGeometrica e representa um tri�ngulo. Ela possui atributos privados _base e _altura, que armazenam a base e a altura do tri�ngulo, respectivamente. O m�todo construtor __init__ recebe dois par�metros, 'base' e 'altura', e define os atributos _base e _altura com esses valores. A classe Triangulo implementa o m�todo calcularArea(), que calcula a �rea do tri�ngulo usando a f�rmula 0.5 * base * altura. Al�m disso, ela fornece m�todos de acesso getBase() e getAltura() para obter os valores dos atributos _base e _altura.

FUN��O PRINCIPAL

A fun��o principal do c�digo realiza as seguintes a��es:
1) Cria uma lista vazia chamadas 'formas'.
2) Cria objetos para representar um c�rculo, quadrado e tri�ngulo com medidas proporcionais definidas, usando os construtores das classes.
3) Adiciona os objetos � lista 'formas'.
4) Entra em um loop enquanto verdadeiro.
5) Exibe um menu de op��es para o usu�rio, permitindo que ele escolha entre diferentes opera��es relacionadas �s formas geom�tricas.
6) L� a op��o do usu�rio, com base na op��o selecionada, realiza uma das opera��es a seguir:
* Exibe as medidas de todos os elementos.
* Encontra o elemento de maior �rea e exibe seu tipo.
* Encontra o elemento de menor �rea e exibe seu tipo.
* Exibe a quantidade de lados de cada elemento.
* Encerra o programa.


Heran�a e Encapsulamento

      O conceito de heran�a � aplicado nas classes Circulo, Quadrado e Triangulo, que herdam os atributos e m�todos da classe base FormaGeometrica. Isso permite que as subclasses compartilhem caracter�sticas comuns e, ao mesmo tempo, implementem seus pr�prios m�todos espec�ficos.
      O encapsulamento � utilizado para proteger os atributos privados _tipo, _raio, _lado, _base e _altura, garantindo que eles s� possam ser acessados atrav�s dos m�todos de acesso apropriados (getTipo, getRaio, getLado, getBase e getAltura). Isso promove o princ�pio da encapsula��o, ocultando os detalhes de implementa��o dos atributos e fornecendo uma interface controlada para acess�-los.
