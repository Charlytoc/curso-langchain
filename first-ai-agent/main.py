# Import relevant functionality
from langchain_openai import ChatOpenAI

from langchain_core.tools import tool
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.messages import HumanMessage
from langgraph.checkpoint.memory import MemorySaver
from langgraph.prebuilt import create_react_agent
import os

from openai_functions import text_to_speech, generate_dalle_image

from dotenv import load_dotenv

load_dotenv()


@tool
def multiply_numbers(x: int, y: int) -> int:
    """
    This tool multiplies two given numbers
    """
    return x * y


@tool
def send_email(email: str, subject: str, body: str) -> str:
    """
    This tool opens the default email client and sends an email to the given email address with the given subject and body
    """

    os.system(f"start mailto:{email}?subject={subject}&body={body}")
    return f"Email sent to {email} with subject {subject} and body {body}"


@tool
def speak(text: str) -> str:
    """
    This tool speaks the given text using the default text-to-speech engine
    """
    text_to_speech(text, "output.mp3")
    # REproduce the audioobs
    os.system("start output.mp3")
    return True


@tool
def generate_image(prompt: str) -> str:
    """
    This tool generates an image using DALL·E 3
    """
    generate_dalle_image(prompt)
    return True


# Create the agent
memory = MemorySaver()
model = ChatOpenAI(model_name="gpt-4o-mini")
search = TavilySearchResults(max_results=2)

tools = [
    search,
    multiply_numbers,
    send_email,
    speak,
    generate_image,
]

agent_executor = create_react_agent(model, tools, checkpointer=memory)

config = {"configurable": {"thread_id": "abc123"}}


def main():
    for chunk in agent_executor.stream(
        {
            "messages": [
                HumanMessage(
                    content="speak 'Hola, pronto voy a dominar a la humanidad'"
                )
            ]
        },
        config,
    ):
        print(chunk)
        print("----")

    for chunk in agent_executor.stream(
        {
            "messages": [
                HumanMessage(content="generate an image of a robot with a red hat")
            ]
        },
        config,
    ):
        print(chunk)
        print("----")

    for chunk in agent_executor.stream(
        {
            "messages": [
                HumanMessage(content="Que clima hace en Cuenca Ecuador?")
            ]
        },
        config,
    ):
        print(chunk)
        print("----")

    
    for chunk in agent_executor.stream(
        {
            "messages": [
                HumanMessage(content="quiero enviar un correo a mi jefe: Su email es: juan@gmail.com. Dile que lo quiero que haga un curso de python.")
            ]
        },
        config,
    ):
        print(chunk)
        print("----")


if __name__ == "__main__":
    main()
