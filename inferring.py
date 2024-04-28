import openai
import os
from IPython.display import display, HTML

from dotenv import load_dotenv, find_dotenv

# Carrega as variáveis de ambiente do arquivo .env, para manter a chave da API segura
_ = load_dotenv(find_dotenv())

# Atribui a chave da API da OpenAI à variável para uso na biblioteca
openai.api_key = os.getenv('OPENAI_API_KEY')

# Função para obter uma conclusão de texto usando o modelo da OpenAI
def get_completion(prompt, model="gpt-3.5-turbo", temperature=0):
    """
    Solicita uma conclusão de texto à API da OpenAI.

    Args:
        prompt (str): O texto que descreve o que o modelo deve fazer.
        model (str): O modelo da OpenAI a ser usado. Padrão é 'gpt-3.5-turbo'.
        temperature (float): O grau de aleatoriedade na resposta do modelo. Padrão é 0 (mais determinístico).

    Returns:
        str: A resposta do modelo baseada no prompt fornecido.
    """
    response = openai.Completion.create(
        model=model,
        prompt=prompt,
        temperature=temperature,
        max_tokens=150  # Limita o número de tokens na resposta para controlar o custo e a extensão
    )
    return response.choices[0].text.strip()  # Retorna a resposta processada sem espaços extras

lamp_review = """
Needed a nice lamp for my bedroom, and this one had \
additional storage and not too high of a price point. \
Got it fast.  The string to our lamp broke during the \
transit and the company happily sent over a new one. \
Came within a few days as well. It was easy to put \
together.  I had a missing part, so I contacted their \
support and they very quickly got me the missing piece! \
Lumina seems to me to be a great company that cares \
about their customers and products!!
"""

prompt = f"""
What is the sentiment of the following product review, 
which is delimited with triple backticks?

Review text: '''{lamp_review}'''
"""
response = get_completion(prompt)
print(response)

prompt = f"""
What is the sentiment of the following product review, 
which is delimited with triple backticks?

Give your answer as a single word, either "positive" \
or "negative".

Review text: '''{lamp_review}'''
"""
response = get_completion(prompt)
print(response)

prompt = f"""
Identify a list of emotions that the writer of the \
following review is expressing. Include no more than \
five items in the list. Format your answer as a list of \
lower-case words separated by commas.

Review text: '''{lamp_review}'''
"""
response = get_completion(prompt)
print(response)

prompt = f"""
Is the writer of the following review expressing anger?\
The review is delimited with triple backticks. \
Give your answer as either yes or no.

Review text: '''{lamp_review}'''
"""
response = get_completion(prompt)
print(response)

prompt = f"""
Identify the following items from the review text: 
- Item purchased by reviewer
- Company that made the item

The review is delimited with triple backticks. \
Format your response as a JSON object with \
"Item" and "Brand" as the keys. 
If the information isn't present, use "unknown" \
as the value.
Make your response as short as possible.
  
Review text: '''{lamp_review}'''
"""
response = get_completion(prompt)
print(response)

prompt = f"""
Identify the following items from the review text: 
- Sentiment (positive or negative)
- Is the reviewer expressing anger? (true or false)
- Item purchased by reviewer
- Company that made the item

The review is delimited with triple backticks. \
Format your response as a JSON object with \
"Sentiment", "Anger", "Item" and "Brand" as the keys.
If the information isn't present, use "unknown" \
as the value.
Make your response as short as possible.
Format the Anger value as a boolean.

Review text: '''{lamp_review}'''
"""
response = get_completion(prompt)
print(response)