from typing import TypedDict, Dict, Any

class State(TypedDict):
    graph_state: str

def validate_state(state: Dict[str, Any]) -> None:
    if "graph_state" not in state:
        raise ValueError("graph_state is required")
    if not isinstance(state["graph_state"], str):
        raise ValueError("graph_state must be a string")

# This is correct
state1: State = {"graph_state": "initial"}

# These would be caught by type checker:
# state2: State = {"wrong_key": "value"}  # Error: wrong structure
# state3: State = {"graph_state": 123}    # Error: wrong type

# But this would NOT be caught by type checker (no type annotation):
state4 = {"wrong_key": "value"}  # No error because no type hint