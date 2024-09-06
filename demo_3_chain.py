import os
import json
from langchain.agents.xml.prompt import agent_instructions
from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from dotenv import dotenv_values
from langchain.agents import AgentType
from langchain_community.agent_toolkits.load_tools import load_tools
from langchain.agents import initialize_agent
from langchain.chains import LLMChain
from langchain.chains import SimpleSequentialChain
from langchain.chains import SequentialChain

config = {
    **dotenv_values("../.env"),
    }


os.environ["OPENAI_API_KEY"] = config["OPENAI_API_KEY"]
os.environ["SERPAPI_API_KEY"] = config["SERP_API_KEY"]


client  = OpenAI()


# prompt = PromptTemplate.from_template("what is a good name for a company that makes {product}")
#
#
# chain = LLMChain(llm = client, prompt = prompt)
#
# response = chain.run("Whisky")
#
# print(response)


prompt = PromptTemplate.from_template("I want to start a restaurant of {cuisine}. suggest me a good name for this")

chain_first = LLMChain(llm=client, prompt= prompt, output_key = "restaurant_name")

prompt_suggest = PromptTemplate.from_template(" suggest some menu items for {restaurant_name}")

chain_two = LLMChain(llm=client, prompt= prompt_suggest, output_key = "menu_items")


chain = SequentialChain(
    chains=[chain_first, chain_two],
    input_variables = ["cuisine"],
    output_variables = ["restaurant_name", "menu_items"]
)

response = chain({"cuisine": "Italian"})
print(response)


