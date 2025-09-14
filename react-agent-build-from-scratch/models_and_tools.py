from langchain_openai import ChatOpenAI
from langchain_core.tools import tool

model = ChatOpenAI(model="gpt-4o-mini")

@tool
def get_weather(location: str) -> str:
    """Call to get the weather for a given location"""
    if (city == "San Francisco"):
        return "It's sunny in San Francisco"
    elif (city == "New York"):
        return "It's cloudy in New York"
    else:
        return "I don't know the weather for this location"

@tool
def get_rain_information(location: str) -> str:
    """Call to get the rain information for a given location"""
    if (location == "San Francisco"):
        return "It's raining in San Francisco"
    elif (location == "New York"):
        return "It's raining in New York"
    else:
        return "I don't know the rain information for this location"
    
tools = [get_weather, get_rain_information]
model_with_tools = model.bind_tools(tools)
