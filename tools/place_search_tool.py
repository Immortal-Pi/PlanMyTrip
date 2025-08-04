import os 
from utils.place_info_search import GooglePlaceSearchTool, TaviltyPlaceSearchTool 
from typing import List
from langchain.tools import tool
from dotenv import load_dotenv



class PlaceSearchTool:
    def __init__(self):
        load_dotenv()
        self.google_api_key=os.getenv('GPLACE_API_KEY')
        self.google_places_search=GooglePlaceSearchTool(self.google_api_key)
        self.tavily_search=TaviltyPlaceSearchTool()
        self.place_search_tool_list=self.__setup_tools()

    def __setup_tools(self)-> List:
       """ 
       Setup all tools for the place search tool
       """ 
       @tool 
       def search_attractions(place:str)-> str:
           """ 
           Search attractions of a place
           """
           try:
               attraction_result=self.google_places_search.google_search_attractions(place)
               if attraction_result:
                   return f'FLoowing are the attactions of {place} as suggested by google: {attraction_result}'
           except Exception as e:
               tavily_result=self.tavily_search.tavily_search_attractions(place)
               return f'Google cannot find the details due to {e}. \n Following are the attractions of {place}:{tavily_result}'
           
    #     @tool 
    #    def search_restaurents(place:str)->    

    