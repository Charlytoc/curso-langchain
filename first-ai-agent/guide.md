# Building an AI Agent with Tools using LangChain

This guide will help you through the process of building an AI Agent with Tools using LangChain. All the source code is in the [main.py](main.py) file.


## What is an AI Agent?

An AI Agent is a program that can perform tasks autonomously, using tools to accomplish goals. It is basically a LLM that is capable of using different functions to accomplish a task. For example, a typical task can be to search the web for information, or to send an email. The AI Agent can use different tools to accomplish these tasks. 


### Prerequisites

- Python 3.10 or higher
- OpenAI API key
- Tavily API key

### Setting up the project

1. Create a virtual environment

```bash
python -m venv .venv
```

2. Activate the virtual environment

```bash
source .venv/bin/activate
```

or

```bash
.\.venv\Scripts\activate
```

### Installing dependencies

Install the latest version of Langchain

```bash
pip install -qU langchain
```

Install Python dotenv

```bash
pip install python-dotenv
```

Install Python Pyttsx3

```bash
pip install pyttsx3
```

Install LangGraph

```bash
pip install -qU langgraph
```

Install Langchain OpenAI

```bash
pip install -qU langchain-openai
```

Install Tavily Search

```bash
pip install -U langchain-community tavily-python
```

### Setting up the environment variables

Create a .env file in the root of the project and add the following variables:

```bash
OPENAI_API_KEY=your_openai_api_key
TAVILY_API_KEY=your_tavily_api_key
```

### Run the AI Agent

```bash
python first-ai-agent/main.py
```
