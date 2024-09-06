import os
from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from dotenv import dotenv_values

config = {
    **dotenv_values("../.env"),
    }
# print(config)
openai_key = config["OPENAI_API_KEY"]

os.environ["OPENAI_API_KEY"] = openai_key
#
#
client  = OpenAI()
#
#
# prompt = "Number of country in Asia and list of countries name."
#
# response = client.predict(prompt)
#
# print(response)
#
#
# """Prompt Template usecase"""
#
#
# prompt_template_name = PromptTemplate(
#     input_variables = ['country'],
#     template = "can you tell me capital of {country}"
# )
#
# # print(prompt_template_name.format(country='Brunei'))
#
# prompt2 = prompt_template_name.format(country="Brunei")
#
# response = client.predict(prompt2)
# print(response)

prompt3 = PromptTemplate.from_template("What is best selling {product} in word?")

prompt4 = prompt3.format(product="car")

print(client.predict(prompt4))