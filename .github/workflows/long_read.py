import openai

# Establece tus credenciales de la API de OpenAI
openai.api_key = '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'

# Función para dividir el texto en párrafos
def dividir_texto(texto, longitud_maxima):
    parrafos = []
    palabras = texto.split()
    parrafo_actual = palabras[0]
    
    for palabra in palabras[1:]:
        if len(parrafo_actual) + len(palabra) + 1 <= longitud_maxima:  # +1 para tener en cuenta el espacio en blanco
            parrafo_actual += ' ' + palabra
        else:
            parrafos.append(parrafo_actual)
            parrafo_actual = palabra
    
    parrafos.append(parrafo_actual)
    return parrafos

# Lee el texto desde el archivo
archivo = ".github/workflows/output2.txt"
ruta_absoluta = os.path.abspath(archivo)

with open(archivo, "r", encoding="utf-8") as file:
    texto_inicial = file.read()

# Define la longitud máxima para cada fragmento
longitud_maxima = 3000  # Puedes ajustar este valor según tus necesidades

# Divide el texto en párrafos
parrafos = dividir_texto(texto_inicial, longitud_maxima)

# Lee el texto fragmentado
for parrafo in parrafos:
    print(parrafo)
    input("Presiona Enter para continuar leyendo...")

# Interactúa con el usuario y responde preguntas basadas en los fragmentos
while True:
    pregunta = input("Hazme una pregunta sobre el texto (o escribe 'salir' para terminar): ")
    
    if pregunta.lower() == "salir":
        break
    
    respuesta_encontrada = False
    
    for parrafo in parrafos:
        # Envía la pregunta y el fragmento de texto a OpenAI para obtener la respuesta
        respuesta = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": parrafo + "\nQuestion: " + pregunta}
            ]
        )
        
        if respuesta.choices[0].message['role'] == 'assistant':
            print("Respuesta:", respuesta.choices[0].message['content'])
            respuesta_encontrada = True
            break
    
    if not respuesta_encontrada:
        print("Lo siento, no pude encontrar una respuesta para tu pregunta.")
