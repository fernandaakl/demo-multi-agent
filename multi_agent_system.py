import os
from dotenv import load_dotenv
from langchain.agents import initialize_agent, AgentType, Tool
from langchain.prompts import PromptTemplate
from langchain.chat_models import AzureChatOpenAI
import logging

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Definir nível de logging (opcional, para melhor depuração)
logging.basicConfig(level=logging.INFO)

# Credenciais da API Azure OpenAI
api_key = os.getenv('AZURE_OPENAI_API_KEY')
azure_endpoint = os.getenv('AZURE_OPENAI_ENDPOINT')
api_version = os.getenv("OPENAI_API_VERSION")

# Inicializar o modelo Azure OpenAI usando LangChain
llm = AzureChatOpenAI(
    openai_api_key=api_key,
    azure_endpoint=azure_endpoint,
    model="gpt-4",  # ou qualquer outro modelo disponível na sua instância Azure
    temperature=0.7,
    openai_api_version=api_version
)

# Definir uma ferramenta para o agente (isso pode ser personalizado por agente)
tools = [
    Tool(
        name="WebScraper",
        func=lambda query: f"Procurando por: {query}",  # Funcionalidade de placeholder
        description="Use esta ferramenta para realizar buscas na web."
    ),
    Tool(
        name="DatabaseQuery",
        func=lambda query: f"Consultando o banco de dados por: {query}",  # Funcionalidade de placeholder
        description="Use esta ferramenta para consultar o banco de dados."
    )
]

# Definir um modelo de prompt simples
prompt_template = """
Você é um agente inteligente. Use as ferramentas e colabore com outros agentes para resolver problemas.

Tarefa: {task}
"""
prompt = PromptTemplate(input_variables=["task"], template=prompt_template)

# Função para inicializar agentes
def initialize_agents():
    agent_1 = initialize_agent(
        tools=tools, 
        llm=llm,
        agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True
    )

    agent_2 = initialize_agent(
        tools=tools,
        llm=llm,
        agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True
    )

    agent_3 = initialize_agent(
        tools=tools,
        llm=llm,
        agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True
    )
    return agent_1, agent_2, agent_3

# Inicializar agentes
agent_1, agent_2, agent_3 = initialize_agents()

# Interação de multi-agente: agente 1 faz uma pergunta ao agente 2 e ao agente 3
def run_multi_agent_system(task):
    logging.info(f"Tarefa: {task}")

    # Agente 1 processa a tarefa
    agent_1_response = agent_1.run(task)
    logging.info(f"Resposta do Agente 1: {agent_1_response}")

    # Agente 1 faz uma pergunta ao Agente 2
    agent_2_response = agent_2.run(agent_1_response)
    logging.info(f"Resposta do Agente 2: {agent_2_response}")

    # Agente 1 faz uma pergunta ao Agente 3
    agent_3_response = agent_3.run(agent_2_response)
    logging.info(f"Resposta do Agente 3: {agent_3_response}")

    # Combinar as respostas dos três agentes com mais inteligência
    combined_response = (
        f"Agente 1 analisou a tarefa e respondeu: {agent_1_response}\n"
        f"Agente 2 revisou a resposta do Agente 1 e adicionou: {agent_2_response}\n"
        f"Agente 3 revisou a resposta do Agente 2 e adicionou: {agent_3_response}\n"
        f"Conclusão: A colaboração entre os agentes resultou em uma solução mais robusta e detalhada."
    )
    return combined_response

# Função principal para interação com o usuário
def main():
    print("Olá! Eu sou seu agente inteligente. Como posso ajudar você hoje?")
    while True:
        user_input = input("Você: ")
        if user_input.lower() in ['sair', 'exit', 'quit']:
            print("Agente: Até logo! Tenha um ótimo dia!")
            break
        task = user_input
        try:
            result = run_multi_agent_system(task)
            print(f"Agente: {result}")
        except ValueError as e:
            print(f"Erro: {e}")
            print("Tentando novamente...")
            result = run_multi_agent_system(task)
            print(f"Agente: {result}")

# Exemplo de uso do sistema multi-agente
if __name__ == "__main__":
    main()