from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
from secret_key import openai_api_key

import os
os.environ['OPENAI_API_KEY'] = openai_api_key

llm = OpenAI(temperature=0.6)

def generate_name_items(cuisine):
    
    #Chain 1: Restaurant name
    prompt_template_name = PromptTemplate(
        input_variables = ['cuisine'],
        template = "I want to open a restaurant for {cuisine} food. Suggest a fancy name for this."
    )

    name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key='restaurant_name')

    #Chain 2: Menu items
    prompt_template_items = PromptTemplate(
        input_variables = ['restaurant_name'],
        template= "Suggest some menu items for {restaurant_name}. Return it as comma seperated list"
    )

    menu_items_chain = LLMChain(llm=llm, prompt=prompt_template_items, output_key='menu_items')

    chain = SequentialChain(
        chains = [name_chain, menu_items_chain],
        input_variables = ['cuisine'],
        output_variables = ['restaurant_name', 'menu_items']
    )

    chain({'cuisine': 'Arabic'})