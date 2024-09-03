import os

from langchain.agents.xml.prompt import agent_instructions
from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from dotenv import dotenv_values
from langchain.agents import AgentType
from langchain_community.agent_toolkits.load_tools import load_tools
from langchain.agents import initialize_agent

config = {
    **dotenv_values(".env"),
    }


os.environ["OPENAI_API_KEY"] = config["OPENAI_API_KEY"]
os.environ["SERPAPI_API_KEY"] = config["SERP_API_KEY"]
#
#
client  = OpenAI()

"""
    for real time info we are using serp api
    Using google serach api in real time
"""

tool = load_tools(
    ['serpapi'],
    llm=client,
)

agent = initialize_agent(
    tool,
    client,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

# response = agent.run("tell me latest update about ICC cricket world cup")
# print(response)

tool_wiki = load_tools(
    ['wikipedia'],
    llm= client,
)

agent_wiki = initialize_agent(
    tool_wiki,
    client,
    agent = AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    # verbose = True,
)

print(agent_wiki.run('tell me about India medival period'))