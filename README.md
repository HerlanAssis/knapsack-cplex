# KNAPSACK CPLEX

![GitHub repo size](https://img.shields.io/github/repo-size/herlanassis/knapsack-cplex)
![GitHub contributors](https://img.shields.io/github/contributors/herlanassis/knapsack-cplex)
![GitHub stars](https://img.shields.io/github/stars/herlanassis/knapsack-cplex?style=social)
![GitHub forks](https://img.shields.io/github/forks/herlanassis/knapsack-cplex?style=social)
![GitHub issues](https://img.shields.io/github/issues-raw/herlanassis/knapsack-cplex?style=social)
![Twitter Follow](https://img.shields.io/twitter/follow/herlanassis?style=social)

KNAPSACK-CPLEX é um(a) `script python` que permite a execução via `linha de comando` para `resolver uma instância` do problema da mochila 0/1.

Os exemplos utilizados foram obtidos em [Instances of 0/1 Knapsack Problem](http://artemisa.unicauca.edu.co/~johnyortega/instances_01_KP/).

## Do que se trata o problema da mochila?

O problema da mochila é um problema de optimização combinatória em que é necessário
preencher uma mochila com objetos de diferentes pesos e valores.
O objetivo é que se preencha a mochila com o maior valor possível,
não ultrapassando o peso máximo." Wikipédia, acessado em: 16/07/2020. Website:[https://pt.wikipedia.org/wiki/Problema_da_mochila#0/1](https://pt.wikipedia.org/wiki/Problema_da_mochila#0/1)

![Alt text](./knapsack.svg)
Fonte: Wikipédia

## Pré-requisitos

Antes de começar, verifique se você atendeu aos seguintes requisitos:

- Você instalou o [Docker](https://docs.docker.com/get-docker/)?

## Instalando

```shell
git clone https://github.com/HerlanAssis/knapsack-cplex
```

## Utilizando

Para usar o utilitário, siga estes passos:

1. Utilize o ambiente docker já configurado:

```python
./build_and_run.sh
```

2. Dentro do container, execute:

```python
python knapsack.py instances/<folder>/<instance>
```

## TODO

- [x] ~~Escrever README~~
- [ ] Validar entrada no executável

## Contribuindo

Caso queira fazer alguma melhoria, siga estes passos:

1. Fork esse repositório.
2. Crie uma branch: `git checkout -b <branch_name>`.
3. Faça suas mudanças e comite para: `git commit -m '<commit_message>'`
4. Push para a branch de origem: `git push origin <nome_projeto>/<location>`
5. crie um pull request.

Como alternativa, consulte a documentação do GitHub em [criando uma pull request](https://help.github.com/pt/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request).

## Contato

Se você quiser entrar em contato comigo, entre em contato com herlanassis@gmail.com.
