Uma escola realiza um levantamento anual para verificar não apenas qual o melhor aluno, mas também qual a melhor turma por média, e qual a média geral do colégio.

O registro de cada aluno da escola se dá no seguinte formato:

type Student = {
  id: string;
  name: string;
  grades: number[];
  class: string;
};

Esse ano, porém, ocorreu um erro no registro e alguns dados foram alterados, após uma investigação, os seguintes erros forram constatados:
- Alguns alunos estão duplicados no sistema,
- Alguns alunos encontram-se sem a turma a qual pertencem,
- Alguns alunos possuem nota(s) maior(es) do que a máxima (100 pontos).

Você é um profissional da área encarregado de fazer o melhor possível para levantar as estatísticas que a escola precisa, corrigindo e/ou ignorando os erros quando necessários.
- Os alunos duplicados devem ser excluídos na contagem,
- Os alunos sem turma, não devem contar para média de turma, mas podem contar para classificação unitária, e para média geral da escola,
- As notas maiores do que a pontuação máxima, devem ser ignoradas, porém as outras notas dos alunos devem ser consideradas,

As estatísticas que a escola precisa são:
- O aluno com a maior média da escola, se houver empate, deve retornar o aluno por ordem alfabética de nome,
- A turma de maior média da escola,
- A média geral da escola,