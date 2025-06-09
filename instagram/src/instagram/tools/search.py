import requests
import json
import os

from langchain.tools import Tool
from langchain_community.document_loaders import WebBaseLoader
from langchain_core.tools import Tool
from dotenv import load_dotenv


load_dotenv()


class SearchTools:

    #@tool('search_internet')
    @staticmethod 
    def search_internet_tool():
        #always add a docstring for your tools, your agent is going to be able to read these docstrings and decide based on description whether or not to use this tool for a given task
        """
        Use this tool to search the internet for information. This tool returns 5 results from 
        Google search engine.
        """
        #return SearchTools.search(query)
        return Tool.from_function(
            name="search_internet",
            description="Search the internet using Google for any general information.",
            func=lambda query: SearchTools.search(query)
            
        )
    
    #@tool('search_instagram')
    @staticmethod
    def search_instagram_tool():
        """
        Use this tool to search Instagram. This tool returns 5 results from Instagram pages.
        """
        #return SearchTools.search(f"site:instagram.com {query}", limit=5)
        return Tool.from_function(
            name="search_instagram",
            description="Search Instagram-specific content using Google search with site:instagram.com.",
            func=lambda query: SearchTools.search(f"site:instagram.com {query}", limit=5)
            
        )

    
    #@tool('open page')
    @staticmethod
    def open_page_tool():
        """
        Use the tool to open a webpage and get the content.
        """
        #loader = WebBaseLoader(url)
        #return loader.load()
        return Tool.from_function(
            name="open_page",
            description="Open a webpage URL and extract readable content.",
            func=lambda url: WebBaseLoader(url).load()
            
        )


    def search(query, limit=5):
        

        url = "https://google.serper.dev/search"
        payload = json.dumps({
            "q": query,
            "num": limit,
        })
        headers = {
        'X-API-KEY': os.getenv("SERPER_API_KEY"),
        'Content-Type': 'application/json'
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        results = response.json()['organic']


        string = []
        for result in results :
            string.append(f"{result['title']}\n{result['snippet']}\n{result['link']}\n\n")

        return f"Search results for '{query}':\n\n" + "\n".join(string)

        

#if __name__ == "__main__" :
    #from dotenv import load_dotenv
    #load_dotenv()
    #print(SearchTools.search_internet("How to make a cake"))
    #print(SearchTools.search_instagram("How to make a cake"))


