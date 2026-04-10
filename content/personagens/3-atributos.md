---
title: "Atributos"
metaTitle: "Atributos"
metaDescription: "Personagens -> Atributos"
---

O valor de cada atributo determina se o personagem possui bônus ou penalidades associadas com várias ações no jogo. As tabelas a seguir listam os modificadores relacionados com cada atributo, com os efeitos descritos abaixo.

# Força (FOR)
Músculo e poder físico.
* **Corpo-a-corpo**: É aplicado a jogadas de ataque e de rolagens de dano com armas corpo-a-corpo.
* **Abrir Portas**: Chance de sucesso ao tentar forçar a abertura de uma porta pesada ou emperrada.

<!--
  Para editar esta tabela, copie o bloco <table>...</table> inteiro e cole em
  https://www.tablesgenerator.com/html_tables (File -> Paste table data...).
  Edite visualmente (para mesclar celulas: selecione-as e use o botao "merge"),
  depois copie o resultado de volta aqui. Mantenha a tabela sem linhas em branco
  internas — MDX interpretaria uma linha vazia como quebra de bloco.
-->
<table>
<thead>
<tr>
<th colspan="3">Modificadores de Força</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>FOR</strong></td>
<td><strong>Corpo-a-corpo</strong></td>
<td><strong>Abrir Portas</strong></td>
</tr>
<tr>
<td>3</td>
<td>-3</td>
<td>1 em 6</td>
</tr>
<tr>
<td>4-5</td>
<td>-2</td>
<td>1 em 6</td>
</tr>
<tr>
<td>6-8</td>
<td>-1</td>
<td>1 em 6</td>
</tr>
<tr>
<td>9-12</td>
<td>Nenhum</td>
<td>2 em 6</td>
</tr>
<tr>
<td>13-15</td>
<td>+1</td>
<td>3 em 6</td>
</tr>
<tr>
<td>16-17</td>
<td>+2</td>
<td>4 em 6</td>
</tr>
<tr>
<td>18</td>
<td>+3</td>
<td>5 em 6</td>
</tr>
</tbody>
</table>

# Inteligência (INT)
Aprendizado, memória e raciocínio. 
* **Línguas conhecidas**: Determina o número de línguas que o personagem sabe falar.
* **Alfabetização**: Indica a capacidade do personagem ler e escrever em suas línguas nativas. 

<!--
  Para editar esta tabela, copie o bloco <table>...</table> inteiro e cole em
  https://www.tablesgenerator.com/html_tables (File -> Paste table data...).
  Edite visualmente (para mesclar celulas: selecione-as e use o botao "merge"),
  depois copie o resultado de volta aqui. Mantenha a tabela sem linhas em branco
  internas — MDX interpretaria uma linha vazia como quebra de bloco.
-->
<table>
<thead>
<tr>
<th colspan="3">Modificadores de Inteligência</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>INT</strong></td>
<td><strong>Línguas Conhecidas</strong></td>
<td><strong>Alfabetização</strong></td>
</tr>
<tr>
<td>3</td>
<td>Nativa (falada com dificuldade)</td>
<td>Analfabeto</td>
</tr>
<tr>
<td>4-5</td>
<td>Nativa</td>
<td>Analfabeto</td>
</tr>
<tr>
<td>6-8</td>
<td>Nativa</td>
<td>Semi-analfabeto</td>
</tr>
<tr>
<td>9-12</td>
<td>Nativa</td>
<td>Alfabetizado</td>
</tr>
<tr>
<td>13-15</td>
<td>Nativa + 1 adicional</td>
<td>Alfabetizado</td>
</tr>
<tr>
<td>16-17</td>
<td>Nativa + 2 adicionais</td>
<td>Alfabetizado</td>
</tr>
<tr>
<td>18</td>
<td>Nativa + 3 adicionais</td>
<td>Alfabetizado</td>
</tr>
</tbody>
</table>

# Sabedoria (SAB)
Força de vontade, bom senso, percepção e intuição. 

* **Resistência à Magia**: É aplicado em jogadas de resistência contra efeitos mágicos. Isto normalmente não se aplica contra ataques de sopro, mas pode ser aplicado a qualquer outro tipo de teste de resistência. 

