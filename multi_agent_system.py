import os
from dotenv import load_dotenv
from langchain.agents import initialize_agent, AgentType, Tool
from langchain.prompts import PromptTemplate
from langchain.chat_models import AzureChatOpenAI
from langchain.llms import OpenAI
from langchain.agents import AgentExecutor
import logging

# Load environment variables from .env file
load_dotenv()

# Set logging level (optional, for better debugging)
logging.basicConfig(level=logging.INFO)

# Azure OpenAI API credentials
api_key = os.getenv('AZURE_OPENAI_API_KEY')
azure_endpoint = os.getenv('AZURE_OPENAI_ENDPOINT')
api_version = os.getenv("OPENAI_API_VERSION")

# Initialize the Azure OpenAI model using LangChain
llm = AzureChatOpenAI(
    openai_api_key=api_key,
    azure_endpoint=azure_endpoint,
    model="gpt-4",  # or any other model available in your Azure instance
    temperature=0.7,
    openai_api_version=api_version
)

# Define a tool for the agent (this can be customized per agent)
tools = [
    Tool(
        name="WebScraper",
        func=lambda query: f"Searching for: {query}",  # Placeholder functionality
        description="Use this tool to perform web searches."
    ),
    Tool(
        name="DatabaseQuery",
        func=lambda query: f"Querying the database for: {query}",  # Placeholder functionality
        description="Use this tool to query the database."
    )
]

# Define a simple prompt template
prompt_template = """
You are an intelligent agent. Use the tools and collaborate with other agents to solve problems.

Task: {task}
"""
prompt = PromptTemplate(input_variables=["task"], template=prompt_template)

# Initialize agents (each agent can use the same LLM but can act differently)
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

# Simple multi-agent interaction: agent 1 passes a task to agent 2
def run_multi_agent_system(task):
    logging.info(f"Task: {task}")

    # Agent 1 processes the task
    agent_1_response = agent_1.run(task)
    logging.info(f"Agent 1 response: {agent_1_response}")

    # Agent 2 processes the output of Agent 1
    agent_2_response = agent_2.run(agent_1_response)
    logging.info(f"Agent 2 response: {agent_2_response}")

    return agent_2_response

# Example usage of the multi-agent system
if __name__ == "__main__":
    task = "Find the latest news about AI technology."
    result = run_multi_agent_system(task)
    print(f"Final Result: {result}")
