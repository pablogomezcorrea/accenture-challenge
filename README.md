# Desafio Accenture

### Orientações

Esse teste prático busca avaliar a capacidade do candidato em construir um agente de IA que analisa dados de um arquivo CSV e responde a perguntas sobre os dados.
Caso você não esteja familiarizado com alguma tecnologia ou conceito que pedirmos, sinta-se livre para pesquisar e aprender o que precisar para entregar o desafio da melhor maneira possível. Isso fará parte da avaliação.
Utilize Python e bibliotecas que julgar necessárias para a construção da solução.
Você PODE usar IA para ajudar a implementar a solução.
O código deve ser publicado em um repositório público do GitHub com permissão de Clone.
O projeto deve conter um arquivo README.md com as tecnologias que foram utilizadas e instruções de build e teste.
O projeto deve conter um arquivo Dockerfile para permitir executar o código dentro de um ambiente controlado.
Over-engineering é bem-vindo, especialmente para níveis Sênior e Consultor. Explore diferentes desafios técnicos e arquiteturais que poderiam surgir.
Prepare-se para discutir suas escolhas técnicas e arquiteturais durante a entrevista.
 

### Condições de Entrega

Você possui até 13/08 as 18h para realizar a entrega do código.
Caso não consiga completar a solução, você pode entregar até onde conseguiu chegar. A quantidade de 
funcionalidades implementadas será uma variável de avaliação, mas não é eliminatório caso não consiga concluir o desafio.
O código precisa ter pelo menos a estrutura mínima, sendo possível acessar a aplicação e consultar as informações 
de empresas e fornecedores.
O processo irá levar em média, uns 20 minutos

# Tecnologias utilizadas
## Aplicação
* Python
* LangChain
* LLM (llama3.1)
* Embeddings
* TextSplitter
* Ollama
* Streamlit
## Infraestrutura
* Docker
* Docker Compose

# Pacotes
<code>pip install sentence-transformers</code>

# Docker
Para o deploy da aplicação, foi criado um docker-compose.yaml que irá fazer 
todo o processo automaticamente. O comando à ser executado segue abaixo, ele deve ser
executado na raiz da aplicação

<code>
docker compose up -d build
</code>

Após finalizar o processo de deploy, será possível visualizar dois containers

![img.png](img.png