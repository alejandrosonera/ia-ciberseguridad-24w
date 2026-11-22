# Notas Sesión 1 - IA y Automatización

- **ML tradicional vs. LLM:** El Machine Learning tradicional aprende patrones en datos específicos para resolver una tarea concreta, mientras que un LLM usa arquitectura Transformer entrenada con texto masivo para predecir estadísticamente el siguiente token.
- **Tokens y API stateless:** Los tokens son fragmentos de palabras que usa el modelo para leer y generar texto. Además, la API no tiene memoria entre llamadas (stateless), por lo que cada petición es independiente y hay que enviar el historial si queremos mantener una conversación.
- **Consumo de mi prueba:** En mi primera ejecución con Llama 3.3 70B en Groq se consumieron 38 tokens de entrada y 75 de salida (113 en total) con coste 0 €.