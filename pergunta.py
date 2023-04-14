import openai 

openai.api_key = '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'


def fazer_pergunta(pergunta):
    engine = "text-davinci-002"
    prompt = f"Fazer uma pergunta: {pergunta}"
    completions = openai.Completion.create(engine=engine, prompt=prompt, max_tokens=1024)
    resposta = completions.choices[0].text.strip()
    return resposta

pergunta = input("> ")
respostaChatGPT = fazer_pergunta(pergunta)
print("Resposta do ChatGPT : ", respostaChatGPT)
