import os
from dotenv import load_dotenv
from openai import OpenAI

# 1. Carga GROQ_API_KEY desde el archivo .env
load_dotenv()

# 2. Inicializa el cliente apuntando a los servidores gratuitos de Groq
client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=os.environ.get("GROQ_API_KEY"),
)

# 3. Envía la petición al modelo Llama 3.3 70B
respuesta = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {"role": "system", "content": "Eres un profesor de ingeniería informática conciso y técnico."},
        {"role": "user", "content": "Explica en tres líneas qué es el mecanismo de atención en un Transformer."}
    ]
)

# 4. Muestra la respuesta y el gasto de tokens
print("--- RESPUESTA DEL MODELO ---")
print(respuesta.choices[0].message.content)
print("\n--- MÉTRICAS DE CONSUMO ---")
print(f"Tokens de entrada: {respuesta.usage.prompt_tokens}")
print(f"Tokens de salida: {respuesta.usage.completion_tokens}")
print(f"Tokens totales: {respuesta.usage.total_tokens}")
print("Coste: 0.00 € (Capa gratuita)")