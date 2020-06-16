# Desafio: descubra as melhores notas de matemática do ENEM 2016

Esta é a minha solução proposta para o desafio da Codenation, para entrar no AceleraDev de Data Science (turma 09/06/2020 - 18/08/2020).

Obtive um score de 92,56%.

## Definição do problema

Você deverá criar um modelo para prever a nota da prova de matemática de quem participou do ENEM 2016.

O contexto do desafio gira em torno dos resultados do ENEM 2016 (disponíveis no arquivo [train.csv](train.csv)). Este arquivo, e apenas ele, deve ser utilizado para todos os desafios. Qualquer dúvida a respeito das colunas, consulte o [Dicionário dos Microdados do Enem 2016](Dicionario_Microdados_Enem_2016.xlsx).

Muitas universidades brasileiras utilizam o ENEM para selecionar seus futuros alunos e alunas. Isto é feito com uma média ponderada das notas das provas de matemática, ciências da natureza, linguagens e códigos, ciências humanas e redação, com os pesos abaixo:

- matemática: 3
- ciências da natureza: 2
- linguagens e códigos: 1.5
- ciências humanas: 1
- redação: 3

No arquivo [test.csv](test.csv) crie um modelo para prever nota da prova de matemática (coluna ```NU_NOTA_MT```) de quem participou do ENEM 2016. Salve sua resposta em um arquivo chamado [answer.csv](answer.csv) com duas colunas: ```NU_INSCRICAO```e ```NU_NOTA_MT```.

Qualquer dúvida a respeito das colunas, consulte o Dicionário dos Microdados do Enem 2016.