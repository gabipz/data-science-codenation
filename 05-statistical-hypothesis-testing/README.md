# Funções de probabilidade

Neste desafio vamos praticar sobre testes de hipóteses, um dos conceitos centrais
da inferência estatística e de toda pesquisa que utiliza estatística como suporte.

## Objetivo

O objetivo deste desafio é explorar algumas funções de testes de hipóteses disponíveis
em pacotes como o SciPy, aprendendo a interpretar seus resultados, ser crítico sobre
seus usos e entender um pouco sobre seus funcionamentos.

Para isso, utilizaremos  o _data set_ [2016 Olympics in Rio de Janeiro](https://www.kaggle.com/rio2016/olympic-games/)
que consiste de 11 variáveis a respeito de 11538 atletas que participaram das
Olimpíadas de 2016 no Rio de Janeiro.

## Tópicos

Neste desafios nós vamos explorar:

* Probabilidade
* Estatística
* Testes de hipóteses
* Testes A/B

## Conteúdos

- [Statistical hypothesis testing - Wikipedia](https://en.wikipedia.org/wiki/Statistical_hypothesis_testing)

- [A Gentle Introduction to Normality Tests in Python](https://machinelearningmastery.com/a-gentle-introduction-to-normality-tests-in-python/)

- [T-test using Python and Numpy](https://towardsdatascience.com/inferential-statistics-series-t-test-using-numpy-2718f8f9bf2f)

- [Statistical functions (scipy.stats)](https://docs.scipy.org/doc/scipy/reference/stats.html#statistical-tests)


## Requisitos

Você precisará de Python 3 e pip. É altamente recomendado utilizar ambientes virtuais
com o virtualenv e o arquivo `requirements.txt` para instalar os pacotes dependências
do desafio:

```bash
$ pip3 install virtualenv
$ virtualenv venv -p python3
$ source venv/bin/activate
$ pip install -r requirements.txt
```

Windows

```bash
> pip3 install virtualenv
> virtualenv ..\venv -p python3
> ..\venv\Scripts\activate
> pip install -r requirements.txt
```

Quando finalizado, você pode desativar o ambiente virtual do virtualenv com:

```bash
$ deactivate
```

