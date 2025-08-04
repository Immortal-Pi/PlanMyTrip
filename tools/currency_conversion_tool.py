import os 
from utils.currency_convertor import CurrencyConverter
from typing import List 
from langchain.tools import tool
from dotenv import load_dotenv

class CurrencyConverterTool:

    def __init__(self):
        load_dotenv()
        self.api_key=os.environ.get('EXCHANGE_RATE_API_KEY')
        self.currency_service=CurrencyConverter(self.api_key)
        self.currency_conveter_tool_list=self.__setup_tools() 

    def __setup_tools(self):
        """ 
        Setup all tools for the currency converter tool
        """
        @tool 
        def convert_currency(amount:float,from_currency:str, to_currency:str):
            """ 
            convert amount from one currency to another
            """
            return self.currency_service.convert(amount,from_currency,to_currency)
        
        return [convert_currency]

        