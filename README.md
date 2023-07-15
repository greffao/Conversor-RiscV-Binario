# Conversor-RiscV-Binario

*Lucas Greff Meneses - 13671615 <br>
Henrique Souza Marques - 11815722 <br>
Eduardo Neves Gomes da Silva - 13822710 <br>
Vinicius Carneiro Macedo - 11915752 <br> <br>
Instituto de Ciências Matemáticas e de Computação <br>
Universidade de São Paulo* <br>

**Resumo:** Esta monografia tem o objetivo de apresentar o segundo trabalho prático da disciplina de Organização e Arquitetura de Computadores. Dentro das propostas apresentadas e dos desafios encontrados pelos participantes do grupo decidimos fazer uma aplicação que converte alguns códigos da RISC-V para seus respectivos códigos em binário.

### Introdução

A RISC-V é uma arquitetura de conjunto de instruções livres que faz a comunicação entre o alto nível dos computadores com o baixo nível. Essa comunicação se dá pela conversão dos comandos dos vários tipos, como “beq” do “Tipo B”, para palavras de 32 bits que são interpretados pelos processadores, assim executando os programas. Nesse cenário acaba surgindo um problema que é a nossa dificuldade, que é olharmos o código em binário e sermos capaz de interpretá-lo ou conferir se ele está correto.

### Desenvolvimento

Nesta seção, será apresentado o método utilizado por nós para agilizar o processo de verificação e interpretação das instruções convertidas para binário. Optamos por utilizar a linguagem de programação Python para gerar nosso programa, onde mapeamos os tipos e suas instruções. Os tipos mapeados foram: B, I, J, R, S e U. Cada membro ficou responsável por desenvolver a parte do código que trata cada tipo, assim desenvolvendo funcionalidades que convertem os conjuntos de instruções para binário e os divide e explica conforme determina a arquitetura RISC-V.

### Conclusão

Construímos uma aplicação em Python capaz de converter instruções da RiscV para binário e separar essa sequência em partes correspondentes às características de cada instrução.

**Referências:** The RISC-V Instruction Set Manual Volume I: User-Level ISA Document Version 2.2

