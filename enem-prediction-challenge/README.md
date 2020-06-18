# Desafio: descubra as melhores notas de matemática do ENEM 2016

A minha solução proposta para o desafio da Codenation, para entrar no AceleraDev de Data Science (turma 09/06/2020 - 18/08/2020) está no arquivo [enem-challenge.ipynb](enem-challenge.ipynb).

Obtive um score de 92,56%.

## Detalhes

Você deverá criar um modelo para prever a nota da prova de matemática de quem participou do ENEM 2016.

O contexto do desafio gira em torno dos resultados do ENEM 2016 (disponíveis no arquivo [train.csv](train.csv)). Este arquivo, e apenas ele, deve ser utilizado para todos os desafios. Qualquer dúvida a respeito das colunas, consulte o [Dicionário dos Microdados do Enem 2016](Dicionario_Microdados_Enem_2016.xlsx).

Muitas universidades brasileiras utilizam o ENEM para selecionar seus futuros alunos e alunas. Isto é feito com uma média ponderada das notas das provas de matemática, ciências da natureza, linguagens e códigos, ciências humanas e redação, com os pesos abaixo:

- matemática: 3
- ciências da natureza: 2
- linguagens e códigos: 1.5
- ciências humanas: 1
- redação: 3

No arquivo [test.csv](test.csv) crie um modelo para prever nota da prova de matemática (coluna ```NU_NOTA_MT```) de quem participou do ENEM 2016. Salve sua resposta em um arquivo chamado [answer.csv](answer.csv) com duas colunas: ```NU_INSCRICAO```e ```NU_NOTA_MT```.

## Conteúdos

Sugestões de conteúdos para completar o desafio:

- [Comprehensive data exploration with Python](https://www.kaggle.com/pmarcelino/comprehensive-data-exploration-with-python)

- [Modern Pandas (Part 1)](https://web.archive.org/web/20200618002717/https://tomaugspurger.github.io/modern-1-intro.html)

- [Modern Pandas (Part 2: Method Chaining)](https://web.archive.org/web/20200506133120/https://tomaugspurger.github.io/method-chaining)

- [Modern Panadas (Part 3): Indexes](https://web.archive.org/web/20200618003003/https://tomaugspurger.github.io/modern-3-indexes)

- [Modern Pandas (Part 4): Performance](https://web.archive.org/web/20200618003117/https://tomaugspurger.github.io/modern-4-performance)

- [Modern Pandas (Part 5): Tidy Data](https://web.archive.org/web/20200618003204/https://tomaugspurger.github.io/modern-5-tidy)

- [An introduction to machine learning with scikit-learn](https://web.archive.org/web/20200618003301/https://scikit-learn.org/stable/tutorial/basic/tutorial.html)

- [Introduction to Linear Regression](https://web.archive.org/web/20200618003435/http://onlinestatbook.com/2/regression/intro.html)

- [Machine Learning - Coursera](https://www.coursera.org/learn/machine-learning)

- [How to run Linear regression in Python scikit-Learn](https://web.archive.org/web/20200618003715/https://bigdata-madesimple.com/how-to-run-linear-regression-in-python-scikit-learn/)