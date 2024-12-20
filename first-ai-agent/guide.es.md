# Construyendo un Agente de IA con Herramientas usando LangChain

Esta guía te ayudará en el proceso de construir un Agente de IA con Herramientas utilizando LangChain. Todo el código fuente se encuentra en el archivo [main.py](main.py).


## ¿Qué es un Agente de IA?

Un Agente de IA es un programa que puede realizar tareas de manera autónoma, utilizando herramientas para alcanzar objetivos. Básicamente, es un modelo de lenguaje (LLM) capaz de usar diferentes funciones para cumplir con una tarea. Por ejemplo, una tarea típica podría ser buscar información en la web o enviar un correo electrónico. El Agente de IA puede usar diferentes herramientas para realizar estas tareas.


### Requisitos previos

- Python 3.10 o superior (https://www.python.org/downloads/)
- Clave de API de OpenAI (https://platform.openai.com)
- Clave de API de Tavily (https://tavily.com/)

### Configuración del proyecto

1. Crea un entorno virtual

```bash
python -m venv .venv
```

2. Activa el entorno virtual

```bash
source .venv/bin/activate
```

o

```bash
.\.venv\Scripts\activate
```

### Instalación de dependencias

Instala la última versión de LangChain

```bash
pip install -qU langchain langgraph langchain-openai langchain-community tavily-python python-dotenv
```

### Configuración de las variables de entorno

Crea un archivo .env en la raíz del proyecto y agrega las siguientes variables:

```bash
OPENAI_API_KEY=tu_clave_de_api_de_openai
TAVILY_API_KEY=tu_clave_de_api_de_tavily
```

### Ejecuta el Agente de IA

```bash
python first-ai-agent/main.py
```