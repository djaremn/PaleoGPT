import openai
import config

openai.api_key = config.openai_key


def run():
    mensajes = []
    mensajes.append({"role": "system", "content": config.system_config})

    while True:
        pregunta = input("Escriba una pregunta: ")
        mensajes.append({"role": "user", "content": pregunta})

        respuesta = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",

            messages=mensajes,
        )

        respuesta_assistente = respuesta.choices[0].message['content']
        mensajes.append({"role": "assistant", "content": respuesta_assistente})
        print(respuesta_assistente)
    return



if __name__=="__main__":
    run()
