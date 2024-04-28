import openai
import os
from IPython.display import display, HTML, Markdown

from dotenv import load_dotenv, find_dotenv
from redlines import Redlines


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

text = f"""
Got this for my daughter for her birthday cuz she keeps taking \
mine from my room.  Yes, adults also like pandas too.  She takes \
it everywhere with her, and it's super soft and cute.  One of the \
ears is a bit lower than the other, and I don't think that was \
designed to be asymmetrical. It's a bit small for what I paid for it \
though. I think there might be other options that are bigger for \
the same price.  It arrived a day earlier than expected, so I got \
to play with it myself before I gave it to my daughter.
"""
prompt = f"proofread and correct this review: ```{text}```"
response = get_completion(prompt)
print(response)
diff = Redlines(text,response)
display(Markdown(diff.output_markdown))
