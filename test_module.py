#--------------------------------
#initialize the model
#--------------------------------
import os
from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env file

#--------------------------------
#test if the api key is working and the model is working
#--------------------------------

def test_api_key(): 
    """Check if the GROQ_API_KEY is present in the environment variables."""
    print("Key found:", "GROQ_API_KEY" in os.environ)
    from langchain.chat_models import init_chat_model
    model = init_chat_model("groq:llama-3.3-70b versatile")
    respose = model.invoke("hello")
    print(respose.content)


print("Key found:", "GROQ_API_KEY" in os.environ)

from langchain.chat_models import init_chat_model
model = init_chat_model("groq:llama-3.3-70b-versatile")


#--------------------------------
#test the model
#--------------------------------
'''
response = model.invoke("hello, give basic information about yourself what model are you what organisation etc")
print(response.content)
'''
#--------------------------------
#initialize tools   
#--------------------------------
from langchain_core.tools import tool 
import math

@tool
def add_numbers(a: float, b: float) -> float:
    """Add two numbers together."""
    return a + b

@tool
def multiply_numbers(a: float, b: float) -> float:
    """Multiply two numbers together."""
    return a * b

@tool
def divide_numbers(a: float, b: float) -> float:
    """Divide two numbers together."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

@tool
def square_root(a: float) -> float:
    """Calculate the square root of a number."""
    if a < 0:
        raise ValueError("Cannot calculate the square root of a negative number.")
    return math.sqrt(a)

tools = [add_numbers, multiply_numbers, divide_numbers, square_root]


#--------------------------------
#asking for prompt
#--------------------------------

prmt = input("Enter your prompt: ")



#--------------------------------
#initialize agent       
#--------------------------------
from langchain.agents import create_agent

agent = create_agent(
    model=model,
    tools=tools,
)

#--------------------------------
# invoke the agent with a prompt
#--------------------------------   

def run_agent(prompt: str):
    """Run the agent with the given prompt and return the response.
    """
    print(f"Prompt: {prompt}")
    print("Agent is thinking...")

    result = agent.invoke({
        "messages": [("user", prompt)]


    })
    final_response = result["messages"][-1].content  # Get the last message from the agent's response
    print("Agent response:" + final_response)


run_agent(prmt)

