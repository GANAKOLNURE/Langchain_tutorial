import os

from langchain.chains import LLMChain
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain.memory import ConversationBufferWindowMemory
from langchain.prompts import PromptTemplate
from langchain_openai import OpenAI
from dotenv import dotenv_values


config = {
    **dotenv_values("../.env"),
    }

openai_key = config["OPENAI_API_KEY"]


os.environ["OPENAI_API_KEY"] = openai_key

client = OpenAI(openai_api_key = openai_key)


prompt = PromptTemplate.from_template("what is a good name for a company that makes {product}?")

# chain = LLMChain(llm=client, prompt=prompt, )
#
# print(chain.run("colorful cup"))


"""
    Conversation Buffer Memory
"""

memory = ConversationBufferMemory()

chain = LLMChain(llm=client, prompt=prompt, memory=memory)

chain.run("Beer")

chain.run("camera")

chain.run("Drones")

# print(chain.memory)
#
# print(chain.memory.buffer)

"""
    Conversation Chain
"""

convo = ConversationChain(llm=OpenAI(temperature=0.7))
# print(convo.prompt)
# print(convo.prompt.template)

# print(convo.run("who won the first cricket world cup?"))
#
# print(convo.run("what is 5+5"))
#
# print(convo.run("who was the captain of winning team?"))
#
# print("*"*10)
#
# print(convo.prompt)

"""
    Conversation Buffer Window Memory
"""

memory=ConversationBufferWindowMemory(k=1)
convo=ConversationChain(llm=OpenAI(temperature=0.7), memory=memory)

print(convo.run("winner of first cricket world cup"))
print(convo.run("can you tell me how much 5*10"))
print(convo.run("captain of winning team"))