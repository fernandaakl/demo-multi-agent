# evaluate_model.py
import openai
import os
from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient

# Carregar as credenciais
openai.api_key = os.getenv("AZURE_OPENAI_API_KEY")
endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")

# Configurar cliente de análise de texto
text_analytics_client = TextAnalyticsClient(endpoint=endpoint, credential=AzureKeyCredential(openai.api_key))

def evaluate_model(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=100
    )
    return response.choices.text.strip()

def analyze_text(text):
    documents = [text]
    response = text_analytics_client.analyze_sentiment(documents=documents)
    return response.sentiment, response.confidence_scores

if __name__ == "__main__":
    prompt = "Explique os benefícios da computação em nuvem."
    result = evaluate_model(prompt)
    sentiment, confidence_scores = analyze_text(result)
    
    print(f"Resultado: {result}")
    print(f"Sentimento: {sentiment}")
    print(f"Confiança: {confidence_scores}")