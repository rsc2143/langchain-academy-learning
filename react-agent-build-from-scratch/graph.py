from typing import(
    TypedDict,
    Annotated,
    Sequence    
)
from langchain.core.messages import BaseMessage
from langchain.graph.message import add_messages
from dataclasses import dataclass, field

class AgentState(TypedDict):
    """The state of the agent"""
    # add_message is a reducer function that allows us to add messages to the state
    messages: Annotated[Sequence[BaseMessage], add_messages] = field(default_factory=list)
    