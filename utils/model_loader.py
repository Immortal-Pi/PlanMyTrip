import os 
from dotenv import load_dotenv
from typing import Literal, Optional, Any 
from pydantic import BaseModel, Field 
# from utils.config_loader import load_config 
from langchain_groq import ChatGroq
from langchain_openai import AzureChatOpenAI 
from utils.config_loader import load_config


class ConfigLoader():
    def __init__(self):
         print(f'Loaded config.....')
         self.config=load_config()

    def __getitem__(self,key):
        return self.config[key]
    


class ModelLoader(BaseModel):
    model_provider: Literal['groq','openai'] = 'groq'
    config: Optional[ConfigLoader]=Field(default=None, exclude=True)

    def model_post_init(self,__context: Any)-> None:
        self.config=ConfigLoader()

    class Config:
        arbitrary_types_allowed=True

    def load_llm(self):
        """ 
        Load and return LLM model 
        """
        print('LLM loading...')
        print(f'Loading model from provider: {self.model_provider}')

        if self.model_provider=='groq':
            print('Loading LLM from Groq ....')
            groq_api_key=os.getenv('GROQ_API_KEY')
            model_name=self.config['llm']['groq']['model_name']
            llm=ChatGroq(model=model_name, api_key=groq_api_key)
        elif self.model_provider=='openai':
            print('Loading LLM from Azure-OpenAI.....')
            model_name=self.config['llm']['openai']['model_name']
            llm=AzureChatOpenAI(
                azure_deployment=model_name,
                api_key=os.getenv('AZURE_OPENAI_GPT_4O_API_KEY'),
                azure_endpoint=self.config['llm']['openai']['end_point'],
                api_version=self.config['llm']['openai']['api_version']
            )

        return llm


