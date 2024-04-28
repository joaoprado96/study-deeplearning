from transformers import GPT2Tokenizer, GPT2LMHeadModel, pipeline

# Carrega o tokenizer e o modelo
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
model = GPT2LMHeadModel.from_pretrained('gpt2')

# Inicializa a pipeline de geração de texto
generator = pipeline('text-generation', model=model, tokenizer=tokenizer)

def get_response(message):
    # Gera uma resposta com base na entrada do usuário
    responses = generator(message, max_length=len(message.split()) + 50, num_return_sequences=1)
    return responses[0]['generated_text']

# Simulação de uma sessão de chat
print("Bem-vindo ao Chatbot GPT-2! Digite 'sair' para terminar.")
while True:
    user_input = input("Você: ")
    if user_input.lower() == 'sair':
        break
    response = get_response(user_input)
    print("Bot:", response)
