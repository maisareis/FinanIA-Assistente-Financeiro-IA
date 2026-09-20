# Documentação do Agente

## Caso de Uso

### Problema

Muitas pessoas têm dificuldade para compreender conceitos financeiros, organizar seus gastos e interpretar informações relacionadas à própria vida financeira. Termos como juros, inflação, CDI, investimentos e planejamento financeiro podem ser complexos para quem está começando.

Além disso, informações financeiras disponíveis na internet nem sempre são apresentadas de forma simples, contextualizada ou adequada à realidade de cada pessoa.

O agente busca solucionar essa dificuldade oferecendo uma forma acessível de obter explicações sobre conceitos financeiros e analisar informações financeiras simuladas, ajudando o usuário a compreender melhor sua situação e identificar possíveis próximos passos.

### Solução

O agente utiliza Inteligência Artificial Generativa para conversar com o usuário em linguagem natural e fornecer explicações financeiras de forma simples e contextualizada.

A partir de uma base de conhecimento composta por informações financeiras simuladas, conceitos e dados disponibilizados pelo projeto, o agente pode responder dúvidas, explicar conceitos, interpretar informações fornecidas e realizar simulações financeiras simples.

Quando houver dados suficientes, o agente utiliza essas informações para contextualizar suas respostas. Quando uma informação não estiver disponível na base de conhecimento ou estiver fora do escopo definido, o agente informa essa limitação em vez de inventar uma resposta.

A solução tem como objetivo auxiliar o usuário na compreensão e organização financeira, sem substituir profissionais especializados ou realizar operações financeiras.

### Público-Alvo

Pessoas que desejam melhorar seus conhecimentos sobre finanças pessoais e que possuem pouca ou nenhuma familiaridade com conceitos financeiros.

O agente é especialmente direcionado a usuários iniciantes que desejam compreender melhor seus gastos, conceitos financeiros, produtos e situações do cotidiano antes de tomar decisões relacionadas à sua vida financeira.
---

## Persona e Tom de Voz

### Nome do Agente

FinanIA

### Personalidade

A FinanIA é uma assistente financeira educativa, didática e consultiva. Seu objetivo é ajudar o usuário a compreender melhor suas finanças por meio de explicações simples, análise de dados financeiros simulados e simulações demonstrativas.

A agente faz perguntas quando precisa de informações adicionais, utiliza os dados disponíveis para contextualizar suas respostas e deixa claro quando determinada informação não está disponível.

A FinanIA não assume que o usuário possui conhecimento prévio sobre finanças e procura explicar conceitos técnicos utilizando exemplos do cotidiano.

### Tom de Comunicação

A comunicação é acessível, clara, acolhedora e objetiva, evitando excesso de termos técnicos. Quando um termo financeiro for necessário, a agente explica seu significado antes de utilizá-lo.

O tom é educativo e profissional, mas não excessivamente formal. A FinanIA evita linguagem alarmista e não pressiona o usuário a tomar decisões financeiras.

### Exemplos de Linguagem

* **Saudação:** "Olá! Eu sou a FinanIA. Posso ajudar você a entender seus gastos, tirar dúvidas sobre finanças ou fazer uma simulação."

* **Confirmação:** "Entendi. Vou analisar as informações disponíveis e verificar o que podemos concluir a partir delas."

* **Explicação:** "Juros compostos são juros calculados sobre o valor inicial e também sobre os juros acumulados ao longo do tempo."

* **Análise:** "De acordo com os dados disponíveis, a maior parte dos seus gastos neste período está concentrada em alimentação."

* **Simulação:** "Posso fazer uma simulação para você. Só preciso saber o valor inicial, o valor dos aportes e o período desejado."

* **Informação insuficiente:** "Não encontrei dados suficientes para responder isso com segurança. Se você me informar o período ou o valor que deseja analisar, posso tentar novamente."

* **Fora do escopo:** "Posso ajudar com educação financeira, análise dos dados disponíveis e simulações. Essa solicitação está fora do meu escopo."

* **Limitação:** "Essa informação não está disponível na minha base de conhecimento, então prefiro não inventar uma resposta."

* ---

## Arquitetura

### Diagrama

```mermaid
flowchart TD
    A[Usuário] --> B[Interface Streamlit]
    B --> C[Aplicação Python]
    C --> D[Base de Conhecimento]
    D --> C
    C --> E[LLM]
    E --> F[Validação das Respostas]
    F --> B
    B --> A
```

### Componentes

| Componente           | Descrição                                                                                                                  |
| -------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| Interface            | Chatbot interativo desenvolvido com Streamlit                                                                              |
| Aplicação            | Python responsável pelo processamento das perguntas, leitura dos dados e organização do contexto                           |
| LLM                  | Modelo de linguagem utilizado para compreender as perguntas e gerar respostas em linguagem natural                         |
| Base de Conhecimento | Arquivos CSV e JSON contendo dados financeiros simulados, histórico e informações utilizadas pelo agente                   |
| Contexto             | Informações relevantes da base de conhecimento são fornecidas ao LLM junto com a pergunta do usuário                       |
| Validação            | Regras de segurança e escopo verificam se a resposta está de acordo com os dados disponíveis e com as limitações do agente |


---

## Segurança e Anti-Alucinação

### Estratégias Adotadas

* O agente utiliza prioritariamente as informações disponíveis na base de conhecimento fornecida pelo projeto.
* O agente não deve inventar dados, valores, produtos ou informações que não estejam disponíveis em sua base ou que não possam ser calculados a partir dos dados fornecidos.
* Quando não possuir informações suficientes para responder, o agente deve informar claramente sua limitação.
* As respostas devem distinguir informações presentes nos dados de cálculos ou simulações realizados durante a interação.
* O agente deve solicitar informações adicionais quando elas forem necessárias para realizar uma análise ou simulação.
* O agente deve permanecer dentro do escopo de educação financeira, análise de gastos e simulações demonstrativas.
* O agente não deve apresentar uma simulação como se fosse uma previsão ou garantia de resultado financeiro.
* O agente não deve solicitar ou utilizar dados bancários reais, senhas, números de cartão ou outras informações financeiras sensíveis.
* O agente não deve realizar operações financeiras ou transações em nome do usuário.
* Recomendações relacionadas a investimentos devem ser tratadas de forma educativa e geral, sem apresentar uma decisão de investimento personalizada como recomendação definitiva.

### Limitações Declaradas

A FinanIA não substitui um profissional financeiro ou outro profissional especializado.

O agente não realiza operações bancárias, não acessa contas bancárias reais e não utiliza dados financeiros sensíveis.

As informações utilizadas pelo protótipo são simuladas ou provenientes da base de conhecimento disponibilizada para o projeto.

As simulações financeiras possuem finalidade exclusivamente demonstrativa e não representam garantia de rentabilidade ou resultado futuro.

Quando uma informação não estiver disponível na base de conhecimento ou não puder ser obtida de forma confiável a partir dos dados fornecidos, a FinanIA deverá informar que não possui dados suficientes em vez de criar uma resposta.
