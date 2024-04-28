from transformers import pipeline, set_seed

# Inicialização do gerador de texto com GPT-2
generator = pipeline('text-generation', model='gpt2')
set_seed(42)

def get_response(message):
    # Gerar uma resposta com base na entrada do usuário
    responses = generator(message, max_length=100, num_return_sequences=1)
    return responses[0]['generated_text']

# Simulação de uma sessão de chat
print("Bem-vindo ao Chatbot GPT! Digite 'sair' para terminar.")
while True:
    user_input = input("Você: ")
    if user_input.lower() == 'sair':
        break
    response = get_response(user_input)
    print("Bot:", response)
