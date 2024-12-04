import openai
import os
from ragas import RAGASEvaluator

# Set up your Azure OpenAI API key and endpoint
openai.api_key = os.environ.get("AZURE_OPENAI_API_KEY"),
openai.api_base = os.environ.get("AZURE_OPENAI_ENDPOINT"),

# Initialize RAGAS evaluator
evaluator = RAGASEvaluator()

# Define your RAG pipeline
def rag_pipeline(query):
    response = openai.Completion.create(
        engine= os.environ.get("AZURE_OPENAI_DEPLOYMENT"),
        prompt=query,
        max_tokens=100
    )
    return response.choices.text.strip()

# Evaluate the RAG pipeline
query = "What is the capital of France?"
response = rag_pipeline(query)
evaluation = evaluator.evaluate(query, response)

print(f"Query: {query}")
print(f"Response: {response}")
print(f"Evaluation: {evaluation}")