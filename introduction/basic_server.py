

# python-dotenv: Nos ayuda a importar información desde un archivo .env
from dotenv import load_dotenv

# os: Librería estándar de Python para interactuar con el sistema operativo
import os

# FastAPI: Es una librería que te permite crear APIs con Python de forma rápida
# Tiene soporte para Streaming, WebSockets y maneja la asincronía de una forma fácil para el desarrollador
from fastapi import FastAPI

# langchain_core: Es la librería principal de langChain donde encontramos muchos componentes necesarios para la aplicación
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Con LangChain OpenAI tienes las utilidades necesarias para interactuar con la API de OpenAI
from langchain_openai import ChatOpenAI
# Si quieres usar Anthropic, usa este, para otras API's es similar
# from langchain_anthropic import ChatAnthropic

# O para usar con Ollama en local
# from langchain_community.chat_models import ChatOllama


# LangServe: Una nueva librería de LangChain que te permite servir con velocidad tu aplicación de LangChain, pero que puede funcionar sin ella.
from langserve import add_routes



# Cargar variables de entorno desde el archivo .env
load_dotenv()

# 1. Crear plantilla de prompt. Ten en cuenta que lo que está dentro de {} son variables que el usuario debe agregar
system_template = "Translate the following into {language} and provide a brief explanation:"

# Crear la plantilla de prompt con los mensajes del sistema y del usuario
# La clase ChatPromptTemplate tiene el método from_messages
# Simplemente le pasas una lista de tuplas, donde cada tupla tiene el tipo: system, user y el texto del mensaje

prompt_template = ChatPromptTemplate.from_messages([
    ('system', system_template),
    ('user', '{text}')
])

# 2. Crear modelo
model = ChatOpenAI(
    openai_api_key=os.getenv("OPENAI_API_KEY"),  # Obtener la clave API de OpenAI desde las variables de entorno
    # Busca tu clave acá: https://platform.openai.com/api-keys
    model="gpt-4o-mini",  # Especificar el modelo a utiliza
    temperature="0.3"
)

# 3. Crear parser
# El parser se va a encargar de procesar la salida que otorga el modelo por nosotros
parsero = StrOutputParser() 

# 4. Crear cadena
# Una "cadena" consiste en la unión de los componentes de nuestra app con IA
chain = prompt_template | model | parsero  # Encadenar la plantilla de prompt, el modelo y el parser

"""
NOTA: En Python podemos modificar el comportamiento de los operadores al trabajar con clases. En este caso, LangChain tiene la lógica necesaria para poder usar el operador | en las clases que constituyen a LCEL (LangChain Expresion Language)
"""

# 5. Definición de la aplicación
# Esto no es más que una app de FastAPI básica
app = FastAPI(
  title="Language Tutor",  # Título de la aplicación
  version="1.0",  # Versión de la aplicación
  description="A simple API server using LangChain's Runnable interfaces to act as a language tutor",  # Descripción de la aplicación
)

# 6. Añadir ruta de la cadena
# La función add_routes de LangServe va a agregar las rutas necesarias a nuestra app de FastAPI
add_routes(
    app,
    chain,
    path="/tutor",  # Ruta donde se expondrá la cadena
)

# Nota: Puedes ver el comportamiento de la app en el puerto donde la sirvas y la ruta/{chain_path}/playground
# En este caso sería: localhost:8000/tutor/playground

if __name__ == "__main__":
    import uvicorn

    # Ejecutar la aplicación con Uvicorn
    uvicorn.run(app, host="localhost", port=8000)


"""
Para poner en marcha este paso, solo ejecuta: 
python introduction/intro
"""