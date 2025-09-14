import json
from langchain_core.messages import ToolMessage, SystemMessage
from langchain_core.runnables import RunnableConfig
from graph import AgentState
from models_and_tools import tools

tools_by_name = {tools.name: tool for tool in tools}

# Define our tool nodes
def tool_node(state: AgentState):
    outputs = []
    for tool_call in state["messages"][-1].tool_calls:
        tool_result = tools_by_name[tool_call["name"]].invoke(tool_call["args"])
        outputs.append(
            ToolMessage(
                content=json.dumps(tool_result),
                name=tool_call["name"],
                tool_call_id=tool_call["id"]
        )
    )
    return {"messages": outputs}

#Define the node that calls the model
def call_model(
    state: AgentState,
    config: RunnableConfig
):
    # this is similar to customizing the create_react_agent with "prompt" parameter, but is more flexible
    system_prompt = SystemMessage(
        content = "You are a helpful assistant, please respond to the user's request to the best of your ability."
    )
    response = model.invoke([system_prompt] + state["messages"], config)
    
    # We return a list, because they will get added to the existing list
    return {"messages": [response]}

def should_continue(state: AgentState):
    messages = state["messages"]
    last_message = messages[-1]
    # If there is no function call, then we can end
    if not last_message.tool_calls:
        return "end"
    #Otherwise, we need to call the tool
    else:
        return continue
    
    
    