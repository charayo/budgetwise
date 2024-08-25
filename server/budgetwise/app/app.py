import os
from getpass import getpass
from langchain_ibm import WatsonxLLM
from langchain_core.prompts import PromptTemplate


class BudgetWiseLLM:
    def __init__(self):
        self.watsonx_api_key = os.getenv("WATSONX_API_KEY")
        self.parameters = {
            "decoding_method": "greedy",
            "max_new_tokens": 1000,
            "min_new_tokens": 10,
            "temperature": 0.1,
        }

    def init_watsonx_llm(self):
        watsonx_llm = WatsonxLLM(
            model_id="ibm/granite-13b-instruct-v2",
            url="https://us-south.ml.cloud.ibm.com",
            project_id="99111f47-1aa8-45d9-963a-4da924a02ee6",
            apikey= self.watsonx_api_key,
            params=self.parameters,
        )
        return watsonx_llm

    def init_agent(self):
        template = "You are BudgetWise, an AI-powered personal finance assistant. Your purpose is to help users manage their finances efficiently by analyzing their income, expenses, and financial goals (Budget). You receive a user's income, budget and breakdown of their expenses according to some categories like groceries, transportation, internet, rent, party, clothes and shoes e.t.c. With that information, provide a personalized budget plans. You offer tailored advice to ensure users can meet their savings goals, and manage their expenses. Your goal is to provide clear, elaborate and actionable financial insights and strategies in a user-friendly and accessible manner, empowering users to stay on top of their financial well-being. With the above details, answer this query {query} accurately."

        prompt = PromptTemplate.from_template(template)

        # llm_chain = LLMChain(prompt=prompt, llm=watsonx_llm)
        agent = prompt | self.init_watsonx_llm()
        return agent

    # question1 = """
    # I have a monthly income of $10000, a budegt of $5000 and my expenses are as follows:
    # - Groceries: $1000
    # - Transportation: $500
    # - Internet: $100
    # - Rent: $2000
    # - Party: $500
    # - Clothes and shoes: $500
    # - Others: $400
    # """
    def generate_response(self, question):
        response = self.init_agent().invoke({"query": question})
        return response