<!--
  Para editar esta tabela, copie o bloco <table>...</table> inteiro e cole em
  https://www.tablesgenerator.com/html_tables (File -> Paste table data...).
  Edite visualmente (para mesclar celulas: selecione-as e use o botao "merge"),
  depois copie o resultado de volta aqui. Mantenha a tabela sem linhas em branco
  internas — MDX interpretaria uma linha vazia como quebra de bloco.
-->
<table>
<thead>
<tr>
<th colspan="2">Modificadores de Sabedoria</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>SAB</strong></td>
<td><strong>Resistência à Magia</strong></td>
</tr>
<tr>
<td>3</td>
<td>-3</td>
</tr>
<tr>
<td>4-5</td>
<td>-2</td>
</tr>
<tr>
<td>6-8</td>
<td>-1</td>
</tr>
<tr>
<td>9-12</td>
<td>Nenhum</td>
</tr>
<tr>
<td>13-15</td>
<td>+1</td>
</tr>
<tr>
<td>16-17</td>
<td>+2</td>
</tr>
<tr>
<td>18</td>
<td>+3</td>
</tr>
</tbody>
</table>

# Destreza (DES)
Agilidade, reflexos, velocidade e equilíbrio.
* **CA**: Modifica o valor de CA (um bônus diminui a CA, uma penalidade aumenta)
* **Mísseis**: Aplicado a jogadas de ataque (mas não jogadas de dano) com armas à distância.
* **Iniciativa**: Modifica o valor da iniciativa do personagem, se a regra opcional de iniciativa individual está sendo usada (veja capítulo de Combate)

<!--
  Para editar esta tabela, copie o bloco <table>...</table> inteiro e cole em
  https://www.tablesgenerator.com/html_tables (File -> Paste table data...).
  Edite visualmente (para mesclar celulas: selecione-as e use o botao "merge"),
  depois copie o resultado de volta aqui. Mantenha a tabela sem linhas em branco
  internas — MDX interpretaria uma linha vazia como quebra de bloco.
-->
<table>
<thead>
<tr>
<th colspan="4">Modificadores de Destreza</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>DES</strong></td>
<td><strong>CA</strong></td>
<td><strong>Mísseis</strong></td>
<td><strong>Iniciativa</strong></td>
</tr>
<tr>
<td>3</td>
<td>-3</td>
<td>-3</td>
<td>-2</td>
</tr>
<tr>
<td>4-5</td>
<td>-2</td>
<td>-2</td>
<td>-1</td>
</tr>
<tr>
<td>6-8</td>
<td>-1</td>
<td>-1</td>
<td>-1</td>
</tr>
<tr>
<td>9-12</td>
<td>Nenhum</td>
<td>Nenhum</td>
<td>Nenhum</td>
</tr>
<tr>
<td>13-15</td>
<td>+1</td>
<td>+1</td>
<td>+1</td>
</tr>
<tr>
<td>16-17</td>
<td>+2</td>
<td>+2</td>
<td>+1</td>
</tr>
<tr>
<td>18</td>
<td>+3</td>
<td>+3</td>
<td>+2</td>
</tr>
</tbody>
</table>

# Constituição (CON)
Saúde, resistência física e vigor.
* **Pontos de vida**: É aplicado quando for rolar os pontos de vida de seu personagem (no 1º nível e posteriormente a cada nível ganho). Um personagem sempre ganha pelo menos 1 ponto de vida por Dado de Vida, independente do modificador de CON.

<!--
  Para editar esta tabela, copie o bloco <table>...</table> inteiro e cole em
  https://www.tablesgenerator.com/html_tables (File -> Paste table data...).
  Edite visualmente (para mesclar celulas: selecione-as e use o botao "merge"),
  depois copie o resultado de volta aqui. Mantenha a tabela sem linhas em branco
  internas — MDX interpretaria uma linha vazia como quebra de bloco.
