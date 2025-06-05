from typing import Dict, TypedDict, List

class ChatState(TypedDict):
    messages: List[Dict[str, str]]