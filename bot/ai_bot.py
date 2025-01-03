import os
from decouple import config
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq

os.environ['GROQ_API_KEY'] = config('GROQ_API_KEY')

class AIBot:
    def __init__(self):
        self.__chat = ChatGroq(model='llama-3.1-70b-versatile')

    def invoke(self, question):
        prompt = PromptTemplate(
            input_variables=['pergunta'],
            template='''Vocẽ é um cara para conversar, responde o usuario da melhor forma possivel,
             e conhecedor de muitas coisas que tem resposta pra tudo.
              Use emoji sempre que possivel {pergunta}'''
        )
        chain = prompt | self.__chat | StrOutputParser()
        response = chain.invoke({
            'pergunta': question,
        })
        return response