-->
<table>
<thead>
<tr>
<th colspan="2">Modificadores de Constituição</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>CONS</strong></td>
<td><strong>Pontos de vida</strong></td>
</tr>
<tr>
<td>3</td>
<td>-3</td>
</tr>
<tr>
<td>4-5</td>
<td>-2</td>
</tr>
<tr>
<td>6-8</td>
<td>-1</td>
</tr>
<tr>
<td>9-12</td>
<td>Nenhum</td>
</tr>
<tr>
<td>13-15</td>
<td>+1</td>
</tr>
<tr>
<td>16-17</td>
<td>+2</td>
</tr>
<tr>
<td>18</td>
<td>+3</td>
</tr>
</tbody>
</table>

# Carisma (CAR)
Força da personalidade, capacidade de persuasão, magnetismo pessoal, atratividade física e capacidade de liderar. 
* **Ajuste de Reação**: Se aplica quando for contratar seguidores e quando interagir com monstros. 
* **Nº Máximo de seguidores**: Determina o número máximo de seguidores que o seu personagem pode possuir ao mesmo tempo.
* **Lealdade dos Seguidores**: Determina a lealdade dos seguidores deste personagem.

<!--
  Para editar esta tabela, copie o bloco <table>...</table> inteiro e cole em
  https://www.tablesgenerator.com/html_tables (File -> Paste table data...).
  Edite visualmente (para mesclar celulas: selecione-as e use o botao "merge"),
  depois copie o resultado de volta aqui. Mantenha a tabela sem linhas em branco
  internas — MDX interpretaria uma linha vazia como quebra de bloco.
-->
<table>
<thead>
<tr>
<th colspan="4">Modificadores de Carisma</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>CAR</strong></td>
<td><strong>Ajuste de Reação</strong></td>
<td><strong>Nº Máximo de</strong> <strong>seguidores</strong></td>
<td><strong>Lealdade dos</strong> <strong>Seguidores</strong></td>
</tr>
<tr>
<td>3</td>
<td>-2</td>
<td>1</td>
<td>4</td>
</tr>
<tr>
<td>4-5</td>
<td>-1</td>
<td>2</td>
<td>5</td>
</tr>
<tr>
<td>6-8</td>
<td>-1</td>
<td>3</td>
<td>6</td>
</tr>
<tr>
<td>9-12</td>
<td>Nenhum</td>
<td>4</td>
<td>7</td>
</tr>
<tr>
<td>13-15</td>
<td>+1</td>
<td>5</td>
<td>8</td>
</tr>
<tr>
<td>16-17</td>
<td>+1</td>
<td>6</td>
<td>9</td>
</tr>
<tr>
<td>18</td>
<td>+2</td>
<td>7</td>
<td>10</td>
</tr>
</tbody>
</table>

# Requisito Primário
Cada classe de personagem possui um ou mais requisitos primários - atributos que possuem uma importância especial ao funcionamento da classe. O valor de atributo que o personagem possui em seu requisito primário afeta quão rapidamente ele ganha pontos de experiência. 

Personagens com apenas um requisito primário utilizam a tabela a seguir. Os modificadores para classes com mais de um atributo como requisito primário estão listados na descrição da classe.
* **Modificador de XP**: É aplicado a todos os pontos de experiência ganhos pelo personagem, a menos que seja dito o contrário na descrição da classe. 

<!--
  Para editar esta tabela, copie o bloco <table>...</table> inteiro e cole em
  https://www.tablesgenerator.com/html_tables (File -> Paste table data...).
  Edite visualmente (para mesclar celulas: selecione-as e use o botao "merge"),
  depois copie o resultado de volta aqui. Mantenha a tabela sem linhas em branco
  internas — MDX interpretaria uma linha vazia como quebra de bloco.
-->
<table>
<thead>
<tr>
<th colspan="2">Modificadores de Requisito Primário</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Requisito Primário</strong></td>
<td><strong>Modificador de XP</strong></td>
</tr>
<tr>
<td>3-5</td>
<td>-20%</td>
</tr>
<tr>
<td>6-8</td>
<td>-10%</td>
</tr>
<tr>
<td>9-12</td>
<td>Nenhum</td>
</tr>
<tr>
<td>13-15</td>
<td>+5%</td>
</tr>
<tr>
<td>16-18</td>
<td>+10%</td>
</tr>
</tbody>
</table>