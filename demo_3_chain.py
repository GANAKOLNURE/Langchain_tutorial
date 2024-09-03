import os

from langchain.agents.xml.prompt import agent_instructions
from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from dotenv import dotenv_values
from langchain.agents import AgentType
from langchain_community.agent_toolkits.load_tools import load_tools
from langchain.agents import initialize_agent
from langchain.chains import LLMChain

config = {
    **dotenv_values(".env"),
    }


os.environ["OPENAI_API_KEY"] = config["OPENAI_API_KEY"]
os.environ["SERPAPI_API_KEY"] = config["SERP_API_KEY"]


client  = OpenAI()


prompt = PromptTemplate.from_template("what is a good name for a company that makes {product}")


chain = LLMChain(llm = client, prompt = prompt)

response = chain.run("Whisky")

print(response)



