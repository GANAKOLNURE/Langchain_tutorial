import os

from dotenv import dotenv_values
from langchain_huggingface import HuggingFaceEndpoint
from langchain import PromptTemplate

config = {
    **dotenv_values("../.env")
}

huggingface_api_key = config["HUGGINGFACE_API_KEY"]

os.environ["HUGGINGFACEHUB_API_TOKEN"] = huggingface_api_key

llm = HuggingFaceEndpoint(
    repo_id="google/flan-t5-large",
    max_length=128,
    max_new_tokens=250
    ,
    temperature=0.5,
    huggingfacehub_api_token=huggingface_api_key)

prompt = PromptTemplate.from_template("what is a good name for a company that makes {product}")

chain = prompt | llm

print(chain.invoke("leather"))



llm = HuggingFaceEndpoint(
    repo_id="facebook/mbart-large-50",
    max_length=128,
    max_new_tokens=250,
    temperature=0.5,
    huggingfacehub_api_token=huggingface_api_key,)

chain_2 = prompt | llm_2

print(chain_2.invoke("leather"))