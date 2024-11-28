# evaluate_model.py
import os
from azure.ai.evaluation import AIProjectClient, EvaluationJob, EvaluationMetric

# Carregar as credenciais
api_key = os.getenv("AZURE_OPENAI_API_KEY")
endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")

# Configurar cliente de avaliação
client = AIProjectClient(endpoint=endpoint, credential=api_key)

def evaluate_model(prompt):
    job = EvaluationJob(
        model_id="gpt-4",
        prompt=prompt,
        metrics=[
            EvaluationMetric(name="relevance"),
            EvaluationMetric(name="fluency"),
            EvaluationMetric(name="accuracy")
        ]
    )
    result = client.create_evaluation_job(job)
    return result

if __name__ == "__main__":
    prompt = "Explique os benefícios da computação em nuvem."
    result = evaluate_model(prompt)
    
    print(f"ID do Job: {result.job_id}")
    print(f"Status: {result.status}")
    print(f"Métricas: {result.metrics}")