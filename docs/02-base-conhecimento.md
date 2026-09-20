# Base de Conhecimento

## Objetivo

A base de conhecimento da FinanIA reúne informações financeiras simuladas utilizadas para contextualizar as respostas do agente.

Os dados foram estruturados para permitir consultas sobre perfil financeiro, transações, produtos financeiros e histórico de atendimentos.

A base possui finalidade exclusivamente educacional e demonstrativa. Os dados não representam informações financeiras reais de clientes nem devem ser interpretados como dados atuais do mercado.

## Estrutura da Base

A base de conhecimento está organizada nos seguintes arquivos:

| Arquivo                     | Descrição                                                              |
| --------------------------- | ---------------------------------------------------------------------- |
| `perfil_usuario.json`       | Informações fictícias sobre o perfil financeiro e objetivos do usuário |
| `transacoes.csv`            | Registro de receitas e despesas simuladas                              |
| `produtos_financeiros.json` | Catálogo de produtos financeiros fictícios para fins educacionais      |
| `historico_atendimento.csv` | Histórico simulado de interações anteriores                            |

## Perfil do Usuário

O arquivo `perfil_usuario.json` contém informações como:

* nome;
* idade;
* profissão;
* renda mensal;
* perfil de investidor;
* objetivo financeiro principal;
* patrimônio;
* reserva de emergência;
* metas financeiras;
* prazo das metas.

Essas informações podem ser utilizadas para contextualizar respostas, desde que estejam disponíveis na base de conhecimento.

A FinanIA não deve utilizar essas informações para determinar automaticamente uma decisão de investimento. O perfil serve principalmente para contextualização e educação financeira.

## Transações

O arquivo `transacoes.csv` contém registros simulados de movimentações financeiras.

Os principais campos são:

* `data`;
* `descricao`;
* `categoria`;
* `valor`;
* `tipo`.

Os registros podem ser utilizados para realizar análises como:

* total de receitas;
* total de despesas;
* saldo do período;
* despesas por categoria;
* identificação das categorias com maior volume de gastos;
* comparação entre receitas e despesas;
* identificação de padrões simples de consumo.

As análises devem considerar somente os dados disponíveis no arquivo.

## Produtos Financeiros

O arquivo `produtos_financeiros.json` contém informações simuladas sobre diferentes produtos financeiros.

Entre os dados armazenados estão:

* nome do produto;
* categoria;
* nível de risco;
* rentabilidade informada;
* aporte mínimo;
* público indicado no conjunto de dados.

Essas informações têm finalidade didática. Valores de rentabilidade presentes nos dados são exemplos simulados e não representam necessariamente condições atuais de mercado.

A FinanIA pode explicar as características dos produtos e comparar suas informações de forma educativa, mas não deve transformar os dados em uma recomendação definitiva de investimento.

## Histórico de Atendimento

O arquivo `historico_atendimento.csv` registra interações simuladas anteriores.

Os dados incluem:

* data;
* canal;
* tema;
* resumo do atendimento;
* situação da solicitação.

O histórico pode ser utilizado para manter contexto durante uma conversa ou identificar assuntos anteriormente abordados.

Informações que estejam fora do escopo da FinanIA não devem ser utilizadas para ampliar artificialmente a atuação do agente.

## Uso da Base pelo Agente

Durante uma interação, a aplicação poderá consultar os arquivos da base de conhecimento para encontrar informações relevantes para a pergunta do usuário.

O fluxo esperado é:

1. O usuário envia uma pergunta.
2. A aplicação identifica o tipo de informação necessária.
3. A base de conhecimento é consultada.
4. Os dados relevantes são organizados como contexto.
5. O contexto é enviado ao modelo de linguagem junto com a pergunta.
6. O modelo gera uma resposta utilizando as informações disponíveis.
7. Regras de segurança e escopo são aplicadas antes da resposta ser apresentada ao usuário.

## Tratamento de Dados Ausentes

Quando uma informação solicitada não estiver disponível na base de conhecimento, a FinanIA deve informar essa limitação.

O agente não deve criar valores, transações, características de produtos ou informações sobre o usuário que não estejam presentes nos dados.

Quando necessário, a FinanIA poderá solicitar informações adicionais ao usuário para realizar uma análise ou simulação.

## Limitações

A base de conhecimento possui dados simulados e limitados ao contexto definido para o projeto.

Ela não representa:

* contas bancárias reais;
* dados financeiros reais de clientes;
* cotações ou taxas de mercado em tempo real;
* recomendações profissionais de investimento;
* operações bancárias;
* informações financeiras completas de uma pessoa real.

As respostas da FinanIA devem respeitar essas limitações e deixar claro quando uma informação não puder ser obtida a partir da base disponível.
