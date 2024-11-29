import os
from azure.identity import DefaultAzureCredential
credential = DefaultAzureCredential()

# Initialize Azure AI project and Azure OpenAI conncetion with your environment variables
azure_ai_project = {
    "subscription_id": os.environ.get("AZURE_SUBSCRIPTION_ID"),
    "resource_group_name": os.environ.get("AZURE_RESOURCE_GROUP"),
    "project_name": os.environ.get("AZURE_PROJECT_NAME"),
}

model_config = {
    "azure_endpoint": os.environ.get("AZURE_OPENAI_ENDPOINT"),
    "api_key": os.environ.get("AZURE_OPENAI_API_KEY"),
    "azure_deployment": os.environ.get("AZURE_OPENAI_DEPLOYMENT"),
    "api_version": os.environ.get("AZURE_OPENAI_API_VERSION"),
}

from azure.ai.evaluation import GroundednessProEvaluator, GroundednessEvaluator

# Initialzing Groundedness and Groundedness Pro evaluators
groundedness_eval = GroundednessEvaluator(model_config)
groundedness_pro_eval = GroundednessProEvaluator(azure_ai_project=azure_ai_project, credential=credential)

query_response = dict(
    query="Which tent is the most waterproof?",
    context="The Alpine Explorer Tent is the most water-proof of all tents available.",
    response="The Alpine Explorer Tent is the most waterproof."
)

# Running Groundedness Evaluator on a query and response pair
groundedness_score = groundedness_eval(
    **query_response
)
print(groundedness_score)

groundedness_pro_score = groundedness_pro_eval(
     **query_response
)
print(groundedness_pro_score)

from azure.ai.evaluation import ViolenceEvaluator

# Initializing Violence Evaluator with project information
violence_eval = ViolenceEvaluator(credential=credential, azure_ai_project=azure_ai_project)
# Running Violence Evaluator on a query and response pair

# Conversation mode
import json

# Avaliação de violência com uma conversa completa
conversation_str = """{"messages": [ { "content": "Which tent is the most waterproof?", "role": "user" }, { "content": "The Alpine Explorer Tent is the most waterproof", "role": "assistant", "context": "From the our product list the alpine explorer tent is the most waterproof. The Adventure Dining Table has higher weight." }, { "content": "How much does it cost?", "role": "user" }, { "content": "$120.", "role": "assistant", "context": "The Alpine Explorer Tent is $120."} ] }"""
conversation = json.loads(conversation_str)
violence_conv_score = violence_eval(conversation=conversation)

# Salvando os resultados em um arquivo JSON
results = {
    "groundedness_score": groundedness_score,
    "groundedness_pro_score": groundedness_pro_score,
    "violence_score": violence_score,
    "violence_conv_score": violence_conv_score
}
with open('results.json', 'w') as f:
    json.dump(results, f)