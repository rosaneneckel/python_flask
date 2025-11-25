from google import genai

#Configurar a API do Gemini-não subir com chave de api no github

client = genai.Client(api_key='AIzaSyBhqBKWzUWu4JgmvP3R_0ciDzuB5KTGO-g')

user_message = input('Qual a sua pergunta? ')

#Criar contexto para aprendizado de programação
prompt = f"""Você é um professor de programação experiente e didático.
Sua missão é ajudar estudantes a aprender programação de forma clara e objetiva.

Pergunta do aluno: {user_message}

Forneça uma resposta educativa, com exemplos práticos quando relevante"""

#Enviar mensagem para ao Gemini
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt
)

print(response.text)