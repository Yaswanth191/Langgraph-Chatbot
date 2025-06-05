from langgraph.graph import END, StateGraph
from typing import Dict, Any
from .state import ChatState
from .model import create_cohere_model

_model = create_cohere_model()

def get_response(state: ChatState) -> Dict[str, Any]:
    last_message = state["messages"][-1]["content"]
    response = _model.generate_response(f"User said: {last_message}")
    return {"messages": state["messages"] + [{"role": "assistant", "content": response}]}

def create_workflow():
    workflow = StateGraph(ChatState)
    workflow.add_node("respond", get_response)
    workflow.set_entry_point("respond")
    
    # Just end after one response (no recursion inside graph)
    workflow.add_edge("respond", END)
    
    return workflow.compile(checkpointer=None)
