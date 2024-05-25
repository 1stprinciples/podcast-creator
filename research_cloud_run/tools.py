from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_community.utilities.tavily_search import TavilySearchAPIWrapper
from langchain.tools import Tool
from langchain_community.tools.google_scholar import GoogleScholarQueryRun
from langchain_community.utilities.google_scholar import GoogleScholarAPIWrapper
from crewai_tools import SerperDevTool, \
                         ScrapeWebsiteTool, \
                         WebsiteSearchTool


# Search tool
def get_tavily_search_tool(tavily_api_key: str = None) -> Tool:
    description = """A search engine optimized for comprehensive, accurate, \
        and trusted     results. Useful for when you need to answer questions \
        about current events or about recent information. \
        Input should be a search query. \
        If the user is asking about something that you don't know about, \
        you should probably use this tool to see if that can provide any information."""
    search = TavilySearchAPIWrapper(tavily_api_key=tavily_api_key)
    tavily_tool = TavilySearchResults(api_wrapper=search, description=description)

    return tavily_tool

tavily_search_tool = get_tavily_search_tool()


# Google scholar tool
google_scholar_tool = GoogleScholarQueryRun(api_wrapper=GoogleScholarAPIWrapper())

# Search tool
search_tool = SerperDevTool()

# Scrape website tool
scrape_website_tool = ScrapeWebsiteTool()
