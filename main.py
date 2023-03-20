#import openai_secret_manager
import openai
import json



# OpenAI API anahtarını kullanarak API istemcisini oluşturun
openai.api_key = ""
model_engine = "text-davinci-003" # model ismi

def ask_chat_gpt(prompt):
    # ChatGPT'den cevap almak için OpenAI API'sini kullanın
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )

    message = response.choices[0].text.strip()
    return message

# Kullanıcıdan soru alın
question = input("Soru girin: ")

# ChatGPT'ye soruyu gönderin ve cevabını alın
response = ask_chat_gpt(question)

# Cevabı yazdırın
print(response)