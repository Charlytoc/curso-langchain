from openai import OpenAI
from dotenv import load_dotenv

import requests

import os
import random

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def text_to_speech(text: str, filename: str):
    voices_options = ["alloy", "echo", "fable", "onyx", "nova", "shimmer"]
    voice = random.choice(voices_options)

    response = client.audio.speech.create(
        model="tts-1",
        voice=voice,
        input=text,
    )
    response.stream_to_file(filename)


def generate_dalle_image(
    prompt,
    model="dall-e-3",
    size="1024x1024",
    quality="standard",
    output_file="image.png",
):
    """
    Genera una imagen usando la API de DALL·E de OpenAI y la guarda como un archivo PNG.

    Args:
        prompt (str): Descripción de la imagen a generar.
        model (str): Modelo a usar, por defecto "dall-e-3".
        size (str): Tamaño de la imagen, por defecto "1024x1024".
        quality (str): Calidad de la imagen ("standard" o "hd" para DALL·E 3).
        output_file (str): Nombre del archivo donde se guardará la imagen, por defecto "image.png".

    Returns:
        str: Ruta del archivo guardado.
    """
    # Verificar si la clave API está configurada
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError(
            "La clave API de OpenAI no está configurada. Usa la variable de entorno 'OPENAI_API_KEY'."
        )

    # Endpoint de la API
    url = "https://api.openai.com/v1/images/generations"

    # Configurar los datos de la solicitud
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {api_key}"}
    data = {
        "model": model,
        "prompt": prompt,
        "n": 1,  # Solo generamos una imagen
        "size": size,
    }

    # Agregar calidad si se usa DALL·E 3
    if model == "dall-e-3" and quality == "hd":
        data["quality"] = "hd"

    # Realizar la solicitud POST
    response = requests.post(url, headers=headers, json=data)

    # Manejar errores
    if response.status_code != 200:
        raise Exception(f"Error en la API: {response.status_code} - {response.json()}")

    # Extraer la URL de la imagen generada
    response_data = response.json()
    image_url = response_data["data"][0]["url"]

    # Descargar la imagen y guardarla como archivo
    image_response = requests.get(image_url)
    if image_response.status_code == 200:
        with open(output_file, "wb") as f:
            f.write(image_response.content)
        print(f"Imagen guardada como {output_file}")
        return output_file
    else:
        raise Exception(f"Error al descargar la imagen: {image_response.status_code}")
