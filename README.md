# API tests

Este projeto de testes composto por alguns tipos de teste para um serviço responsável pela conversão de um número inteiro para sua grafia por extenso

os tipos de testes que compõem o projeto atualmente são:
* Testes de contrato, visando se os requisitos especificados no projeto são cumpridos;
* Testes de stress, onde estamos vendo quantas requisições são necessárias para que a aplicação caia, se ela cair.

O Projeto foi desenvolvido utilizando python e algumas bibliotecas python.

Para o controle de versões tanto do Python quanto das dependências utilizadas no projeto, é utilizado o [Poetry](https://python-poetry.org/) e o mesmo deve estar instalado na maquina para a execução do projeto, assim como o *Python* ao menos na versão *3.8* qualquer versão inferior será ignorada e não será possível inicializar e controlar as dependências pelo poetry.

Com o Poetry instalado, primeiramente devemos criar um ambiente virtual isso é possível através do seguinte comando no diretório do projeto:
```
poetry shell
```

Após a criação do nosso ambiente virtual, devemos instalar as dependências do projeto com o seguinte comando no diretório do projeto:
```
poetry install
```

Para a execução dos testes foi configurado o tox um testrunner que já está contemplado nas dependências do projeto.

Para executarmos todos os testes conseguimos a partir do seguinte comando no diretório do projeto:
```
tox
```
Após a execução dos testes são gerados os reports e estes são armazenados na raiz do projeto.

Os reports dos tests de stress serão 3 arquivos .csv com o prefixo stress_tests e o report dos testes de contratos será um arquivo html chamado scanapi-report.html

Para executarmos os testes de stress conseguimos a partir do seguinte comando no diretório do projeto:
```
tox -e stress
```

Para executarmos os testes de contrato conseguimos a partir do seguinte comando no diretório do projeto:
```
tox -e scanapi
```


# todo
* Adicionar suporte a algum sistema de CI, como Github Actions, GitlabCI, CircleCI, etc.
* Possibilida da execução dos testes em um ambiente docker.
