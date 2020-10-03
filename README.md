# Analise de Algoritmo e Estrutura de Dados
Repositório com códigos e anotações da disciplina de Análise de Algoritmos e Estrutura de Dados do curso EACH-USP 2020

##Ordenação
O arquivo ordena.py  visa exemplicar, via código, uma possível implementação de ordenação.

O algoritmo usa como base a tecnica de divisão e conquiesta.

3 métodos de ordenação são implementados:
1 - mergesort_v1: Faz a ordenação dividindo o vetor em 2 partes;
2 - mergesort_v1: Faz a ordenação dividindo o vetor em 4 partes;

3 - selection_sort:  Faz a ordenação buscando o menos elemento no vetor e colocando na primeira posição;
esse ultima não utiliza a tecnica de divisão e conquista e foi implementado usando uma abordagem iterativa.

o metodo auxiliar intercala faz a permutação entra 2 partes do vetor ja ordenadas
ex:
parte1: [5, 6, 9, 11] | parte2: [4, 7, 12, 15]

o metodo intervala teria como resultado:
A[4, 5, 6, 7, 9, 11, 12, 15]

